# 美股关键经济数据监控系统

监控美股关键经济数据发布时间，倒计时提醒，自动推送市场影响分析到微信。

## 📁 项目结构

```
us-stock-monitor/
├── config/
│   ├── __init__.py
│   ├── settings.py          # 配置文件 (WxPusher Token 等)
│   └── data_calendar.py     # 经济数据日历 (时间规律 + 影响分析)
├── utils/
│   ├── __init__.py
│   └── wxpusher.py          # WxPusher 推送模块
├── logs/                     # 日志目录
├── main.py                   # 主程序
├── requirements.txt          # Python 依赖
├── crontab_config.txt        # 定时任务配置参考
└── README.md                 # 本文件
```

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置 WxPusher

1. 访问 [WxPusher 官网](https://wxpusher.zxhd99.com/)
2. 注册账号
3. 创建应用，获取 **AppToken**
4. 关注你的应用，获取 **UID**
5. 编辑 `config/settings.py`:

```python
WX_PUSHER_APP_TOKEN = "你的AppToken"
WX_PUSHER_UIDS = ["你的UID"]
```

### 3. 测试推送

```bash
python main.py --dashboard    # 查看倒计时面板
python main.py --weekly       # 推送本周日历 (测试推送)
```

### 4. 运行模式

```bash
# 模式一: 单次检查 (适合 crontab 定时调用)
python main.py

# 模式二: 推送本周日历
python main.py --weekly

# 模式三: 持续运行 (守护进程，每5分钟检查)
python main.py --daemon

# 模式四: 自定义检查间隔
python main.py --daemon --interval 60

# 模式五: 仅查看倒计时面板
python main.py --dashboard
```

## 📊 监控的数据

| 类别 | 数据 | 重要程度 | 发布频率 |
|------|------|----------|----------|
| 就业 | 非农就业报告 | 🔴 极度重要 | 每月第一个周五 |
| 就业 | 失业率 | 🟡 重要 | 每月第一个周五 |
| 就业 | 初请失业金人数 | 🟢 一般 | 每周四 |
| 就业 | ADP就业报告 | 🟢 一般 | 每月第一个周三 |
| 通胀 | CPI / 核心CPI | 🔴 极度重要 | 每月中旬 |
| 通胀 | PPI | 🟡 重要 | 每月中旬 |
| 通胀 | PCE | 🔴 极度重要 | 每月末 |
| 美联储 | 利率决议 | 🔴 极度重要 | 每年8次 |
| 美联储 | 会议纪要 | 🟡 重要 | 利率决议后3周 |
| 经济 | GDP | 🔴 极度重要 | 每季度 |
| 经济 | PMI 制造业/服务业 | 🟡 重要 | 每月 |
| 经济 | 零售销售 | 🟡 重要 | 每月 |
| 国际 | 日本央行决议 | 🟡 重要 | 每年8次 |
| 国际 | 欧洲央行决议 | 🟡 重要 | 每6周 |

## ⏰ 推送机制

系统会在以下时间点推送提醒：

- **提前 1 天** (24小时): 数据发布预告 + 可能影响分析
- **提前 1 小时**: 即将发布提醒 + 关注要点
- **提前 15 分钟**: 即将发布最后提醒

每周一早上自动推送 **本周数据日历**。

## 🔧 云服务器部署

### Linux (推荐 Ubuntu/CentOS)

```bash
# 1. 安装 Python
sudo apt install python3 python3-pip

# 2. 上传项目到服务器
scp -r us-stock-monitor/ root@your-server:/opt/

# 3. 安装依赖
cd /opt/us-stock-monitor
pip3 install -r requirements.txt

# 4. 配置定时任务
crontab -e
# 添加:
*/5 * * * * cd /opt/us-stock-monitor && /usr/bin/python3 main.py >> /opt/us-stock-monitor/logs/cron.log 2>&1
0 8 * * 1 cd /opt/us-stock-monitor && /usr/bin/python3 main.py --weekly
```

### 使用 systemd (更可靠)

```bash
sudo nano /etc/systemd/system/us-stock-monitor.service
```

添加内容:
```ini
[Unit]
Description=US Stock Data Monitor
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/opt/us-stock-monitor
ExecStart=/usr/bin/python3 main.py --daemon --interval 300
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

启动:
```bash
sudo systemctl daemon-reload
sudo systemctl start us-stock-monitor
sudo systemctl enable us-stock-monitor
sudo systemctl status us-stock-monitor
```

## 📝 自定义配置

### 修改提醒时间间隔

编辑 `config/settings.py`:

```python
REMIND_INTERVALS = [
    1440,  # 提前1天
    60,    # 提前1小时
    15,    # 提前15分钟
]
```

### 添加新的监控数据

编辑 `config/data_calendar.py`，在 `ECONOMIC_CALENDAR` 中添加:

```python
"new_event_id": {
    "name": "数据名称",
    "name_en": "English Name",
    "importance": "critical",  # critical/high/medium
    "schedule_rule": "first_friday",
    "et_time": "08:30",
    "impact_analysis": {
        "better_than_expected": ["影响1", "影响2"],
        "worse_than_expected": ["影响3", "影响4"],
        "key_point": "核心关注点",
    },
},
```

## 📂 日志查看

```bash
tail -f logs/us_stock_monitor.log
```

## ⚠️ 注意事项

1. 发布时间规则是基于历史规律，实际日期可能有变动
2. 夏令时/冬令时会影响北京时间 (差1小时)
3. 首次使用务必测试推送是否成功
4. FOMC/BOJ等会议日期需要手动更新日历
