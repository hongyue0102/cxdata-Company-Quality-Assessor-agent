#!/usr/bin/env python3
"""
公司质地打分 - 结构化分析与评分计算
读取 fetch_data.py 拉取的 JSON 数据，按七维评分框架计算各模块得分，输出分析结果 JSON。

使用方式：
    python analyze_data.py [股票代码]
    示例: python analyze_data.py 300475
"""

import json
import sys
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"


def safe_float(val, default=0.0):
    if val in (None, "", "NaN"):
        return default
    try:
        return float(val)
    except (ValueError, TypeError):
        return default


def safe_int(val, default=0):
    return int(safe_float(val, default))


def load(name: str) -> list:
    with open(DATA_DIR / name, encoding="utf-8") as f:
        return json.load(f)


def load_meta() -> dict:
    data = load("meta.json")
    return data[0] if data else {}


def score_band(value: float, bands: list) -> int:
    """根据分段打分。bands = [(阈值, 分数), ...], 从高到低。"""
    for threshold, score in bands:
        if value >= threshold:
            return score
    return bands[-1][1] if bands else 0


def get_latest_period(data: list, prefer_annual: bool = True) -> dict:
    """从数据列表中取最新报告期。优先年报，回退到最新季报。"""
    if not data:
        return {}
    # 按 END_DATE 排序
    sorted_data = sorted(data, key=lambda x: str(x.get("END_DATE", "")), reverse=True)
    if prefer_annual:
        annual = [r for r in sorted_data if "12-31" in str(r.get("END_DATE", ""))]
        if annual:
            return annual[0]
    return sorted_data[0]


def get_two_periods(data: list) -> tuple:
    """取最新两个报告期数据（用于同比计算）。"""
    if not data:
        return {}, {}
    sorted_data = sorted(data, key=lambda x: str(x.get("END_DATE", "")), reverse=True)
    if len(sorted_data) >= 2:
        return sorted_data[0], sorted_data[1]
    elif len(sorted_data) == 1:
        return sorted_data[0], {}
    return {}, {}


