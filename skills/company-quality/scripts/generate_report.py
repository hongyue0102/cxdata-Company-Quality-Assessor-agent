#!/usr/bin/env python3
"""
公司质地打分 - 报告骨架生成器

输出数值固定的 Markdown 骨架（所有表格数值/字段名/结构由 Python 写死），
LLM 只需在每个「**AI 解读：**」槽位补充文字解读。

使用方式：
    python generate_report.py [股票代码]

读取：
    data/meta.json
    data/analysis.json
输出：
    stdout 完整 Markdown 骨架

设计原则（与 cxdata-stock-analysis-agent/analyzer.py 一致）：
    1. 所有数值必须 100% 来自 analysis.json，禁止 LLM 自行计算或估算
    2. 表格结构、字段名、单位由 Python 写死，LLM 不得修改
    3. 每段表格后留「**AI 解读：**」槽位，LLM 只在槽位填文字
    4. 报告末尾的免责声明必须原样保留
"""

import json
import re
import sys
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data"


# ========== 输入净化（参照 cxdata-stock-analysis-agent/analyzer.py） ==========

# 控制字符与换行（防报告结构破坏 / 日志注入）
_CONTROL_RE = re.compile(r"[\r\n\t\x00-\x1f\x7f]")


def _md(value) -> str:
    """
    净化拼入 markdown 报告的远端/用户可控字段（公司名、行业、股东名、扣分项等），
    剥离控制字符并转义 HTML 特殊字符，防止报告渲染为 HTML 时触发 XSS。
    """
    if value is None:
        return ""
    cleaned = _CONTROL_RE.sub(" ", str(value))
    return (cleaned.replace("&", "&amp;")
                   .replace("<", "&lt;")
                   .replace(">", "&gt;")
                   .replace('"', "&quot;"))


# ========== 辅助格式化函数（参照 analyzer.py:127-153） ==========

def _fmt_num(val, decimals=2):
    """数值格式化，None 兜底为 N/A。"""
    if val is None or val == "":
        return "N/A"
    try:
        return f"{float(val):.{decimals}f}"
    except (ValueError, TypeError):
        return str(val)


def _fmt_pct(val, decimals=2, with_sign=False):
    """百分比格式化。with_sign=True 时正数加 + 号。"""
    if val is None or val == "":
        return "N/A"
    try:
        v = float(val)
        sign = "+" if (with_sign and v > 0) else ""
        return f"{sign}{v:.{decimals}f}%"
    except (ValueError, TypeError):
        return str(val)


def _fmt_yi(val, decimals=2):
    """亿元金额格式化（输入值单位已经是亿元）。"""
    if val is None or val == "":
        return "N/A"
    try:
        return f"{float(val):.{decimals}f} 亿"
    except (ValueError, TypeError):
        return str(val)


def _fmt_yi_from_yuan(val, decimals=2):
    """元 → 亿元格式化（输入值单位是元）。"""
    if val is None or val == "":
        return "N/A"
    try:
        return f"{float(val) / 1e8:.{decimals}f} 亿"
    except (ValueError, TypeError):
        return str(val)


def _fmt_score(score, max_score):
    """评分格式化为 '15/20'。"""
    if score is None or max_score is None:
        return "N/A"
    return f"{score}/{max_score}"


def _fmt_bool(val):
    """布尔值格式化为 是/否。"""
    if val is None:
        return "N/A"
    return "是" if val else "否"


def _fmt_date_short(date_str):
    """日期截取前 10 位。如 '2025-12-31' → '2025-12-31'。"""
    if not date_str:
        return "N/A"
    return str(date_str)[:10]


# ========== 数据加载 ==========

