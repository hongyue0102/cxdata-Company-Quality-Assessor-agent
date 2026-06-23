#!/usr/bin/env python3
"""
公司质地打分 - 数据获取脚本
拉取 analyze_data.py 所需的全部数据（~25 个 API 调用）。

使用方式：
    python fetch_data.py <股票代码>
    示例: python fetch_data.py 300475

输出目录：data/

鉴权说明：
    本脚本通过 subprocess 调用同目录下的 query.py（cxdata 官方统一查询工具）。
    认证状态由 query.py 自动管理（读取 ~/.cxda-cache/.shared/cxda_auth.json）。
    若未认证，query.py 会返回错误，需先由 Agent 引导用户完成 auth.py 鉴权流程。
"""

import json
import re
import subprocess
import sys
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
_QUERY_SCRIPT = SCRIPT_DIR / "query.py"

# 控制字符与换行（防日志/print 注入）
_CONTROL_RE = re.compile(r"[\r\n\t\x00-\x1f\x7f]")


def _safe_log(value) -> str:
    """净化用于 print/日志的字段，剥离换行等控制字符，防止伪造日志条目"""
    if value is None:
        return ""
    return _CONTROL_RE.sub(" ", str(value))

# ========== 业务接口（硬编码，只允许以下接口） ==========

_ALLOWED_APIS = frozenset([
    "getDPubComInfo1ByCond-G",          # 基本信息
    "getPubComInfoByCond-G",            # 公司简介
    "getStkBasicInfoByCond-G",          # 个股基本信息（取上市日期，用于次新股判定）
    "getComFinMainIndxByCond-G",        # 主要会计数据
    "getDComAuditOpinNewByCond-G",      # 审计意见
    "getDComProfMakeQatByCond-G",       # 盈利质量预警
    "getComFinNoteMainBusiByCond-G",    # 主营构成
    "getComFinNoteBalaTacbbByCond-G",   # 资产负债表附注
    "getComFinNoteProfAndLossByCond-G", # 非经常性损益
    "getStkFinIndexInduRankByCond-G",   # 行业排名
    "getStkInduFinIndexByCond-G",       # 行业平均
    "getDComHldActuContlrByCond-G",     # 实控人
    "getDComTenHldByCond-G",            # 十大股东
    "getDComSharePleByCond-G",          # 股权质押
    "getDComDivPlanByCond-G",           # 分红方案
    "getDComDivImplByCond-G",           # 分红实施
    "getDComInceMainByCond-G",          # 股权激励
    "getDComDirHoldstkChanByCond-G",    # 董事增减持
    "getDManHoldstkChanByCond-G",       # 高管增减持
    "getDComRelaTradeByCond-G",         # 关联交易
])


def _run_query(api_id: str, params: dict) -> dict:
    """单次 subprocess 调用 query.py api。返回解析后的 dict（含原始 status 字段）。"""
    cmd = [sys.executable, str(_QUERY_SCRIPT), "api", api_id]
    for k, v in params.items():
        cmd.append(f"{k}={v}")

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=120,
        cwd=str(SCRIPT_DIR),
    )
    if result.returncode != 0:
        raise RuntimeError(f"query.py 退出码 {result.returncode}, stderr: {result.stderr[:200]}")
    stdout = result.stdout.strip()
    if not stdout:
        raise RuntimeError("query.py 无输出")
    return json.loads(stdout)


def _session_confirm():
    """调用 query.py session confirm，解除 50 次限制阻断。"""
    cmd = [sys.executable, str(_QUERY_SCRIPT), "session", "confirm"]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30, cwd=str(SCRIPT_DIR))
    if result.returncode != 0:
        raise RuntimeError(f"session confirm 失败: {result.stderr[:200]}")


def call_api(api_id: str, params: dict) -> dict:
    """通过 query.py 调用业务接口（仅允许 _ALLOWED_APIS 中的接口）。

    query.py 内部处理：认证、token 缓存、gzip+base64 解码、积分计数、50 次限制。
    触发 50 次限制时自动调 session confirm 解除阻断并重试一次（批量取数场景）。
    返回的 dict 与原 HTTP 直连版本兼容：含 code/result/totalCount 等字段。
    """
    if api_id not in _ALLOWED_APIS:
        print(f"  [ERROR] 不允许的接口: {api_id}")
        return {"code": "error", "result": [], "totalCount": 0}

    try:
        data = _run_query(api_id, params)

        # 50 次限制触发：自动 confirm 后重试一次
        if data.get("status") == "confirmation_required":
            print(f"  [AUTO-CONFIRM] {api_id}: 触发 50 次限制，自动 confirm 后重试")
            _session_confirm()
            data = _run_query(api_id, params)

        # 认证失败不重试
        if data.get("status") in ("failed", "terms_not_accepted"):
            msg = data.get("error", "未知错误")
            print(f"  [ERROR] {api_id}: {msg}")
            return {"code": "error", "result": [], "totalCount": 0,
                    "status": data.get("status")}

        return data
    except json.JSONDecodeError as e:
        print(f"  [ERROR] {api_id}: 响应解析失败 {e}")
        return {"code": "error", "result": [], "totalCount": 0}
    except subprocess.TimeoutExpired:
        print(f"  [ERROR] {api_id}: 调用超时（120s）")
        return {"code": "error", "result": [], "totalCount": 0}
    except Exception as e:
        print(f"  [ERROR] {api_id}: {e}")
        return {"code": "error", "result": [], "totalCount": 0}