# ========================================
# 模块1：商业模式分析（满分20分）
# ========================================
def analyze_business_model() -> dict:
    """分析商业模式清晰度、收入结构、产品集中度。"""
    breakdown = load("main_business_breakdown.json")
    company_info = load("company_info.json")
    profile = load("company_profile.json")

    info = company_info[0] if company_info else {}
    scope = profile[0].get("COM_PRO", "") if profile else ""
    main_bus = profile[0].get("MAIN_BUS", "") if profile else ""

    # 取最新年报的收入拆分
    latest_date = ""
    latest_items = []
    for r in breakdown:
        ed = str(r.get("END_DATE", ""))
        if "12-31" in ed and ed > latest_date:
            latest_date = ed
            latest_items = []
        if ed == latest_date:
            latest_items.append(r)

    # 按行业/产品/地区分类
    by_industry = [r for r in latest_items if r.get("PROJ_CLASS") == "按行业"]
    by_product = [r for r in latest_items if r.get("PROJ_CLASS") == "按产品"]
    by_region = [r for r in latest_items if r.get("PROJ_CLASS") == "按地区"]

    total_revenue = sum(safe_float(r.get("MAIN_BUSI_INCO")) for r in by_industry)
    top1_revenue = safe_float(by_industry[0].get("MAIN_BUSI_INCO")) if by_industry else 0
    top1_ratio = top1_revenue / total_revenue * 100 if total_revenue > 0 else 0

    # 毛利率（按行业加权）
    gross_margins = []
    for r in by_industry:
        gm = safe_float(r.get("GROSS_MARG"))
        rev = safe_float(r.get("MAIN_BUSI_INCO"))
        if gm and rev > 0:
            gross_margins.append({"name": r.get("PRO_NAME_NEW", ""), "margin": gm, "revenue": rev})

    avg_margin = sum(g["margin"] * g["revenue"] for g in gross_margins) / total_revenue if total_revenue > 0 and gross_margins else 0

    # 【新增】按产品维度收入拆分（关键：海普存储等自研品牌）
    product_breakdown = []
    for r in by_product:
        rev = safe_float(r.get("MAIN_BUSI_INCO"))
        gm = safe_float(r.get("GROSS_MARG"))
        product_breakdown.append({
            "name": r.get("PRO_NAME_NEW", ""),
            "revenue_yi": round(rev / 1e8, 2),
            "margin": round(gm * 100, 2) if gm else None,
            "ratio": round(rev / total_revenue * 100, 2) if total_revenue > 0 else 0,
        })
    product_breakdown.sort(key=lambda x: x["revenue_yi"], reverse=True)

    # 找出核心产品（非分销/贸易类）
    core_products = [p for p in product_breakdown if p["revenue_yi"] > 0 and "分销" not in p["name"] and "贸易" not in p["name"]]

    # 评分
    concentration_score = score_band(100 - top1_ratio, [(60, 15), (40, 12), (20, 8), (0, 4)])
    margin_score = score_band(avg_margin * 100, [(40, 5), (20, 3), (5, 1), (0, 0)])

    total_score = concentration_score + margin_score

    return {
        "score": total_score,
        "max_score": 20,
        "business_scope": scope[:200] if scope else "",
        "main_business": main_bus[:200] if main_bus else "",
        "top_business": by_industry[0].get("PRO_NAME_NEW", "") if by_industry else "",
        "top_business_ratio": round(top1_ratio, 1),
        "avg_gross_margin": round(avg_margin * 100, 2),
        "revenue_by_industry": [
            {"name": r.get("PRO_NAME_NEW", ""), "revenue_yi": round(safe_float(r.get("MAIN_BUSI_INCO")) / 1e8, 2),
             "margin": round(safe_float(r.get("GROSS_MARG")) * 100, 2)}
            for r in by_industry[:5]
        ],
        "revenue_by_product": product_breakdown[:5],
        "core_products": core_products[:3],
        "revenue_by_region": [
            {"name": r.get("PRO_NAME_NEW", ""), "revenue_yi": round(safe_float(r.get("MAIN_BUSI_INCO")) / 1e8, 2)}
            for r in by_region[:3]
        ],
        "scoring": {
            "concentration": {"score": concentration_score, "max": 15, "reason": f"最大业务占比{top1_ratio:.1f}%"},
            "margin": {"score": margin_score, "max": 5, "reason": f"加权毛利率{avg_margin*100:.2f}%"},
        }
    }


# ========================================
# 模块2：行业地位与竞争优势（满分25分）
# ========================================
def analyze_competitive_position() -> dict:
    """分析行业排名、竞争优势。"""
    ranking = load("industry_ranking.json")
    industry_avg = load("industry_average.json")
    main_data = load("main_accounting_data.json")

    meta = load_meta()
    sw_industry = meta.get("sw_industry", "")

    # 最新年报数据（年报用于排名对比更稳定）
    latest_annual = get_latest_period(main_data, prefer_annual=True)

    # 最新报告期数据（用于展示当前实力）
    latest_all = get_latest_period(main_data, prefer_annual=False)

    # 最新年报行业排名
    latest_rank = {}
    if ranking:
        annual_ranks = [r for r in ranking if "12-31" in str(r.get("END_DATE", ""))]
        if annual_ranks:
            latest_rank = max(annual_ranks, key=lambda x: str(x.get("END_DATE", "")))

    # ROE 排名
    roe_rank = safe_int(latest_rank.get("L01_RET_ON_EQU_RANK"))
    total_companies = safe_int(latest_rank.get("COM_NUM"))
    rev_rank = safe_int(latest_rank.get("L03_OPER_INC_RANK"))

    # 行业 ROE 均值
    ind_roe = 0
    if industry_avg:
        annual_avg = [r for r in industry_avg if "12-31" in str(r.get("END_DATE", ""))]
        if annual_avg:
            ind_roe = safe_float(max(annual_avg, key=lambda x: str(x.get("END_DATE", ""))).get("INDU_ROE"))

    # 年报 ROE（用于排名对比）
    annual_roe = safe_float(latest_annual.get("ROE_WEIGH")) if latest_annual else 0
    # 最新报告期 ROE（含季报）
    latest_roe = safe_float(latest_all.get("ROE_WEIGH")) if latest_all else 0

    # 排名百分位
    roe_pct = (1 - roe_rank / total_companies) * 100 if total_companies > 0 and roe_rank > 0 else 0
    rev_pct = (1 - rev_rank / total_companies) * 100 if total_companies > 0 and rev_rank > 0 else 0

    # 评分：规模排名(10) + 盈利排名(10) + 竞争优势(5)
    scale_score = score_band(rev_pct, [(75, 10), (50, 7), (25, 4), (0, 1)])
    profit_rank_score = score_band(roe_pct, [(75, 10), (50, 7), (25, 4), (0, 1)])
    above_ind = annual_roe > ind_roe * 1.2 if ind_roe > 0 else False
    advantage_score = 5 if above_ind else 2

    total_score = scale_score + profit_rank_score + advantage_score

    return {
        "score": total_score,
        "max_score": 25,
        "industry": sw_industry,
        "annual_roe": annual_roe,
        "latest_roe": latest_roe,
        "roe_rank": roe_rank,
        "roe_percentile": round(roe_pct, 1),
        "revenue_rank": rev_rank,
        "revenue_percentile": round(rev_pct, 1),
        "industry_avg_roe": ind_roe,
        "total_companies_in_industry": total_companies,
        "above_industry_avg": above_ind,
        "scoring": {
            "scale_ranking": {"score": scale_score, "max": 10, "reason": f"营收行业排名百分位{rev_pct:.1f}%"},
            "profit_ranking": {"score": profit_rank_score, "max": 10, "reason": f"ROE行业排名百分位{roe_pct:.1f}%"},
            "advantage": {"score": advantage_score, "max": 5, "reason": f"ROE {annual_roe}% vs 行业 {ind_roe}%"},
        }
    }


