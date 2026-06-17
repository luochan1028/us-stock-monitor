"""
美股关键经济数据日历配置
定义每个数据的发布时间规律和可能造成的市场影响
"""

# 重要程度等级
CRITICAL = "critical"   # 极度重要 - 可能引发市场剧烈波动
HIGH = "high"           # 重要 - 可能引发明显波动
MEDIUM = "medium"       # 一般 - 可能引发小幅波动

# 美国大选日历
US_ELECTION_CALENDAR = {
    "presidential_2024": {
        "name": "2024年总统大选",
        "date": "2024-11-05",
        "status": "completed",
        "impact": "特朗普胜选，推行减税+关税政策，市场总体乐观",
    },
    "midterm_2026": {
        "name": "2026年中期选举",
        "date": "2026-11-03",
        "status": "upcoming",
        "impact": "将决定国会控制权，影响后续立法进程",
    },
    "presidential_2028": {
        "name": "2028年总统大选",
        "date": "2028-11-07",
        "status": "future",
        "impact": "下届总统选举",
    },
}

# 经济数据日历
ECONOMIC_CALENDAR = {
    # ==================== 就业数据 ====================
    "non_farm_payrolls": {
        "name": "非农就业报告",
        "name_en": "Non-Farm Payrolls",
        "importance": CRITICAL,
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
        "historical_data": [
            {
                "date": "2025-06-06",
                "actual": "13.9万",
                "expected": "14.5万",
                "previous": "14.4万",
                "market_reaction": "标普跌0.2%，纳斯达克跌0.3% - 就业略弱于预期，但未触发恐慌",
                "next_month_trend": "数据公布后一周市场震荡，等待CPI确认",
            },
            {
                "date": "2025-05-02",
                "actual": "17.7万",
                "expected": "18.0万",
                "previous": "13.3万",
                "market_reaction": "标普微涨0.1%，市场消化略弱数据",
                "next_month_trend": "就业数据持续疲软，6月FOMC转鸽概率上升",
            },
            {
                "date": "2025-04-04",
                "actual": "13.3万",
                "expected": "13.0万",
                "previous": "11.9万",
                "market_reaction": "标普跌0.3%，就业持续放缓引发担忧",
                "next_month_trend": "就业疲软+通胀数据叠加，降息预期升温",
            },
        ],
        "position_advice": {
            "bullish": "非农大幅高于预期时：可适当加仓，关注金融、消费板块",
            "bearish": "非农大幅低于预期时：减仓至6成以下，增加防御性仓位（公用事业、黄金）",
            "neutral": "非农符合预期时：维持当前仓位，关注后续CPI和FOMC指引",
        },
    },
    "unemployment_rate": {
        "name": "失业率",
        "name_en": "Unemployment Rate",
        "importance": HIGH,
        "schedule_rule": "first_friday",
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
        "historical_data": [
            {
                "date": "2025-06-06",
                "actual": "4.2%",
                "expected": "4.1%",
                "previous": "4.1%",
                "market_reaction": "失业率小幅上升，市场反应平淡",
                "next_month_trend": "失业率连续上升，关注是否形成趋势",
            },
            {
                "date": "2025-05-02",
                "actual": "4.1%",
                "expected": "4.0%",
                "previous": "4.0%",
                "market_reaction": "失业率连续两个月上升，市场警惕",
                "next_month_trend": "Sahm Rule触发条件接近（失业率较12个月低点上升0.5%）",
            },
        ],
        "position_advice": {
            "bullish": "失业率下降或持平：维持当前仓位",
            "bearish": "失业率连续上升，接近4.5%：减仓至5成，警惕Sahm Rule触发",
            "neutral": "失业率在4.0%-4.2%区间：正常操作，无需过度调整",
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
        "position_advice": {
            "neutral": "周度数据，对仓位影响有限。连续4周上升超过25万需警惕",
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
        "position_advice": {
            "neutral": "ADP仅作参考，无需因ADP数据大幅调整仓位。等待非农确认",
        },
    },

    # ==================== 通胀数据 ====================
    "cpi": {
        "name": "消费者物价指数 CPI",
        "name_en": "Consumer Price Index",
        "importance": CRITICAL,
        "schedule_rule": "mid_month",
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
        "historical_data": [
            {
                "date": "2025-06-12",
                "actual": "3.4%",
                "expected": "3.3%",
                "previous": "3.4%",
                "market_reaction": "CPI高于预期，标普跌0.4%，纳斯达克跌0.6% - 科技股领跌",
                "next_month_trend": "通胀粘性确认后，市场降息预期从7月推迟至9月",
            },
            {
                "date": "2025-05-15",
                "actual": "3.4%",
                "expected": "3.5%",
                "previous": "3.5%",
                "market_reaction": "CPI略低于预期，标普涨0.5%，市场短暂反弹",
                "next_month_trend": "通胀趋势仍需观察，FOMC保持谨慎",
            },
            {
                "date": "2025-04-10",
                "actual": "3.5%",
                "expected": "3.4%",
                "previous": "3.2%",
                "market_reaction": "CPI大幅高于预期，标普跌1.1%，VIX飙升至18以上",
                "next_month_trend": "通胀反弹确认，市场从降息预期转向加息担忧",
            },
        ],
        "position_advice": {
            "bullish": "CPI回落至3%以下：可加仓至8成以上，成长股受益",
            "bearish": "CPI高于预期且核心CPI持续在3%以上：减仓至5成，增加现金配置",
            "neutral": "CPI符合预期：维持6-7成仓位，关注后续FOMC表态",
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
        "position_advice": {
            "bearish": "核心CPI连续高于3%：减仓，警惕美联储长期高利率",
            "bullish": "核心CPI回落至2.5%以下：可大幅加仓",
            "neutral": "核心CPI在2.5%-3%之间：中性操作",
        },
    },
    "ppi": {
        "name": "生产者物价指数 PPI",
        "name_en": "Producer Price Index",
        "importance": HIGH,
        "schedule_rule": "mid_month",
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
        "position_advice": {
            "neutral": "PPI仅作参考，关键看是否传导至CPI。如PPI连续上升，需警惕后续CPI",
        },
    },
    "pce": {
        "name": "个人消费支出物价指数 PCE",
        "name_en": "Personal Consumption Expenditures",
        "importance": CRITICAL,
        "schedule_rule": "end_of_month",
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
        "historical_data": [
            {
                "date": "2025-05-30",
                "actual": "2.7%",
                "expected": "2.6%",
                "previous": "2.7%",
                "market_reaction": "PCE略高于预期，标普跌0.3%，市场消化后反弹",
                "next_month_trend": "PCE仍高于2%目标，FOMC维持高利率",
            },
            {
                "date": "2025-04-30",
                "actual": "2.7%",
                "expected": "2.8%",
                "previous": "2.8%",
                "market_reaction": "PCE低于预期，标普涨0.6%，降息预期升温",
                "next_month_trend": "通胀趋势改善，但距离2%目标仍有距离",
            },
        ],
        "position_advice": {
            "bullish": "核心PCE降至2.5%以下：大幅加仓，降息周期确认",
            "bearish": "核心PCE高于3%：减仓至4-5成，防御为主",
            "neutral": "核心PCE在2.5%-3%：维持6成仓位，等待方向明确",
        },
    },

    # ==================== 美联储政策 ====================
    "fomc_rate_decision": {
        "name": "美联储利率决议",
        "name_en": "FOMC Rate Decision",
        "importance": CRITICAL,
        "schedule_rule": "fomc_meeting",
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
        "historical_data": [
            {
                "date": "2025-06-18",
                "actual": "维持利率不变 (4.25-4.50%)",
                "expected": "维持不变",
                "previous": "维持不变",
                "market_reaction": "符合预期，鲍威尔表态偏鹰，标普盘中跌0.5%后收回",
                "next_month_trend": "点阵图显示年内最多降息1次，7月概率低",
            },
            {
                "date": "2025-05-07",
                "actual": "维持利率不变",
                "expected": "维持不变",
                "previous": "维持不变",
                "market_reaction": "鲍威尔承认经济不确定性增加，标普涨0.4%",
                "next_month_trend": "市场开始定价7月降息可能性",
            },
            {
                "date": "2025-03-19",
                "actual": "维持利率不变",
                "expected": "维持不变",
                "previous": "维持不变",
                "market_reaction": "点阵图暗示年内2次降息，标普涨0.8%",
                "next_month_trend": "降息预期推动市场反弹，但需数据确认",
            },
        ],
        "position_advice": {
            "bullish": "FOMC降息或释放明确鸽派信号：加仓至8成以上，全面做多",
            "bearish": "FOMC加息或释放鹰派信号：减仓至4成以下，增加现金和短债",
            "neutral": "维持利率不变：根据前瞻指引调整仓位，中性偏谨慎",
        },
    },
    "fomc_minutes": {
        "name": "美联储会议纪要",
        "name_en": "FOMC Meeting Minutes",
        "importance": HIGH,
        "schedule_rule": "fomc_minutes",
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
        "position_advice": {
            "neutral": "纪要通常不改变市场方向，但可能加剧波动。无需大幅调整仓位",
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
        "schedule_rule": "quarterly",
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
        "historical_data": [
            {
                "date": "2025-06-26",
                "actual": "1.3%（初值）",
                "expected": "1.5%",
                "previous": "2.3%（修正值）",
                "market_reaction": "GDP低于预期，经济放缓信号明确，标普跌0.5%",
                "next_month_trend": "Q2增长放缓，市场担忧衰退风险上升",
            },
            {
                "date": "2025-03-27",
                "actual": "2.3%（修正值）",
                "expected": "2.2%",
                "previous": "2.0%（初值）",
                "market_reaction": "GDP修正值上调，标普微涨",
                "next_month_trend": "经济韧性确认，但Q1高增长难以持续",
            },
        ],
        "position_advice": {
            "bullish": "GDP增速高于2%且结构健康：可加仓周期股",
            "bearish": "GDP低于1%或连续两个季度负增长：大幅减仓至3-4成，防御为主",
            "neutral": "GDP在1.5%-2%之间：维持中性仓位，关注消费和就业数据",
        },
    },
    "pmi_manufacturing": {
        "name": "制造业PMI",
        "name_en": "Manufacturing PMI",
        "importance": HIGH,
        "schedule_rule": "beginning_of_month",
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
        "position_advice": {
            "neutral": "PMI仅作参考，制造业占美国经济比重较小。低于45需警惕",
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
        "position_advice": {
            "neutral": "服务业PMI低于50需高度警惕，占经济70%的部门萎缩是衰退信号",
        },
    },
    "retail_sales": {
        "name": "零售销售数据",
        "name_en": "Retail Sales",
        "importance": HIGH,
        "schedule_rule": "mid_month",
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
        "historical_data": [
            {
                "date": "2025-06-17",
                "actual": "0.1%",
                "expected": "0.3%",
                "previous": "0.2%",
                "market_reaction": "零售销售低于预期，消费疲软信号，标普跌0.3%",
                "next_month_trend": "消费放缓+GDP放缓叠加，衰退概率上升",
            },
        ],
        "position_advice": {
            "bullish": "零售销售连续高于0.3%：可加仓消费股",
            "bearish": "零售销售连续为负：减仓，警惕消费衰退",
            "neutral": "零售销售在0-0.3%之间：维持当前仓位",
        },
    },
    "consumer_confidence": {
        "name": "消费者信心指数",
        "name_en": "Consumer Confidence Index",
        "importance": MEDIUM,
        "schedule_rule": "last_tuesday",
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
        "schedule_rule": "boj_meeting",
        "et_time": "varies",
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
        "historical_data": [
            {
                "date": "2024-08-05",
                "actual": "加息至0.25%",
                "expected": "维持不变",
                "previous": "0.1%",
                "market_reaction": "日元套利交易大规模平仓，全球股市闪崩，道指跌2.5%，纳斯达克跌3.4%",
                "next_month_trend": "BOJ后续表态偏鸽，市场逐步恢复，但波动率显著上升",
            },
            {
                "date": "2025-03-19",
                "actual": "维持利率不变",
                "expected": "维持不变",
                "previous": "0.25%",
                "market_reaction": "符合预期，市场反应平淡",
                "next_month_trend": "BOJ维持观望，日元持续走弱",
            },
        ],
        "position_advice": {
            "bullish": "BOJ维持宽松政策：无特殊影响",
            "bearish": "BOJ意外加息或鹰派表态：立即减仓至3成以下，警惕流动性冲击",
            "neutral": "BOJ维持利率不变：正常操作，关注日本通胀数据",
        },
    },
    "ecb_rate_decision": {
        "name": "欧洲央行利率决议",
        "name_en": "ECB Rate Decision",
        "importance": HIGH,
        "schedule_rule": "ecb_meeting",
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
        "position_advice": {
            "bearish": "10Y-2Y倒挂超过50bp持续3个月以上：大幅减仓，衰退概率极高",
            "neutral": "10Y-2Y小幅倒挂或转正：正常操作",
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
        "position_advice": {
            "bullish": "VIX低于15：市场过度乐观，可适当持有反向期权对冲",
            "bearish": "VIX超过30：市场恐慌，不要盲目抄底，等待VIX回落至25以下",
            "neutral": "VIX在15-25之间：正常操作",
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
        for m in range(month, 13):
            for d in range(1, 8):
                if datetime.date(year, m, d).weekday() == 4:
                    candidates.append(datetime.date(year, m, d))
                    break
        for m in range(1, month):
            for d in range(1, 8):
                if datetime.date(year + 1, m, d).weekday() == 4:
                    candidates.append(datetime.date(year + 1, m, d))
                    break

    elif schedule_rule == "first_wednesday":
        for m in range(month, 13):
            for d in range(1, 8):
                if datetime.date(year, m, d).weekday() == 2:
                    candidates.append(datetime.date(year, m, d))
                    break

    elif schedule_rule == "every_thursday":
        for i in range(14):
            d = from_datetime.date() + datetime.timedelta(days=i)
            if d.weekday() == 3:
                candidates.append(d)

    elif schedule_rule == "mid_month":
        for m in range(month, 13):
            for d in [13, 14, 12, 15]:
                try:
                    candidates.append(datetime.date(year, m, d))
                except ValueError:
                    pass
                break

    elif schedule_rule == "end_of_month":
        for m in range(month, 13):
            last_day = calendar.monthrange(year, m)[1]
            candidates.append(datetime.date(year, m, last_day))

    elif schedule_rule == "beginning_of_month":
        for m in range(month, 13):
            candidates.append(datetime.date(year, m, 1))

    elif schedule_rule == "last_tuesday":
        for m in range(month, 13):
            last_day = calendar.monthrange(year, m)[1]
            for d in range(last_day, last_day - 7, -1):
                if datetime.date(year, m, d).weekday() == 1:
                    candidates.append(datetime.date(year, m, d))
                    break

    elif schedule_rule == "quarterly":
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

    for date in candidates:
        et_date = et.localize(
            datetime.datetime(date.year, date.month, date.day, hour, minute)
        )
        bj_datetime = et_date.astimezone(bj)
        if bj_datetime > from_datetime:
            return bj_datetime

    return None