def _load_data(stk_code=None):
    """读取 meta.json + analysis.json，合并返回。"""
    meta_path = DATA_DIR / "meta.json"
    analysis_path = DATA_DIR / "analysis.json"

    if not meta_path.exists():
        print(f"[ERROR] meta.json 不存在，请先运行 fetch_data.py {stk_code or '<代码>'}", file=sys.stderr)
        sys.exit(1)
    if not analysis_path.exists():
        print(f"[ERROR] analysis.json 不存在，请先运行 analyze_data.py {stk_code or '<代码>'}", file=sys.stderr)
        sys.exit(1)

    with open(meta_path, encoding="utf-8") as f:
        meta_list = json.load(f)
    meta = meta_list[0] if meta_list else {}

    with open(analysis_path, encoding="utf-8") as f:
        analysis = json.load(f)

    analysis["_meta"] = meta
    return analysis


# ========== 8 段骨架生成 ==========

def _anchor(a):
    """从 meta 动态生成 '公司简称（代码）' 锚点字符串，用于段落标题和 AI 约束。"""
    meta = a.get("_meta", {})
    company_info = {}
    ci_path = DATA_DIR / "company_info.json"
    if ci_path.exists():
        try:
            with open(ci_path, encoding="utf-8") as f:
                ci_list = json.load(f)
            if ci_list:
                company_info = ci_list[0]
        except Exception:
            pass
    short_name = company_info.get("STK_SHORT_NAME") or company_info.get("COM_CHI_SHORT_NAME") or ""
    stk_code = meta.get("stk_code", "") or ""
    if short_name and stk_code:
        return f"{short_name}（{stk_code}）"
    name = meta.get("company_name", "") or ""
    if name and stk_code:
        return f"{name}（{stk_code}）"
    return stk_code or name or ""


def _build_header(a, lines):
    """报告标题与基本信息行。"""
    meta = a.get("_meta", {})
    company_name = meta.get("company_name", "") or "（公司名缺失）"
    stk_code = meta.get("stk_code", "") or "（代码缺失）"
    fetch_time = meta.get("fetch_time", "")

    lines.append(f"# 【公司质地评估报告】{_md(company_name)}（{_md(stk_code)}）")
    lines.append("")
    lines.append(f"> 数据获取时间：{fetch_time} | 数据来源：财新数据（cxdata） | 基于公开财务数据推演，不构成任何投资建议")
    lines.append("")
    anchor = _anchor(a)
    lines.append("")
    lines.append("---")
    lines.append("")


def _build_section1_score(a, lines):
    """第 1 段：公司质地总评分。"""
    final_score = a.get("final_score")
    max_score = a.get("max_score")
    grade = a.get("grade", "N/A")
    cp = a.get("competitive_position", {}) or {}
    industry = cp.get("industry", "N/A")
    risk = a.get("risk_deduction", {}) or {}
    total_deduction = risk.get("total_deduction")
    max_deduction = risk.get("max_deduction")

    lines.append(f"## 【1. 公司质地总评分】—— {_md(_anchor(a))}")
    lines.append("")
    lines.append("| 项目 | 数据 |")
    lines.append("|------|------|")
    lines.append(f"| **质地总评** | {_fmt_score(final_score, max_score)} |")
    lines.append(f"| **质地等级** | {_md(grade)} |")
    lines.append(f"| **所属行业** | {_md(industry)} |")
    lines.append(f"| **风险扣分** | {_fmt_score(total_deduction, max_deduction)} |")
    lines.append("")
    lines.append("> **一句话定性：**")
    lines.append("")
    lines.append("**AI 解读：**")
    lines.append("")
    lines.append("---")
    lines.append("")