# ========================================
# 模块3：成长质量（满分25分）
# ========================================
def analyze_growth_quality() -> dict:
    """分析收入增长、利润增长趋势。同时展示年报和最新季报。"""
    main_data = load("main_accounting_data.json")

    # 年报序列
    annual_records = [r for r in main_data if "12-31" in str(r.get("END_DATE", ""))]
    annual_records.sort(key=lambda x: str(x.get("END_DATE", "")), reverse=True)

    yearly = []
    for r in annual_records[:5]:
        yearly.append({
            "date": str(r.get("END_DATE", ""))[:10],
            "revenue": safe_float(r.get("OPER_INC")),
            "net_profit": safe_float(r.get("NTPRO_PARE_COM")),
            "roe": safe_float(r.get("ROE_WEIGH")),
            "eps": safe_float(r.get("BAS_EPS")),
        })

    # 年报增长率
    growth_rates = []
    for i in range(len(yearly) - 1):
        curr = yearly[i]
        prev = yearly[i + 1]
        rev_growth = (curr["revenue"] - prev["revenue"]) / abs(prev["revenue"]) * 100 if prev["revenue"] != 0 else 0
        profit_growth = (curr["net_profit"] - prev["net_profit"]) / abs(prev["net_profit"]) * 100 if prev["net_profit"] != 0 else 0
        growth_rates.append({
            "date": curr["date"],
            "revenue_growth": round(rev_growth, 2),
            "profit_growth": round(profit_growth, 2),
        })

    # 最新季报数据（含同比）
    latest_all = get_latest_period(main_data, prefer_annual=False)
    latest_period = str(latest_all.get("END_DATE", ""))[:10] if latest_all else ""

    # 评分用年报增长率
    latest_growth = growth_rates[0] if growth_rates else {}
    rev_g = latest_growth.get("revenue_growth", 0)
    prof_g = latest_growth.get("profit_growth", 0)

    avg_rev_growth = sum(g["revenue_growth"] for g in growth_rates[:3]) / len(growth_rates[:3]) if growth_rates else 0
    avg_profit_growth = sum(g["profit_growth"] for g in growth_rates[:3]) / len(growth_rates[:3]) if growth_rates else 0

    quality_ratio = prof_g - rev_g if rev_g != 0 else 0

    # 评分（满分25：营收6 + 利润6 + 持续性7 + 质量6）
    revenue_score = score_band(rev_g, [(30, 6), (15, 5), (5, 3), (0, 1), (-100, 0)])
    profit_score = score_band(prof_g, [(30, 6), (15, 5), (5, 3), (0, 1), (-100, 0)])
    sustainability_score = score_band(avg_rev_growth, [(20, 7), (10, 5), (0, 2), (-5, 1), (-100, 0)])
    quality_score = 6 if quality_ratio > 5 else (3 if quality_ratio > 0 else 0)

    total_score = min(revenue_score + profit_score + sustainability_score + quality_score, 25)

    # 【新增】最新报告期关键数据
    latest_quarter_info = {}
    if latest_all:
        latest_quarter_info = {
            "period": latest_period,
            "revenue_yi": round(safe_float(latest_all.get("OPER_INC")) / 1e8, 2),
            "net_profit_yi": round(safe_float(latest_all.get("NTPRO_PARE_COM")) / 1e8, 2),
            "roe": safe_float(latest_all.get("ROE_WEIGH")),
            "eps": safe_float(latest_all.get("BAS_EPS")),
        }

    return {
        "score": total_score,
        "max_score": 25,
        "latest": latest_growth,
        "yearly_growth": growth_rates,
        "yearly_data": yearly,
        "latest_quarter": latest_quarter_info,
        "avg_3y_revenue_growth": round(avg_rev_growth, 2),
        "avg_3y_profit_growth": round(avg_profit_growth, 2),
        "quality_ratio": round(quality_ratio, 2),
        "scoring": {
            "revenue_growth": {"score": revenue_score, "max": 6, "reason": f"最新营收增速{rev_g:.1f}%"},
            "profit_growth": {"score": profit_score, "max": 6, "reason": f"最新利润增速{prof_g:.1f}%"},
            "sustainability": {"score": sustainability_score, "max": 7, "reason": f"3年平均营收增速{avg_rev_growth:.1f}%"},
            "quality": {"score": quality_score, "max": 6, "reason": f"利润增速-营收增速={quality_ratio:.1f}%"},
        }
    }