def fetch_all_pages(api_id: str, params: dict, page_size: int = 20) -> list:
    """自动分页拉取全部数据。"""
    all_results = []
    page = 1
    total = None

    while True:
        params_copy = {**params, "pageNum": str(page), "pageSize": str(page_size)}
        data = call_api(api_id, params_copy)
        results = data.get("result", [])

        if not results:
            if page == 1:
                time.sleep(2)
                data = call_api(api_id, params_copy)
                results = data.get("result", [])
                if not results:
                    break
            else:
                break

        all_results.extend(results)

        if page == 1:
            tc = data.get("totalCount")
            if tc is not None:
                total = int(tc)

        if total is not None and len(all_results) >= total:
            break
        if len(results) < page_size:
            break

        page += 1
        time.sleep(1)

    return all_results


OUTPUT_DIR = SCRIPT_DIR / "data"


def save(filename: str, data):
    with open(OUTPUT_DIR / filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    count = len(data) if isinstance(data, list) else 1
    print(f"  {filename} ({count} 条)")


def main():
    if len(sys.argv) < 2:
        print("用法: python fetch_data.py <股票代码>")
        sys.exit(1)

    raw_code = sys.argv[1].strip()
    stk_code = _safe_log(raw_code.split(".")[0])
    t_start = time.time()

    print(f"=== 公司质地打分 - 精简取数 ===")
    print(f"股票代码: {stk_code}")

    OUTPUT_DIR.mkdir(exist_ok=True)

    # ===== 步骤1: 基本信息 =====
    print("\n[1/9] 基本信息...")

    company_info = {}
    for attempt in range(3):
        company_info = call_api("getDPubComInfo1ByCond-G",
                                {"stkCode": stk_code, "pageNum": "1", "pageSize": "5"})
        if company_info.get("result"):
            break
        print(f"  [RETRY] company_info 第{attempt+1}次失败...")
        time.sleep(5)
    save("company_info.json", company_info.get("result", []))

    company_name = ""
    sw_industry = ""
    if company_info.get("result"):
        r = company_info["result"][0]
        company_name = r.get("COM_CHI_NAME", "")
        sw_industry = r.get("INDU_CLASS_NAME_S", "") or r.get("INDU_CLASS_NAME_Q", "")

    # 公司简介
    if company_name:
        profile = fetch_all_pages("getPubComInfoByCond-G",
                                  {"comChiName": company_name})
        save("company_profile.json", profile)
    else:
        save("company_profile.json", [])

    # 上市日期（用于次新股判定：上市不足1年豁免分红项）
    list_date = ""
    try:
        stk_basic = call_api("getStkBasicInfoByCond-G", {"stkCode": stk_code})
        if stk_basic.get("result"):
            list_date = stk_basic["result"][0].get("LIST_DATE", "") or ""
    except Exception as e:
        print(f"  [WARN] 上市日期获取失败: {e}")
    save("list_date.json", [{"LIST_DATE": list_date}] if list_date else [])

    print(f"  公司: {_safe_log(company_name)}, 行业: {_safe_log(sw_industry)}, 上市日期: {_safe_log(list_date) or '未知'}")

    meta = {
        "stk_code": stk_code,
        "company_name": company_name,
        "sw_industry": sw_industry,
        "fetch_time": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
    save("meta.json", [meta])

    # ===== 步骤2: 主要会计数据（行业地位/成长/财务质量/风险扣分 共用） =====
    print("\n[2/9] 主要会计数据...")

    main_acct = fetch_all_pages("getComFinMainIndxByCond-G",
                                {"stkCode": stk_code})
    save("main_accounting_data.json", main_acct)

    # 审计意见
    audit = fetch_all_pages("getDComAuditOpinNewByCond-G",
                            {"stkCode": stk_code})
    save("audit_opinion.json", audit)

    # ===== 步骤3: 财务指标（盈利质量预警） =====
    print("\n[3/9] 财务指标...")

    data = fetch_all_pages("getDComProfMakeQatByCond-G",
                           {"stkCode": stk_code, "sheetMarkPar": "1"})
    save("indicator_profit_quality.json", data)

    # ===== 步骤4: 主营构成 + 财务附注（商业模式/财务质量/风险扣分） =====
    print("\n[4/9] 主营构成与附注...")

    mb_data = fetch_all_pages("getComFinNoteMainBusiByCond-G",
                              {"stkCode": stk_code, "endDate": "2024-12-31", "sheetMarkPar": "1"})
    save("main_business_breakdown.json", mb_data)

    # 资产负债表附注（应收账款等），只拉最新一期
    latest_end_date = main_acct[0].get("END_DATE", "") if main_acct else ""
    bal_params = {"stkCode": stk_code}
    if latest_end_date:
        bal_params["endDate"] = latest_end_date
    bal_notes = fetch_all_pages("getComFinNoteBalaTacbbByCond-G",
                                bal_params)
    save("balance_sheet_notes.json", bal_notes)

    # 非经常性损益，只需最近几年年报（一页60条足够）
    nr_data = call_api("getComFinNoteProfAndLossByCond-G",
                       {"stkCode": stk_code, "sheetMarkPar": "1", "pageNum": "1", "pageSize": "60"})
    save("non_recurring.json", nr_data.get("result", []))

    # ===== 步骤5: 行业排名（行业地位章节） =====
    print("\n[5/9] 行业排名...")

    if sw_industry:
        rank_data = call_api("getStkFinIndexInduRankByCond-G",
                             {"stkCode": stk_code, "pageNum": "1", "pageSize": "40"})
        save("industry_ranking.json", rank_data.get("result", []))

        avg_data = fetch_all_pages("getStkInduFinIndexByCond-G",
                                   {"induClassName": sw_industry})
        save("industry_average.json", avg_data)
    else:
        print("  [WARN] 未获取到申万行业名，跳过行业排名")
        save("industry_ranking.json", [])
        save("industry_average.json", [])

    # ===== 步骤6: 股东与股权（治理章节） =====
    print("\n[6/9] 股东与股权...")

    # 实控人
    controller = fetch_all_pages("getDComHldActuContlrByCond-G",
                                 {"stkCode": stk_code})
    save("actual_controller.json", controller)

    # 十大股东，只需最新一期（一页足够）
    top10 = call_api("getDComTenHldByCond-G",
                     {"stkCode": stk_code, "pageNum": "1", "pageSize": "20"})
    save("top10_shareholders.json", top10.get("result", []))

    # 股权质押
    pledge = fetch_all_pages("getDComSharePleByCond-G",
                             {"stkCode": stk_code})
    save("share_pledge.json", pledge)

    # ===== 步骤7: 分红与激励（治理章节） =====
    print("\n[7/9] 分红与激励...")

    dividend_plan = fetch_all_pages("getDComDivPlanByCond-G",
                                    {"stkCode": stk_code})
    save("dividend_plan.json", dividend_plan)

    dividend_impl = fetch_all_pages("getDComDivImplByCond-G",
                                    {"stkCode": stk_code})
    save("dividend_implementation.json", dividend_impl)

    incentive = fetch_all_pages("getDComInceMainByCond-G",
                                {"stkCode": stk_code})
    save("equity_incentive.json", incentive)

    # ===== 步骤8: 公司治理（治理章节） =====
    print("\n[8/9] 公司治理...")

    # 董事增减持
    dir_changes = fetch_all_pages("getDComDirHoldstkChanByCond-G",
                                  {"stkCode": stk_code})
    save("director_share_changes.json", dir_changes)

    # 高管增减持
    man_changes = fetch_all_pages("getDManHoldstkChanByCond-G",
                                  {"stkCode": stk_code})
    save("management_share_changes.json", man_changes)

    # ===== 步骤9: 风险扣分数据 =====
    print("\n[9/9] 风险扣分...")

    # 关联交易明细，只需最近2-3期（一页60条足够）
    rt_data = call_api("getDComRelaTradeByCond-G",
                       {"stkCode": stk_code, "pageNum": "1", "pageSize": "60"})
    save("related_trade.json", rt_data.get("result", []))

    # ===== 完成 =====
    elapsed = time.time() - t_start
    print(f"\n=== 取数完成！{stk_code}, 耗时: {elapsed:.0f}s ===")

    # 统计
    zero_files = []
    total_files = 0
    for f in sorted(OUTPUT_DIR.glob("*.json")):
        if f.name == "analysis.json":
            continue
        total_files += 1
        with open(f, encoding="utf-8") as fh:
            data = json.load(fh)
            if isinstance(data, list) and len(data) == 0:
                zero_files.append(f.name)
    print(f"数据文件: {total_files} 个，其中 0 条: {len(zero_files)} 个")
    if zero_files:
        print(f"  缺失: {', '.join(zero_files)}")


if __name__ == "__main__":
    main()