def _build_section2_business(a, lines):
    """第 2 段：商业模式与壁垒。"""
    bm = a.get("business_model", {}) or {}
    score = bm.get("score")
    max_score = bm.get("max_score")
    top_business = bm.get("top_business", "N/A")
    top_business_ratio = bm.get("top_business_ratio")
    avg_gross_margin = bm.get("avg_gross_margin")
    main_business = (bm.get("main_business") or "").strip()

    lines.append(f"## 【2. 商业模式与壁垒】—— {_md(_anchor(a))}")
    lines.append("")
    lines.append(f"**得分：{_fmt_score(score, max_score)}**")
    lines.append("")
    lines.append("**核心指标：**")
    lines.append("")
    lines.append("| 核心指标 | 数据 |")
    lines.append("|----------|------|")
    lines.append(f"| 最大业务板块 | {_md(top_business)} |")
    lines.append(f"| 最大业务收入占比 | {_fmt_pct(top_business_ratio)} |")
    lines.append(f"| 加权毛利率 | {_fmt_pct(avg_gross_margin)} |")
    lines.append("")
    lines.append(f"**主营业务：** {_md(main_business) if main_business else 'N/A'}")
    lines.append("")

    # 收入结构（按行业）
    rev_industry = bm.get("revenue_by_industry", []) or []
    lines.append("**收入结构（按行业）：**")
    lines.append("")
    lines.append("| 业务 | 收入（亿元） | 毛利率 |")
    lines.append("|------|--------------|--------|")
    if rev_industry:
        for row in rev_industry:
            name = row.get("name", "")
            rev = row.get("revenue_yi")
            margin = row.get("margin")
            lines.append(f"| {_md(name)} | {_fmt_num(rev)} | {_fmt_pct(margin)} |")
    else:
        lines.append("| （无数据） | - | - |")
    lines.append("")

    # 收入结构（按区域）
    rev_region = bm.get("revenue_by_region", []) or []
    lines.append("**收入结构（按区域）：**")
    lines.append("")
    lines.append("| 区域 | 收入（亿元） |")
    lines.append("|------|--------------|")
    if rev_region:
        for row in rev_region:
            name = row.get("name", "")
            rev = row.get("revenue_yi")
            lines.append(f"| {_md(name)} | {_fmt_num(rev)} |")
    else:
        lines.append("| （无数据） | - |")
    lines.append("")

    lines.append("**AI 解读：**")
    lines.append("")
    lines.append("---")
    lines.append("")


def _build_section3_competitive(a, lines):
    """第 3 段：行业地位与竞争优势。"""
    cp = a.get("competitive_position", {}) or {}
    score = cp.get("score")
    max_score = cp.get("max_score")
    industry = cp.get("industry", "N/A")
    total_companies = cp.get("total_companies_in_industry")
    annual_roe = cp.get("annual_roe")
    latest_roe = cp.get("latest_roe")
    industry_avg_roe = cp.get("industry_avg_roe")
    roe_rank = cp.get("roe_rank")
    roe_percentile = cp.get("roe_percentile")
    revenue_rank = cp.get("revenue_rank")
    revenue_percentile = cp.get("revenue_percentile")
    above_avg = cp.get("above_industry_avg")

    lines.append(f"## 【3. 行业地位与竞争优势】—— {_md(_anchor(a))}")
    lines.append("")
    lines.append(f"**得分：{_fmt_score(score, max_score)}**")
    lines.append("")
    lines.append("| 指标 | 数据 |")
    lines.append("|------|------|")
    lines.append(f"| 所属行业 | {_md(industry)} |")
    lines.append(f"| 行业内公司总数 | {_fmt_num(total_companies, 0) if total_companies is not None else 'N/A'} 家 |")
    lines.append(f"| 年度 ROE | {_fmt_pct(annual_roe)} |")
    lines.append(f"| 最新报告期 ROE | {_fmt_pct(latest_roe)} |")
    industry_avg_roe_name = cp.get("industry_avg_roe_name", "")
    roe_label = f"行业 ROE（加权平均·{_md(industry_avg_roe_name)}）" if industry_avg_roe_name else "行业 ROE（加权平均）"
    lines.append(f"| {roe_label} | {_fmt_pct(industry_avg_roe)} |")
    lines.append(f"| ROE 是否超行业均值 | {_fmt_bool(above_avg)} |")
    lines.append(f"| ROE 行业排名 | 第 {_fmt_num(roe_rank, 0) if roe_rank is not None else 'N/A'} 名 |")
    lines.append(f"| ROE 行业分位 | {_fmt_pct(roe_percentile)} |")
    lines.append(f"| 营收 行业排名 | 第 {_fmt_num(revenue_rank, 0) if revenue_rank is not None else 'N/A'} 名 |")
    lines.append(f"| 营收 行业分位 | {_fmt_pct(revenue_percentile)} |")
    lines.append("")
    lines.append("**AI 解读：**")
    lines.append("")
    lines.append("---")
    lines.append("")