# ========================================
# 模块4：财务质量（满分20分）
# ========================================
def analyze_financial_quality() -> dict:
    """分析盈利质量、资产质量、现金流质量。"""
    main_data = load("main_accounting_data.json")
    profit_quality = load("indicator_profit_quality.json")
    balance_notes = load("balance_sheet_notes.json")

    # 年报数据（用于评分基准）
    latest = get_latest_period(main_data, prefer_annual=True)

    # 最新报告期数据（用于展示当前状态）
    latest_all = get_latest_period(main_data, prefer_annual=False)

    revenue = safe_float(latest.get("OPER_INC"))
    net_profit = safe_float(latest.get("NTPRO_PARE_COM"))
    oper_cash = safe_float(latest.get("NET_OPER_CASH"))
    total_assets = safe_float(latest.get("TOT_ASE"))
    total_liabilities = safe_float(latest.get("TOT_LIAB"))
    roe = safe_float(latest.get("ROE_WEIGH"))
    debt_ratio = safe_float(latest.get("DEBT_RATIO"))
    eps = safe_float(latest.get("BAS_EPS"))

    # 最新报告期的负债率
    latest_debt_ratio = safe_float(latest_all.get("DEBT_RATIO")) if latest_all else debt_ratio

    # 利润含金量
    cash_to_profit = oper_cash / abs(net_profit) * 100 if net_profit != 0 else 0

    # 【新增】应收账款同比增速
    ar_by_period = {}
    for r in balance_notes:
        if "应收" in str(r.get("SUBJ_NAME", "")):
            ed = str(r.get("END_DATE", ""))
            amt = safe_float(r.get("FINA_AMOUNT"))
            if ed not in ar_by_period:
                ar_by_period[ed] = 0
            ar_by_period[ed] += amt

    ar_periods = sorted(ar_by_period.keys(), reverse=True)
    ar_latest = ar_by_period[ar_periods[0]] if len(ar_periods) >= 1 else 0
    ar_prev = ar_by_period[ar_periods[1]] if len(ar_periods) >= 2 else 0
    ar_growth = (ar_latest - ar_prev) / abs(ar_prev) * 100 if ar_prev != 0 else 0
    ar_to_assets = ar_latest / total_assets * 100 if total_assets > 0 and ar_latest > 0 else 0

    # ROE 评分（满分20：ROE8 + 负债6 + 现金流6）
    roe_score = score_band(roe, [(20, 8), (15, 6), (10, 4), (5, 2), (0, 0)])
    debt_score = score_band(100 - debt_ratio, [(60, 6), (40, 4), (25, 3), (10, 1), (0, 0)])
    cash_score = score_band(cash_to_profit, [(120, 6), (80, 4), (50, 3), (0, 1), (-100, 0)])

    # 盈利质量预警
    latest_pq = {}
    annual_pq = [r for r in profit_quality if "12-31" in str(r.get("END_DATE", ""))]
    annual_pq.sort(key=lambda x: str(x.get("END_DATE", "")), reverse=True)
    if annual_pq:
        latest_pq = annual_pq[0]
    warn_sign = latest_pq.get("WARN_SIGN", "")

    quality_deduction = 0
    if "庞氏骗局" in warn_sign:
        quality_deduction = 2
    elif "预警" in warn_sign:
        quality_deduction = 1

    # 审计意见（提取类型）
    audit = load("audit_opinion.json")
    annual_audit = sorted([r for r in audit if "12-31" in str(r.get("END_DATE", ""))],
                          key=lambda x: str(x.get("END_DATE", "")), reverse=True)
    audit_opinion_raw = annual_audit[0].get("AUDIT_OPIN1", "") if annual_audit else ""
    if "无法表示" in audit_opinion_raw or "否定" in audit_opinion_raw:
        audit_type = "无法表示/否定"
        quality_deduction += 4
    elif "保留" in audit_opinion_raw:
        audit_type = "保留意见"
        quality_deduction += 1
    elif "无保留" in audit_opinion_raw or "公允" in audit_opinion_raw:
        audit_type = "标准无保留"
    else:
        audit_type = "未明确"

    total_score = max(roe_score + debt_score + cash_score - quality_deduction, 0)

    return {
        "score": total_score,
        "max_score": 20,
        "roe": roe,
        "latest_debt_ratio": latest_debt_ratio,
        "annual_debt_ratio": debt_ratio,
        "eps": eps,
        "cash_to_profit_ratio": round(cash_to_profit, 1),
        "revenue_yi": round(revenue / 1e8, 2),
        "net_profit_yi": round(net_profit / 1e8, 2),
        "oper_cash_yi": round(oper_cash / 1e8, 2),
        "total_assets_yi": round(total_assets / 1e8, 2),
        "total_liabilities_yi": round(total_liabilities / 1e8, 2),
        "accounts_receivable_growth": round(ar_growth, 1),
        "accounts_receivable_to_assets": round(ar_to_assets, 1),
        "profit_quality_warn": warn_sign,
        "audit_type": audit_type,
        "scoring": {
            "roe": {"score": roe_score, "max": 8, "reason": f"ROE={roe:.2f}%"},
            "debt": {"score": debt_score, "max": 6, "reason": f"资产负债率={debt_ratio:.2f}%（最新{latest_debt_ratio:.1f}%）"},
            "cash": {"score": cash_score, "max": 6, "reason": f"现金流/净利润={cash_to_profit:.1f}%"},
            "quality_deduction": {"score": -quality_deduction, "max": 0, "reason": f"预警={warn_sign}, 审计={audit_type}"},
        }
    }


