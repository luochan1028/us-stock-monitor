"""
美股关键经济数据日历配置
定义每个数据的发布时间规律和可能造成的市场影响
"""

# 重要程度等级
CRITICAL = "critical"   # 极度重要 - 可能引发市场剧烈波动
HIGH = "high"           # 重要 - 可能引发明显波动
MEDIUM = "medium"       # 一般 - 可能引发小幅波动

# 经济数据日历
ECONOMIC_CALENDAR = {
    # ==================== 就业数据 ====================
    "non_farm_payrolls": {
        "name": "非农就业报告",
        "name_en": "Non-Farm Payrolls",
        "importance": CRITICAL,
        # 每月第一个周五 美东时间 8:30 (北京冬季时间 21:30, 夏季时间 20:30)
        "schedule_rule": "first_friday",
        "et_time": "08:30",
        "impact_analysis": {
            "better_than_expected": [
                "美股通常上涨 - 经济强劲信号",
                "美元走强",
                "可能增加美联储加息预期",
                "美债收益率上升",
                "科技成长股可能承压（利率敏感）",
            ],
            "worse_than_expected": [
                "美股可能下跌 - 经济衰退担忧",
                "美元走弱",
                "可能增加美联储降息预期",
                "美债收益率下降",
                "防御性板块（公用事业、医疗）相对抗跌",
            ],
            "key_point": "关注失业率、劳动参与率、平均时薪增速",
        },
    },
    "unemployment_rate": {
        "name": "失业率",
        "name_en": "Unemployment Rate",
        "importance": HIGH,
        "schedule_rule": "first_friday",  # 与非农同时发布
        "et_time": "08:30",
        "impact_analysis": {
            "better_than_expected": [
                "就业市场健康 - 利好消费股",
                "可能推升通胀预期",
                "美联储加息概率上升",
            ],
            "worse_than_expected": [
                "就业市场疲软 - 利空周期股",
                "降息预期升温",
                "利好债券",
            ],
            "key_point": "4%以下是健康水平，超过5%需警惕",
        },
    },
    "jobless_claims": {
        "name": "初请失业金人数",
        "name_en": "Initial Jobless Claims",
        "importance": MEDIUM,
        "schedule_rule": "every_thursday",
        "et_time": "08:30",
        "impact_analysis": {
            "better_than_expected": [
                "就业市场稳定信号",
                "对市场影响较小但持续上升需警惕",
            ],
            "worse_than_expected": [
                "如果连续上升，可能预示就业恶化",
                "单独一周数据影响有限",
            ],
            "key_point": "关注四周移动平均值，22万以下为健康",
        },
    },
    "adp_employment": {
        "name": "ADP就业报告",
        "name_en": "ADP National Employment Report",
        "importance": MEDIUM,
        "schedule_rule": "first_wednesday",
        "et_time": "08:15",
        "impact_analysis": {
            "better_than_expected": [
                "非农先行指标 - 利好市场预期",
                "如果与非农背离，需分析原因",
            ],
            "worse_than_expected": [
                "可能预示非农也不佳",
                "引发就业市场担忧",
            ],
            "key_point": "非农前两天发布，是重要前瞻指标",
        },
    },

    # ==================== 通胀数据 ====================
    "cpi": {
        "name": "消费者物价指数 CPI",
        "name_en": "Consumer Price Index",
        "importance": CRITICAL,
        "schedule_rule": "mid_month",  # 每月12-15日左右
        "et_time": "08:30",
        "impact_analysis": {
            "better_than_expected": [
                "通胀高于预期 - 美联储可能加快加息",
                "美股可能大跌（尤其科技股）",
                "美元走强",
                "美债收益率飙升",
                "黄金可能承压",
            ],
            "worse_than_expected": [
                "通胀回落 - 市场欢呼",
                "美股通常大涨",
                "降息预期升温",
                "债券价格上涨",
            ],
            "key_point": "核心CPI（剔除食品能源）更受关注，美联储目标2%",
        },
    },
    "core_cpi": {
        "name": "核心CPI",
        "name_en": "Core CPI",
        "importance": CRITICAL,
        "schedule_rule": "mid_month",
        "et_time": "08:30",
        "impact_analysis": {
            "better_than_expected": [
                "通胀粘性信号 - 利空市场",
                "美联储维持鹰派立场概率增加",
            ],
            "worse_than_expected": [
                "通胀降温确认 - 利好市场",
                "增强软着陆信心",
            ],
            "key_point": "美联储最看重的通胀指标之一",
        },
    },
    "ppi": {
        "name": "生产者物价指数 PPI",
        "name_en": "Producer Price Index",
        "importance": HIGH,
        "schedule_rule": "mid_month",  # CPI后一天左右
        "et_time": "08:30",
        "impact_analysis": {
            "better_than_expected": [
                "上游通胀压力 - 可能传导至CPI",
                "企业利润率可能承压",
            ],
            "worse_than_expected": [
                "通胀压力缓解",
                "企业成本下降",
            ],
            "key_point": "领先CPI，是通胀先行指标",
        },
    },
    "pce": {
        "name": "个人消费支出物价指数 PCE",
        "name_en": "Personal Consumption Expenditures",
        "importance": CRITICAL,
        "schedule_rule": "end_of_month",  # 每月最后一天左右
        "et_time": "08:30",
        "impact_analysis": {
            "better_than_expected": [
                "美联储最看重的通胀指标超标",
                "可能引发市场剧烈反应",
                "加息预期大幅升温",
            ],
            "worse_than_expected": [
                "通胀受控确认",
                "市场大涨概率高",
            ],
            "key_point": "美联储货币政策最核心的参考指标",
        },
    },

    # ==================== 美联储政策 ====================
    "fomc_rate_decision": {
        "name": "美联储利率决议",
        "name_en": "FOMC Rate Decision",
        "importance": CRITICAL,
        "schedule_rule": "fomc_meeting",  # 每年8次，约每6周一次
        "et_time": "14:00",
        "impact_analysis": {
            "better_than_expected": [
                "加息 - 美股可能大跌",
                "成长股、科技股首当其冲",
                "银行股可能受益（利差扩大）",
                "美元走强",
                "新兴市场承压",
            ],
            "worse_than_expected": [
                "降息 - 美股通常大涨",
                "流动性增加利好所有资产",
                "美元走弱",
                "黄金、加密货币等受益",
            ],
            "key_point": "关注点阵图、鲍威尔新闻发布会（14:30）、措辞变化",
        },
    },
    "fomc_minutes": {
        "name": "美联储会议纪要",
        "name_en": "FOMC Meeting Minutes",
        "importance": HIGH,
        "schedule_rule": "fomc_minutes",  # 利率决议后3周
        "et_time": "14:00",
        "impact_analysis": {
            "better_than_expected": [
                "鹰派纪要 - 市场承压",
                "如果暗示更多加息，利空",
            ],
            "worse_than_expected": [
                "鸽派纪要 - 市场反弹",
                "如果暗示加息接近尾声，利好",
            ],
            "key_point": "揭示委员分歧和下一步政策倾向",
        },
    },
    "fed_speech": {
        "name": "美联储官员讲话",
        "name_en": "Fed Speaker",
        "importance": MEDIUM,
        "schedule_rule": "varies",
        "et_time": "varies",
        "impact_analysis": {
            "key_point": "重点关注鲍威尔、副主席、票委讲话",
        },
    },

    # ==================== 经济增长指标 ====================
    "gdp": {
        "name": "国内生产总值 GDP",
        "name_en": "Gross Domestic Product",
        "importance": CRITICAL,
        "schedule_rule": "quarterly",  # 每季度末次月发布
        "et_time": "08:30",
        "impact_analysis": {
            "better_than_expected": [
                "经济强劲 - 利好周期股",
                "金融、工业、材料板块受益",
                "可能增加加息预期",
            ],
            "worse_than_expected": [
                "经济放缓 - 利空周期股",
                "连续两个季度负增长 = 技术性衰退",
                "降息预期升温",
                "防御性板块相对抗跌",
            ],
            "key_point": "关注初值、修正值、终值三版数据",
        },
    },
    "pmi_manufacturing": {
        "name": "制造业PMI",
        "name_en": "Manufacturing PMI",
        "importance": HIGH,
        "schedule_rule": "beginning_of_month",  # 每月1日
        "et_time": "09:45",
        "impact_analysis": {
            "better_than_expected": [
                "制造业扩张信号",
                "利好工业、材料板块",
            ],
            "worse_than_expected": [
                "制造业萎缩（低于50）",
                "经济衰退预警",
            ],
            "key_point": "50是荣枯线，高于50表示扩张",
        },
    },
    "pmi_services": {
        "name": "服务业PMI",
        "name_en": "Services PMI",
        "importance": HIGH,
        "schedule_rule": "mid_month",
        "et_time": "09:45",
        "impact_analysis": {
            "key_point": "美国服务业占经济70%以上，比制造业PMI更重要",
        },
    },
    "retail_sales": {
        "name": "零售销售数据",
        "name_en": "Retail Sales",
        "importance": HIGH,
        "schedule_rule": "mid_month",  # 每月13-15日左右
        "et_time": "08:30",
        "impact_analysis": {
            "better_than_expected": [
                "消费强劲 - 利好消费股",
                "占美国GDP 70%的消费确认健康",
                "可能推升通胀预期",
            ],
            "worse_than_expected": [
                "消费疲软 - 经济衰退信号",
                "消费股承压",
            ],
            "key_point": "消费是美国经济的核心引擎",
        },
    },
    "consumer_confidence": {
        "name": "消费者信心指数",
        "name_en": "Consumer Confidence Index",
        "importance": MEDIUM,
        "schedule_rule": "last_tuesday",  # 每月最后一个周二
        "et_time": "10:00",
        "impact_analysis": {
            "key_point": "领先指标，预示未来消费趋势",
        },
    },

    # ==================== 国际因素 ====================
    "boj_rate_decision": {
        "name": "日本央行利率决议",
        "name_en": "Bank of Japan Rate Decision",
        "importance": HIGH,
        "schedule_rule": "boj_meeting",  # 每年8次
        "et_time": "varies",  # 东京时间
        "impact_analysis": {
            "better_than_expected": [
                "加息 - 日元套利交易 unwind",
                "全球流动性收紧",
                "美股可能大跌（如2024年8月5日闪崩）",
                "日股首当其冲",
            ],
            "worse_than_expected": [
                "维持负利率 - 流动性持续宽松",
                "对市场影响中性偏正面",
            ],
            "key_point": "日本是全球最大债权国，政策变动影响深远",
        },
    },
    "ecb_rate_decision": {
        "name": "欧洲央行利率决议",
        "name_en": "ECB Rate Decision",
        "importance": HIGH,
        "schedule_rule": "ecb_meeting",  # 每6周一次
        "et_time": "varies",
        "impact_analysis": {
            "key_point": "欧元区政策外溢影响美股",
        },
    },

    # ==================== 其他重要数据 ====================
    "treasury_auction": {
        "name": "美国国债拍卖",
        "name_en": "Treasury Auction",
        "importance": MEDIUM,
        "schedule_rule": "weekly",
        "et_time": "11:00",
        "impact_analysis": {
            "key_point": "投标倍数影响美债收益率，间接影响股市估值",
        },
    },
    "yield_curve_10y2y": {
        "name": "10年/2年美债收益率利差",
        "name_en": "10Y-2Y Treasury Yield Spread",
        "importance": HIGH,
        "schedule_rule": "continuous",
        "et_time": "market_hours",
        "impact_analysis": {
            "key_point": "收益率曲线倒挂是经济衰退最准确的领先指标",
        },
    },
    "vix": {
        "name": "VIX恐慌指数",
        "name_en": "CBOE Volatility Index",
        "importance": MEDIUM,
        "schedule_rule": "continuous",
        "et_time": "market_hours",
        "impact_analysis": {
            "key_point": "超过30表示市场恐慌，低于15表示过度乐观",
        },
    },
}