def _build_section4_growth(a, lines):
    """第 4 段：成长质量。"""
    gq = a.get("growth_quality", {}) or {}
    score = gq.get("score")
    max_score = gq.get("max_score")

    lines.append(f"## 【4. 成长质量】—— {_md(_anchor(a))}")
    lines.append("")
    lines.append(f"**得分：{_fmt_score(score, max_score)}**")
    lines.append("")

    # 近 5 年年度数据
    yearly_data = gq.get("yearly_data", []) or []
    lines.append("**近 5 年年度数据：**")
    lines.append("")
    lines.append("| 年度 | 营收（亿元） | 净利润（亿元） | ROE | EPS |")
    lines.append("|------|--------------|----------------|-----|-----|")
    if yearly_data:
        for row in yearly_data:
            date_str = _fmt_date_short(row.get("date"))
            revenue = row.get("revenue")
            net_profit = row.get("net_profit")
            roe = row.get("roe")
            eps = row.get("eps")
            lines.append(
                f"| {date_str} | {_fmt_yi_from_yuan(revenue)} | {_fmt_yi_from_yuan(net_profit)} "
                f"| {_fmt_pct(roe)} | {_fmt_num(eps)} |"
            )
    else:
        lines.append("| （无数据） | - | - | - | - |")
    lines.append("")

    # 年度增速
    yearly_growth = gq.get("yearly_growth", []) or []
    lines.append("**年度增速：**")
    lines.append("")
    lines.append("| 年度 | 营收增速 | 利润增速 |")
    lines.append("|------|----------|----------|")
    if yearly_growth:
        for row in yearly_growth:
            date_str = _fmt_date_short(row.get("date"))
            rev_g = row.get("revenue_growth")
            prof_g = row.get("profit_growth")
            lines.append(f"| {date_str} | {_fmt_pct(rev_g, with_sign=True)} | {_fmt_pct(prof_g, with_sign=True)} |")
    else:
        lines.append("| （无数据） | - | - |")
    lines.append("")

    # 核心增速指标
    avg_3y_rev = gq.get("avg_3y_revenue_growth")
    avg_3y_prof = gq.get("avg_3y_profit_growth")
    quality_ratio = gq.get("quality_ratio")
    lines.append("**核心增速指标：**")
    lines.append("")
    lines.append("| 指标 | 数据 |")
    lines.append("|------|------|")
    lines.append(f"| 3 年平均营收增速 | {_fmt_pct(avg_3y_rev, with_sign=True)} |")
    lines.append(f"| 3 年平均利润增速 | {_fmt_pct(avg_3y_prof, with_sign=True)} |")
    lines.append(f"| 利润/营收 增速差 | {_fmt_pct(quality_ratio, with_sign=True)} |")
    lines.append("")

    # 最新季度
    lq = gq.get("latest_quarter", {}) or {}
    lines.append("**最新季度数据：**")
    lines.append("")
    lines.append("| 指标 | 数据 |")
    lines.append("|------|------|")
    lines.append(f"| 报告期 | {_fmt_date_short(lq.get('period'))} |")
    lines.append(f"| 营收（亿元） | {_fmt_num(lq.get('revenue_yi'))} |")
    lines.append(f"| 净利润（亿元） | {_fmt_num(lq.get('net_profit_yi'))} |")
    lines.append(f"| ROE | {_fmt_pct(lq.get('roe'))} |")
    lines.append(f"| EPS | {_fmt_num(lq.get('eps'))} |")
    lines.append("")
    lines.append("**AI 解读：**")
    lines.append("")
    lines.append("---")
    lines.append("")


