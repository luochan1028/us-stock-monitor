"""
美股关键经济数据监控系统 - 配置文件
"""
import os

# WxPusher 配置
# 获取方式: https://wxpusher.zxhd99.com/ 注册后获取
# 方式1: 直接填写 (不要提交到 git)
# 方式2: 使用环境变量 WX_PUSHER_APP_TOKEN 和 WX_PUSHER_UIDS
WX_PUSHER_APP_TOKEN = os.environ.get("WX_PUSHER_APP_TOKEN", "your_app_token_here")
WX_PUSHER_UIDS = os.environ.get(
    "WX_PUSHER_UIDS", "your_uid_here"
).split(",")

# 时区配置
TIMEZONE = "Asia/Shanghai"  # 北京时间
ET_TIMEZONE = "US/Eastern"  # 美东时间

# 推送提醒时间点（分钟）
REMIND_INTERVALS = [
    1440,  # 提前1天 (24小时)
    60,    # 提前1小时
    15,    # 提前15分钟
]

# 日志配置
LOG_DIR = "logs"
LOG_FILE = "us_stock_monitor.log"

# 数据缓存配置（避免重复请求）
CACHE_DIR = "cache"