# ========================================
# 模块5：治理与资本配置（满分10分）
# ========================================
def analyze_governance() -> dict:
    """分析管理层、股权结构、分红、质押。"""
    controller = load("actual_controller.json")
    shareholders = load("top10_shareholders.json")
    pledge = load("share_pledge.json")
    div_plan = load("dividend_plan.json")
    div_impl = load("dividend_implementation.json")
    incentive = load("equity_incentive.json")

    # 【新增】高管增减持
    dir_changes = load("director_share_changes.json")
    man_changes = load("management_share_changes.json")

    # 实控人
    latest_controller = {}
    if controller:
        controller.sort(key=lambda x: str(x.get("END_DATE", "")), reverse=True)
        latest_controller = controller[0]
    controller_name = latest_controller.get("ACTU_CONTLR", "")
    control_ratio = safe_float(latest_controller.get("CONTL_HLD_RATIO"))

    # 最新十大股东
    latest_top10 = []
    if shareholders:
        shareholders.sort(key=lambda x: str(x.get("END_DATE", "")), reverse=True)
        latest_date = str(shareholders[0].get("END_DATE", ""))
        latest_top10 = [r for r in shareholders if str(r.get("END_DATE", "")) == latest_date and r.get("HOLD_RANK")]

    # 【新增】质押与十大股东交叉检查
    pledge_details = []
    pledge_names = set()
    if pledge:
        for p in pledge:
            pname = p.get("PLE_HLD_NAME", "")
            pvol = safe_float(p.get("PLE_VOL"))
            if pname and pvol > 0:
                pledge_names.add(pname)
                pledge_details.append({
                    "name": pname,
                    "pledge_shares": round(pvol / 1e4, 0),
                    "start_date": str(p.get("START_DATE", ""))[:10],
                })

    # 十大股东中的质押情况
    top10_pledge_info = []
    for s in latest_top10:
        sname = s.get("HLD_NAME", "")
        if sname in pledge_names:
            top10_pledge_info.append({
                "name": sname,
                "hold_ratio": safe_float(s.get("HOLD_RATIO")),
                "is_pledged": True,
            })

    pledge_count = len(pledge_details)

    # 【新增】高管增减持分析
    all_changes = dir_changes + man_changes
    recent_changes = []
    for c in all_changes:
        chan_type = str(c.get("CHAN_REAS_PAR", ""))
        chan_vol = safe_float(c.get("CHAN_VOL"))
        if chan_vol != 0:
            recent_changes.append({
                "name": c.get("INDIV_NAME", ""),
                "position": c.get("POSI_NAME", ""),
                "change_type": chan_type,
                "volume": round(chan_vol),
                "date": str(c.get("CHAN_DATE", c.get("END_DATE", "")))[:10],
            })
    recent_changes.sort(key=lambda x: x["date"], reverse=True)
    recent_changes = recent_changes[:10]

    # 判断是否有减持
    has_reduction = any(c["volume"] < 0 for c in recent_changes[:5])

    # 分红情况
    div_years = []
    for r in div_plan:
        if r.get("IS_DIV_PAR") == "是":
            div_years.append(str(r.get("END_DATE", ""))[:4])
    div_count = len(div_years)

    latest_div = {}
    if div_impl:
        div_impl.sort(key=lambda x: str(x.get("END_DATE", "")), reverse=True)
        latest_div = div_impl[0]
    div_rmb = safe_float(latest_div.get("DIV_RMB"))

    has_incentive = len(incentive) > 0

    # 审计连续性
    audit = load("audit_opinion.json")
    audit_firms = set(r.get("ACC_OFFI_IN1", "") for r in audit if r.get("ACC_OFFI_IN1"))

    # 评分
    if 20 <= control_ratio <= 50:
        ctrl_score = 3
    elif 10 <= control_ratio < 20 or 50 < control_ratio <= 60:
        ctrl_score = 2
    else:
        ctrl_score = 1

    div_score = score_band(div_count, [(4, 3), (2, 2), (1, 1), (0, 0)])

    # 质押评分：考虑十大股东质押
    if pledge_count == 0 or not top10_pledge_info:
        pledge_score = 1
    else:
        pledge_score = 0

    gov_bonus = 1 if has_incentive else 0
    audit_score = 2 if len(audit_firms) <= 2 and len(audit) > 0 else 1

    total_score = ctrl_score + div_score + pledge_score + gov_bonus + audit_score

    return {
        "score": total_score,
        "max_score": 10,
        "actual_controller": controller_name,
        "control_ratio": control_ratio,
        "top10_shareholders": [
            {"rank": r.get("HOLD_RANK"), "name": r.get("HLD_NAME", ""), "ratio": safe_float(r.get("HOLD_RATIO"))}
            for r in latest_top10[:5]
        ],
        "pledge_count": pledge_count,
        "pledge_details": pledge_details[:5],
        "top10_pledge": top10_pledge_info,
        "dividend_years": div_years,
        "dividend_count": div_count,
        "latest_dividend_per_share": div_rmb,
        "has_equity_incentive": has_incentive,
        "audit_firms": list(audit_firms),
        "insider_trading": recent_changes,
        "has_insider_reduction": has_reduction,
        "scoring": {
            "control_structure": {"score": ctrl_score, "max": 3, "reason": f"实控人持股{control_ratio:.1f}%"},
            "dividend": {"score": div_score, "max": 3, "reason": f"近5年分红{div_count}次"},
            "pledge_risk": {"score": pledge_score, "max": 1, "reason": f"质押记录{pledge_count}条，十大股东质押{len(top10_pledge_info)}人"},
            "governance_bonus": {"score": gov_bonus, "max": 1, "reason": f"股权激励={'有' if has_incentive else '无'}"},
            "audit_continuity": {"score": audit_score, "max": 2, "reason": f"审计机构{len(audit_firms)}家"},
        }
    }