def get_this_week_events():
    """获取本周即将发布的数据事件"""
    import datetime
    import pytz

    now = datetime.datetime.now(pytz.timezone("Asia/Shanghai"))
    current_month = now.month
    current_year = now.year

    events = []

    for event_id, event_config in ECONOMIC_CALENDAR.items():
        event = {
            "id": event_id,
            "config": event_config,
            "datetime": get_next_event_datetime(event_id, now),
        }
        if event["datetime"]:
            events.append(event)

    # 按时间排序
    events.sort(key=lambda x: x["datetime"])
    return events


def get_next_event_datetime(event_id, from_datetime):
    """计算某个事件的下次发生时间（北京时间）"""
    import datetime
    import pytz

    et = pytz.timezone("US/Eastern")
    bj = pytz.timezone("Asia/Shanghai")

    schedule_rule = ECONOMIC_CALENDAR[event_id]["schedule_rule"]
    et_time_str = ECONOMIC_CALENDAR[event_id].get("et_time", "08:30")

    if schedule_rule in ["varies", "continuous", "fomc_meeting", "fomc_minutes", 
                         "boj_meeting", "ecb_meeting"]:
        # 这些事件需要特殊处理，返回 None 表示需要手动指定
        return None

    return _calculate_next_date(schedule_rule, et_time_str, from_datetime, et, bj)