def _build_section5_financial(a, lines):
    """第 5 段：财务质量。"""
    fq = a.get("financial_quality", {}) or {}
    score = fq.get("score")
    max_score = fq.get("max_score")

    lines.append(f"## 【5. 财务质量】—— {_md(_anchor(a))}")
    lines.append("")
    lines.append(f"**得分：{_fmt_score(score, max_score)}**")
    lines.append("")
    lines.append("| 指标 | 数据 |")
    lines.append("|------|------|")
    lines.append(f"| ROE（年度） | {_fmt_pct(fq.get('roe'))} |")
    lines.append(f"| 年度资产负债率 | {_fmt_pct(fq.get('annual_debt_ratio'))} |")
    lines.append(f"| EPS | {_fmt_num(fq.get('eps'))} |")
    lines.append(f"| 经营现金流/净利润 | {_fmt_pct(fq.get('cash_to_profit_ratio'))} |")
    lines.append(f"| 营收（亿元） | {_fmt_num(fq.get('revenue_yi'))} |")
    lines.append(f"| 净利润（亿元） | {_fmt_num(fq.get('net_profit_yi'))} |")
    lines.append(f"| 经营现金流（亿元） | {_fmt_num(fq.get('oper_cash_yi'))} |")
    lines.append(f"| 总资产（亿元） | {_fmt_num(fq.get('total_assets_yi'))} |")
    lines.append(f"| 总负债（亿元） | {_fmt_num(fq.get('total_liabilities_yi'))} |")
    lines.append(f"| 应收账款占比 | {_fmt_pct(fq.get('accounts_receivable_to_assets'))} |")
    lines.append(f"| 盈利质量预警 | {_md(fq.get('profit_quality_warn', 'N/A') or 'N/A')} |")
    lines.append(f"| 审计意见 | {_md(fq.get('audit_type', 'N/A') or 'N/A')} |")
    lines.append("")
    lines.append("**AI 解读：**")
    lines.append("")
    lines.append("---")
    lines.append("")


def _build_section6_governance(a, lines):
    """第 6 段：治理与资本配置。"""
    gv = a.get("governance", {}) or {}
    score = gv.get("score")
    max_score = gv.get("max_score")

    lines.append(f"## 【6. 治理与资本配置】—— {_md(_anchor(a))}")
    lines.append("")
    lines.append(f"**得分：{_fmt_score(score, max_score)}**")
    lines.append("")
    lines.append("**核心治理指标：**")
    lines.append("")
    lines.append("| 指标 | 数据 |")
    lines.append("|------|------|")
    lines.append(f"| 实际控制人 | {_md(gv.get('actual_controller', 'N/A') or 'N/A')} |")
    lines.append(f"| 实控人持股比例 | {_fmt_pct(gv.get('control_ratio'))} |")
    lines.append(f"| 历史分红次数 | {_fmt_num(gv.get('dividend_count'), 0) if gv.get('dividend_count') is not None else 'N/A'} 次 |")
    lines.append(f"| 最新每股分红（元） | {_fmt_num(gv.get('latest_dividend_per_share'))} |")
    div_plan = gv.get("latest_dividend_plan", "")
    if div_plan:
        lines.append(f"| 最新分红方案 | {_md(div_plan)} |")
    lines.append(f"| 是否有股权激励 | {_fmt_bool(gv.get('has_equity_incentive'))} |")
    lines.append(f"| 是否有高管减持 | {_fmt_bool(gv.get('has_insider_reduction'))} |")
    lines.append("")

    # 前 10 大股东
    top10 = gv.get("top10_shareholders", []) or []
    lines.append("**前 10 大股东：**")
    lines.append("")
    lines.append("| 排名 | 股东名称 | 持股比例 |")
    lines.append("|------|----------|----------|")
    if top10:
        for row in top10:
            rank = row.get("rank", "")
            name = row.get("name", "")
            ratio = row.get("ratio")
            lines.append(f"| {_md(rank)} | {_md(name)} | {_fmt_pct(ratio)} |")
    else:
        lines.append("| （无数据） | - | - |")
    lines.append("")

    # 分红年份
    div_years = gv.get("dividend_years", []) or []
    lines.append(f"**历史分红年份：** {', '.join(_md(y) for y in div_years) if div_years else '无'}")
    lines.append("")
    lines.append("**AI 解读：**")
    lines.append("")
    lines.append("---")
    lines.append("")