# ========================================
# 模块6：风险扣分项（扣分，最多扣15分）
# ========================================
def analyze_risks() -> dict:
    """识别主要风险扣分项。"""
    main_data = load("main_accounting_data.json")
    related_trade = load("related_trade.json")
    balance_notes = load("balance_sheet_notes.json")
    non_recurring = load("non_recurring.json")
    profit_quality = load("indicator_profit_quality.json")
    gov = analyze_governance()  # 复用治理分析的质押和减持数据

    # 用年报做基准
    latest = get_latest_period(main_data, prefer_annual=True)
    latest_all = get_latest_period(main_data, prefer_annual=False)
    net_profit = safe_float(latest.get("NTPRO_PARE_COM"))
    revenue = safe_float(latest.get("OPER_INC"))
    total_assets = safe_float(latest.get("TOT_ASE"))

    deductions = []

    # 1. 关联交易占比
    if related_trade:
        latest_end = max(str(r.get("END_DATE", "")) for r in related_trade)
        latest_related = sum(abs(safe_float(r.get("THIS_TRADE_AMUT"))) for r in related_trade
                             if str(r.get("END_DATE", "")) == latest_end)
        related_ratio = latest_related / revenue * 100 if revenue > 0 else 0
        if related_ratio > 30:
            deductions.append({"item": "关联交易占比过高", "deduction": 3, "detail": f"关联交易占营收{related_ratio:.1f}%"})
        elif related_ratio > 15:
            deductions.append({"item": "关联交易占比较高", "deduction": 1, "detail": f"关联交易占营收{related_ratio:.1f}%"})

    # 2. 非经常性损益占比
    annual_nr = [r for r in non_recurring if "12-31" in str(r.get("END_DATE", ""))]
    if annual_nr:
        latest_nr_date = max(str(r.get("END_DATE", "")) for r in annual_nr)
        nr_total = sum(abs(safe_float(r.get("RELA_ACOUT"))) for r in annual_nr if str(r.get("END_DATE", "")) == latest_nr_date)
        nr_ratio = nr_total / abs(net_profit) * 100 if net_profit != 0 else 0
        if nr_ratio > 50:
            deductions.append({"item": "非经常性损益占比高", "deduction": 2, "detail": f"占净利润{nr_ratio:.1f}%"})
        elif nr_ratio > 20:
            deductions.append({"item": "非经常性损益需关注", "deduction": 1, "detail": f"占净利润{nr_ratio:.1f}%"})

    # 3. 盈利质量预警
    annual_pq = [r for r in profit_quality if "12-31" in str(r.get("END_DATE", ""))]
    if annual_pq:
        annual_pq.sort(key=lambda x: str(x.get("END_DATE", "")), reverse=True)
        warn = annual_pq[0].get("WARN_SIGN", "")
        if "庞氏骗局" in warn:
            deductions.append({"item": "盈利质量预警", "deduction": 3, "detail": warn})
        elif "预警" in warn:
            deductions.append({"item": "盈利质量需关注", "deduction": 1, "detail": warn})

    # 4. 资产负债率过高（用最新报告期）
    latest_debt = safe_float(latest_all.get("DEBT_RATIO")) if latest_all else safe_float(latest.get("DEBT_RATIO"))
    if latest_debt > 80:
        deductions.append({"item": "资产负债率过高", "deduction": 3, "detail": f"资产负债率{latest_debt:.1f}%"})
    elif latest_debt > 70:
        deductions.append({"item": "资产负债率偏高", "deduction": 1, "detail": f"资产负债率{latest_debt:.1f}%"})

    # 5. 应收账款增速过快
    ar_by_period = {}
    for r in balance_notes:
        if "应收" in str(r.get("SUBJ_NAME", "")):
            ed = str(r.get("END_DATE", ""))
            amt = safe_float(r.get("FINA_AMOUNT"))
            if ed not in ar_by_period:
                ar_by_period[ed] = 0
            ar_by_period[ed] += amt

    ar_periods = sorted(ar_by_period.keys(), reverse=True)
    if len(ar_periods) >= 2:
        ar_curr = ar_by_period[ar_periods[0]]
        ar_prev = ar_by_period[ar_periods[1]]
        ar_growth = (ar_curr - ar_prev) / abs(ar_prev) * 100 if ar_prev != 0 else 0
        if ar_growth > 100:
            deductions.append({"item": "应收账款增速过快", "deduction": 2, "detail": f"应收同比+{ar_growth:.0f}%"})
        elif ar_growth > 50:
            deductions.append({"item": "应收账款增速需关注", "deduction": 1, "detail": f"应收同比+{ar_growth:.0f}%"})

    # 【新增】6. 高管减持扣分
    if gov.get("has_insider_reduction"):
        deductions.append({"item": "高管减持", "deduction": 1, "detail": "近期存在高管减持行为"})

    total_deduction = min(sum(d["deduction"] for d in deductions), 10)

    return {
        "total_deduction": total_deduction,
        "max_deduction": 10,
        "risk_items": deductions,
    }