def _calculate_next_date(schedule_rule, et_time_str, from_datetime, et, bj):
    """根据调度规则计算下次发布时间"""
    import datetime
    import calendar

    hour, minute = map(int, et_time_str.split(":"))
    year = from_datetime.year
    month = from_datetime.month
    day = from_datetime.day

    candidates = []

    if schedule_rule == "first_friday":
        # 每月第一个周五
        for m in range(month, 13):
            for d in range(1, 8):
                if datetime.date(year, m, d).weekday() == 4:  # Friday
                    candidates.append(datetime.date(year, m, d))
                    break
        for m in range(1, month):
            for d in range(1, 8):
                if datetime.date(year + 1, m, d).weekday() == 4:
                    candidates.append(datetime.date(year + 1, m, d))
                    break

    elif schedule_rule == "first_wednesday":
        # 每月第一个周三
        for m in range(month, 13):
            for d in range(1, 8):
                if datetime.date(year, m, d).weekday() == 2:  # Wednesday
                    candidates.append(datetime.date(year, m, d))
                    break

    elif schedule_rule == "every_thursday":
        # 每周四
        for i in range(14):
            d = from_datetime.date() + datetime.timedelta(days=i)
            if d.weekday() == 3:  # Thursday
                candidates.append(d)

    elif schedule_rule == "mid_month":
        # 每月12-15日
        for m in range(month, 13):
            for d in [13, 14, 12, 15]:
                try:
                    candidates.append(datetime.date(year, m, d))
                except ValueError:
                    pass
                break

    elif schedule_rule == "end_of_month":
        # 每月最后一天
        for m in range(month, 13):
            last_day = calendar.monthrange(year, m)[1]
            candidates.append(datetime.date(year, m, last_day))

    elif schedule_rule == "beginning_of_month":
        # 每月1日
        for m in range(month, 13):
            candidates.append(datetime.date(year, m, 1))

    elif schedule_rule == "last_tuesday":
        # 每月最后一个周二
        for m in range(month, 13):
            last_day = calendar.monthrange(year, m)[1]
            for d in range(last_day, last_day - 7, -1):
                if datetime.date(year, m, d).weekday() == 1:  # Tuesday
                    candidates.append(datetime.date(year, m, d))
                    break

    elif schedule_rule == "quarterly":
        # 每季度（1月、4月、7月、10月的最后月次月）
        quarterly_months = [1, 4, 7, 10]
        for qm in quarterly_months:
            if qm >= month:
                # GDP通常在季度结束后第一个月发布
                pass
        # 简化处理：每3个月
        for i in range(4):
            m = month + i * 3
            if m > 12:
                break
            last_day = calendar.monthrange(year, m)[1]
            candidates.append(datetime.date(year, m, last_day))

    elif schedule_rule == "weekly":
        for i in range(14):
            d = from_datetime.date() + datetime.timedelta(days=i)
            candidates.append(d)

    # 筛选未来的日期
    for date in candidates:
        et_date = et.localize(
            datetime.datetime(date.year, date.month, date.day, hour, minute)
        )
        bj_datetime = et_date.astimezone(bj)
        if bj_datetime > from_datetime:
            return bj_datetime

    return None
