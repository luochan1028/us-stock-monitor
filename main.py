"""
美股关键经济数据监控主程序

功能:
1. 计算数据发布时间倒计时
2. 分析数据可能造成的市场影响
3. 通过 WxPusher 推送到微信
4. 支持多级提醒 (提前1天、1小时、15分钟)
5. 每周推送数据日历

使用方式:
    python main.py              # 运行一次检查
    python main.py --weekly     # 推送本周日历
    python main.py --daemon     # 持续运行模式
"""

import datetime
import time
import sys
import os
import logging
import pytz
import argparse

# 添加项目根目录到路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config.settings import REMIND_INTERVALS, LOG_DIR, LOG_FILE, TIMEZONE
from config.data_calendar import get_this_week_events, ECONOMIC_CALENDAR, get_next_event_datetime
from utils.wxpusher import WxPusher


# 配置日志
os.makedirs(LOG_DIR, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(os.path.join(LOG_DIR, LOG_FILE), encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


class USStockMonitor:
    """美股数据监控器"""

    def __init__(self):
        self.pusher = WxPusher()
        self.timezone = pytz.timezone(TIMEZONE)
        self._pushed_events = {}  # 记录已推送的事件，避免重复

    def get_current_time(self):
        """获取当前北京时间"""
        return datetime.datetime.now(self.timezone)

    def calculate_countdown(self, event_datetime):
        """
        计算倒计时

        Args:
            event_datetime: 事件时间 (datetime)

        Returns:
            dict: 包含剩余天、时、分、秒
        """
        now = self.get_current_time()
        delta = event_datetime - now

        if delta.total_seconds() < 0:
            return None  # 事件已过期

        days = delta.days
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        return {
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds,
            "total_minutes": delta.total_seconds() / 60,
        }

    def check_events(self):
        """检查所有事件，推送需要提醒的事件"""
        logger.info("开始检查数据发布事件...")

        events = get_this_week_events()

        if not events:
            logger.info("没有检测到即将发布的事件")
            return

        logger.info(f"检测到 {len(events)} 个即将发布的事件")

        now = self.get_current_time()

        for event in events:
            event_id = event["id"]
            event_dt = event["datetime"]

            countdown = self.calculate_countdown(event_dt)
            if countdown is None:
                continue

            total_minutes = countdown["total_minutes"]

            # 检查是否到达提醒时间点
            for remind_minutes in REMIND_INTERVALS:
                # 允许 5 分钟的误差窗口
                if abs(total_minutes - remind_minutes) <= 5:
                    push_key = f"{event_id}_{remind_minutes}"
                    if push_key not in self._pushed_events:
                        logger.info(
                            f"推送提醒: {event['config']['name']} - "
                            f"提前 {remind_minutes} 分钟"
                        )
                        self.pusher.send_countdown_reminder(event, remind_minutes)
                        self._pushed_events[push_key] = now

            # 清理过期记录 (超过1天的)
            self._clean_old_records()

    def _clean_old_records(self):
        """清理超过24小时的推送记录"""
        now = self.get_current_time()
        expired_keys = []
        for key, push_time in self._pushed_events.items():
            if (now - push_time).total_seconds() > 86400:
                expired_keys.append(key)
        for key in expired_keys:
            del self._pushed_events[key]

    def send_weekly_calendar(self):
        """推送本周数据日历"""
        logger.info("推送本周数据日历...")
        events = get_this_week_events()
        self.pusher.send_weekly_calendar(events)

    def print_countdown_dashboard(self):
        """在控制台打印倒计时面板"""
        events = get_this_week_events()

        print("\n" + "=" * 60)
        print("📊 美股关键经济数据倒计时面板")
        print("=" * 60)

        if not events:
            print("本周暂无即将发布的重要数据")
            return

        for event in events:
            config = event["config"]
            dt = event["datetime"]
            countdown = self.calculate_countdown(dt)

            if countdown is None:
                continue

            imp_emoji = {
                "critical": "🔴",
                "high": "🟡",
                "medium": "🟢",
            }
            emoji = imp_emoji.get(config["importance"], "⚪")

            print(f"\n{emoji} {config['name']}")
            print(f"   发布时间: {dt.strftime('%Y-%m-%d %H:%M')} (北京)")
            print(
                f"   倒计时: {countdown['days']}天 "
                f"{countdown['hours']}小时 "
                f"{countdown['minutes']}分钟"
            )

            if "impact_analysis" in config and "key_point" in config["impact_analysis"]:
                print(f"   关注: {config['impact_analysis']['key_point']}")

        print("\n" + "=" * 60)

    def run_daemon(self, check_interval=300):
        """
        持续运行模式

        Args:
            check_interval: 检查间隔 (秒), 默认5分钟
        """
        logger.info(f"启动守护进程模式，检查间隔: {check_interval}秒")

        # 先推送一次周历
        self.send_weekly_calendar()

        while True:
            try:
                self.check_events()
                self.print_countdown_dashboard()
                logger.info(f"下次检查: {check_interval}秒后")
                time.sleep(check_interval)
            except KeyboardInterrupt:
                logger.info("收到中断信号，退出...")
                break
            except Exception as e:
                logger.error(f"发生错误: {e}", exc_info=True)
                time.sleep(60)  # 出错后等待1分钟再重试


def main():
    parser = argparse.ArgumentParser(description="美股关键经济数据监控系统")
    parser.add_argument(
        "--weekly",
        action="store_true",
        help="仅推送本周数据日历",
    )
    parser.add_argument(
        "--daemon",
        action="store_true",
        help="持续运行模式 (每5分钟检查一次)",
    )
    parser.add_argument(
        "--interval",
        type=int,
        default=300,
        help="守护模式检查间隔 (秒)",
    )
    parser.add_argument(
        "--dashboard",
        action="store_true",
        help="仅打印倒计时面板",
    )

    args = parser.parse_args()
    monitor = USStockMonitor()

    if args.weekly:
        monitor.send_weekly_calendar()
    elif args.daemon:
        monitor.run_daemon(args.interval)
    elif args.dashboard:
        monitor.print_countdown_dashboard()
    else:
        # 默认: 检查一次并推送
        monitor.check_events()


if __name__ == "__main__":
    main()