# ========================================
# 汇总评分
# ========================================
def calculate_total_score() -> dict:
    bm = analyze_business_model()
    cp = analyze_competitive_position()
    gq = analyze_growth_quality()
    fq = analyze_financial_quality()
    gv = analyze_governance()
    risk = analyze_risks()

    raw_score = bm["score"] + cp["score"] + gq["score"] + fq["score"] + gv["score"]
    final_score = max(raw_score - risk["total_deduction"], 0)
    # 分母=五大维度满分之和（87）。风险扣分是减分项（从已得分数里扣，最好扣0），
    # 不计入分母——否则任何公司最高只能 87/97≈89.7%，永远到不了满分。
    max_score = bm["max_score"] + cp["max_score"] + gq["max_score"] + fq["max_score"] + gv["max_score"]

    if final_score >= 90:
        grade = "A（优质）"
    elif final_score >= 75:
        grade = "B（良好）"
    elif final_score >= 60:
        grade = "C（一般）"
    elif final_score >= 40:
        grade = "D（较弱）"
    else:
        grade = "E（差）"

    return {
        "final_score": final_score,
        "max_score": max_score,
        "raw_score": raw_score,
        "grade": grade,
        "business_model": bm,
        "competitive_position": cp,
        "growth_quality": gq,
        "financial_quality": fq,
        "governance": gv,
        "risk_deduction": risk,
    }