def _build_section7_risk(a, lines):
    """第 7 段：主要扣分项。"""
    risk = a.get("risk_deduction", {}) or {}
    total_deduction = risk.get("total_deduction")
    max_deduction = risk.get("max_deduction")
    risk_items = risk.get("risk_items", []) or []

    lines.append(f"## 【7. 主要扣分项】—— {_md(_anchor(a))}")
    lines.append("")
    lines.append(f"**风险扣分：{_fmt_score(total_deduction, max_deduction)}**")
    lines.append("")
    lines.append("| 扣分项 | 扣分 | 详情 |")
    lines.append("|--------|------|------|")
    if risk_items:
        for item in risk_items:
            name = item.get("item", "")
            ded = item.get("deduction")
            detail = item.get("detail", "")
            lines.append(f"| {_md(name)} | -{_fmt_num(ded, 0) if ded is not None else 'N/A'} | {_md(detail)} |")
    else:
        lines.append("| 无扣分项 | 0 | 本次评估未触发风险扣分项 |")
    lines.append("")
    lines.append("**AI 解读：**")
    lines.append("")
    lines.append("---")
    lines.append("")


def _build_section8_conclusion(a, lines):
    """第 8 段：结论。"""
    final_score = a.get("final_score")
    max_score = a.get("max_score")
    grade = a.get("grade", "N/A")

    lines.append(f"## 【8. 结论】—— {_md(_anchor(a))}")
    lines.append("")
    lines.append(f"**综合评分：{_fmt_score(final_score, max_score)}（{grade}）**")
    lines.append("")

    lines.append("**综合评价：**")
    lines.append("")
    lines.append("**AI 解读：**")
    lines.append("")
    lines.append("**值得长期跟踪吗？**")
    lines.append("")
    lines.append("**AI 解读：**")
    lines.append("")
    lines.append("**适合什么类型的投资者？**")
    lines.append("")
    lines.append("**AI 解读：**")
    lines.append("")
    lines.append("**核心跟踪指标：**")
    lines.append("")
    lines.append("| 指标 | 关注原因 |")
    lines.append("|------|----------|")
    lines.append("| （由 AI 在槽位下方补充） | |")
    lines.append("")
    lines.append("**风险提示：**")
    lines.append("")
    lines.append("**AI 解读：**")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*免责声明：本报告由公司质地评估系统自动生成，基于公开财务数据和技术面分析，仅供学习研究参考，不构成任何投资建议。股市有风险，投资需谨慎。*")
    lines.append("")


def generate_report(stk_code=None) -> str:
    """生成数值固定的 Markdown 骨架并返回完整字符串。"""
    a = _load_data(stk_code)
    lines: list = []
    _build_header(a, lines)
    _build_section1_score(a, lines)
    _build_section2_business(a, lines)
    _build_section3_competitive(a, lines)
    _build_section4_growth(a, lines)
    _build_section5_financial(a, lines)
    _build_section6_governance(a, lines)
    _build_section7_risk(a, lines)
    _build_section8_conclusion(a, lines)
    return "\n".join(lines)


def main():
    stk_code = sys.argv[1] if len(sys.argv) > 1 else None
    print(generate_report(stk_code))


if __name__ == "__main__":
    main()
