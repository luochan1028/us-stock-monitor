"""
WxPusher 微信推送模块
文档: https://wxpusher.zjiecode.com/docs/
"""

import requests
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.settings import WX_PUSHER_APP_TOKEN, WX_PUSHER_UIDS


class WxPusher:
    """WxPusher 推送客户端"""

    API_URL = "https://wxpusher.zjiecode.com/api/send/message"

    def __init__(self, app_token=None, uids=None):
        self.app_token = app_token or WX_PUSHER_APP_TOKEN
        self.uids = uids or WX_PUSHER_UIDS

    def send_message(self, content, title="美股数据监控提醒", summary=None):
        """发送消息到微信"""
        if self.app_token == "your_app_token_here":
            print("[WxPusher] 请先配置 WX_PUSHER_APP_TOKEN")
            return False

        payload = {
            "appToken": self.app_token,
            "content": content,
            "summary": summary or title,
            "contentType": 3,
            "uids": self.uids,
        }

        try:
            response = requests.post(
                self.API_URL,
                json=payload,
                timeout=15,
            )
            result = response.json()

            if result.get("code") == 1000:
                print(f"[WxPusher] 推送成功: {title}")
                return True
            else:
                print(f"[WxPusher] 推送失败: {result}")
                return False

        except Exception as e:
            print(f"[WxPusher] 推送异常: {e}")
            return False

    def send_weekly_calendar(self, events):
        """发送每周数据日历 - 包含历史对比和仓位建议"""
        importance_emoji = {
            "critical": "🔴",
            "high": "🟡",
            "medium": "🟢",
        }

        content = "## 📊 本周美股关键数据日历\n\n"

        if not events:
            content += "本周无重要数据发布。"
        else:
            for event in events:
                dt = event["datetime"]
                config = event["config"]
                imp = config["importance"]
                emoji = importance_emoji.get(imp, "⚪")

                content += f"### {emoji} {config['name']}\n"
                content += f"- **发布时间**: {dt.strftime('%Y-%m-%d %H:%M')} (北京时间)\n"
                content += f"- **重要程度**: {imp.upper()}\n"

                if "impact_analysis" in config:
                    impact = config["impact_analysis"]
                    if "key_point" in impact:
                        content += f"- **核心关注**: {impact['key_point']}\n"

                # 历史数据
                if "historical_data" in config:
                    hist = config["historical_data"][0]  # 最近一次
                    content += f"\n**上次数据** ({hist['date']}):\n"
                    content += f"- 实际: {hist['actual']} | 预期: {hist['expected']}\n"
                    content += f"- **市场反应**: {hist['market_reaction']}\n"
                    content += f"- **后续走势**: {hist['next_month_trend']}\n"

                # 仓位建议
                if "position_advice" in config:
                    content += "\n**仓位建议**:\n"
                    advice = config["position_advice"]
                    if "bullish" in advice:
                        content += f"- 看涨: {advice['bullish']}\n"
                    if "bearish" in advice:
                        content += f"- 看跌: {advice['bearish']}\n"
                    if "neutral" in advice:
                        content += f"- 中性: {advice['neutral']}\n"

                content += "\n---\n\n"

        # 美国大选信息
        from config.data_calendar import US_ELECTION_CALENDAR
        content += "## 🗳️ 美国大选日历\n\n"
        for eid, edata in US_ELECTION_CALENDAR.items():
            status_emoji = {
                "completed": "✅",
                "upcoming": "⏳",
                "future": "🔮",
            }
            se = status_emoji.get(edata["status"], "📌")
            content += f"- {se} **{edata['name']}** ({edata['date']}): {edata['impact']}\n"

        content += "\n---\n\n"
        content += "> 📌 **说明**:\n"
        content += "> - 系统将在数据发布前 **1天、1小时、15分钟** 分别推送提醒\n"
        content += "> - 🔴 极度重要 | 🟡 重要 | 🟢 一般\n"
        content += "> - 仓位建议仅供参考，不构成投资建议\n"

        return self.send_message(
            content=content,
            title="本周美股数据日历",
            summary=f"本周共有 {len(events)} 个重要数据发布",
        )

    def send_countdown_reminder(self, event, minutes_remaining):
        """发送倒计时提醒 - 包含历史对比和仓位建议"""
        config = event["config"]
        dt = event["datetime"]

        importance_emoji = {
            "critical": "🔴",
            "high": "🟡",
            "medium": "🟢",
        }
        emoji = importance_emoji.get(config["importance"], "⚪")

        if minutes_remaining >= 1440:
            time_label = "**明天**"
        elif minutes_remaining >= 60:
            time_label = "**1小时后**"
        elif minutes_remaining >= 15:
            time_label = "**15分钟后**"
        else:
            time_label = "**即将发布**"

        content = f"## {emoji} 数据发布提醒\n\n"
        content += f"### 📢 {config['name']} ({config['name_en']})\n\n"
        content += f"⏰ 发布时间: {time_label}\n"
        content += f"📅 北京时间: {dt.strftime('%Y-%m-%d %H:%M')}\n"
        content += f"⚡ 重要程度: {config['importance'].upper()}\n\n"

        # 市场影响
        if "impact_analysis" in config:
            impact = config["impact_analysis"]
            content += "---\n\n"
            content += "### 📈 可能的市场影响\n\n"

            if "key_point" in impact:
                content += f"**核心关注**: {impact['key_point']}\n\n"

            if "better_than_expected" in impact:
                content += "**好于预期**:\n"
                for point in impact["better_than_expected"]:
                    content += f"- {point}\n"
                content += "\n"

            if "worse_than_expected" in impact:
                content += "**差于预期**:\n"
                for point in impact["worse_than_expected"]:
                    content += f"- {point}\n"
                content += "\n"

        # 历史数据对比
        if "historical_data" in config:
            hist = config["historical_data"][0]
            content += "---\n\n"
            content += "### 📊 上次数据对比\n\n"
            content += f"**{hist['date']}** 数据:\n"
            content += f"- 实际值: **{hist['actual']}** | 预期: {hist['expected']} | 前值: {hist['previous']}\n"
            content += f"- **市场反应**: {hist['market_reaction']}\n"
            content += f"- **后续走势**: {hist['next_month_trend']}\n"

        # 仓位建议
        if "position_advice" in config:
            content += "\n---\n\n"
            content += "### 💰 仓位操作建议\n\n"
            advice = config["position_advice"]
            if "bullish" in advice:
                content += f"📈 **好于预期**: {advice['bullish']}\n"
            if "bearish" in advice:
                content += f"📉 **差于预期**: {advice['bearish']}\n"
            if "neutral" in advice:
                content += f"⚖️ **符合预期**: {advice['neutral']}\n"

        if minutes_remaining <= 15:
            title = f"⚡ 即将发布: {config['name']}"
        elif minutes_remaining <= 60:
            title = f"⏰ 1小时后发布: {config['name']}"
        else:
            title = f"📢 明日预告: {config['name']}"

        return self.send_message(
            content=content,
            title=title,
            summary=f"{config['name']} 将在 {minutes_remaining} 分钟后发布",
        )


if __name__ == "__main__":
    pusher = WxPusher()
    pusher.send_message(
        content="## 测试消息\n\n美股数据监控系统已启动！",
        title="系统测试",
    )