def main():
    stk_code = sys.argv[1] if len(sys.argv) > 1 else ""
    meta = load_meta()
    if not stk_code:
        stk_code = meta.get("stk_code", "unknown")

    print(f"=== 公司质地打分 - 结构化分析 ===")
    print(f"股票代码: {stk_code}")

    result = calculate_total_score()

    print(f"\n--- 评分结果 ---")
    print(f"质地总评: {result['final_score']}/{result['max_score']} ({result['grade']})")
    print(f"  商业模式: {result['business_model']['score']}/{result['business_model']['max_score']}")
    print(f"  行业地位: {result['competitive_position']['score']}/{result['competitive_position']['max_score']}")
    print(f"  成长质量: {result['growth_quality']['score']}/{result['growth_quality']['max_score']}")
    print(f"  财务质量: {result['financial_quality']['score']}/{result['financial_quality']['max_score']}")
    print(f"  治理与资本配置: {result['governance']['score']}/{result['governance']['max_score']}")
    print(f"  风险扣分: -{result['risk_deduction']['total_deduction']}")
    for r in result['risk_deduction']['risk_items']:
        print(f"    - {r['item']}: {r['detail']}")

    output = DATA_DIR / "analysis.json"
    with open(output, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"\n=== 分析完成！结果已保存到 {output} ===")


if __name__ == "__main__":
    main()
