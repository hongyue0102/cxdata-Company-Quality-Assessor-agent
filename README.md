# cxdata-Company-Quality-Assessor-agent

A股公司质地评估专家 Agent，自动拉取公司财务、股东、治理等数据，按六维评分框架生成八段式质地评估报告。

## 使用方式

### ✅ 规范指令（推荐使用，AI 稳定路由到本 Agent）

| 指令 | 说明 |
|---|---|
| `分析 600584 的公司质地` | 代码 + "公司质地" |
| `评估 300475 这家公司` | 代码 + "评估" |
| `帮我看看 002156 质地怎么样` | 代码 + "质地怎么样" |
| `华域汽车基本面怎么样` | 名称 + "基本面" |
| `宁德时代这家公司怎么样` | 名称 + "这家公司怎么样" |
| `用公司质地agent评估 600584` | 直接点名 agent |

**关键要素**：指令中必须包含 **股票代码（6位数字）** 或 **具体公司名称**，并配合"质地/基本面/评估/这家公司怎么样"等基本面意图词。

Agent 会自动：鉴权 → 拉取数据（财务/股东/治理/分红等）→ 结构化评分 → 生成数值固定骨架 → LLM 在槽位填字 → 保存报告（八段式长报告，约 5-10 分钟）。

### ❌ 容易误路由的指令（请避免使用）

以下指令**未指定具体股票**或**意图不属于基本面**，会触发其他 agent 或导致 AI 反问，**不要这样调用本 agent**：

| ❌ 模糊/越界指令 | ⚠️ AI 可能误调用的对象 |
|---|---|
| `看看这家公司` / `分析下` | 不知分析哪家，触发反问 |
| `这股票能不能买` | 意图不清（技术面？基本面？），触发反问 |
| `分析下 600519` （无"质地/基本面"词）| 可能误调技术分析 agent |
| `今天行情怎么样` | 误调主线分析 agent / 通用行情 |
| `今日主线` | 误调主线分析 agent |
| `600519 现在能买吗` / `K线怎么样` | 误调技术分析 agent（属技术面/择时）|
| `分析下电子板块` | 误调板块分析 agent |
| `帮我选几只股票` | 误调选股 agent |

> 如果使用了上述模糊指令，AI 会主动反问澄清，但会多一次交互——建议直接用规范指令。

### 🔀 与其他 agent 的边界（避免重复调用）

| 用户需求 | 应调用 |
|---|---|
| **A 股单只个股的公司质地评估**（财务/治理/分红/长期价值，八段式报告）| **本 agent**（公司质地） |
| A股市场整体主线 / 板块强弱对比 / 情绪周期 | cxdata-mainline-analysis-agent |
| 个股技术面分析（K线/均线/MACD/RSI/量能）| cxdata-stock-analysis-agent |
| 单一板块的深度分析（如只看电子）| 板块分析 agent |
| 多只股票对比 / 选股 / 排序 | 选股 agent |
| 港股 / 美股 / 期货 / 加密货币 | 对应市场 agent |
| 回测 / 策略 / 仓位管理 | 策略类 agent |

### 💡 与股票技术分析 agent 的区别（重要）

两者都需要股票代码，但职责完全不同：

| 维度 | 本 agent（公司质地）| 股票分析 agent（技术面）|
|---|---|---|
| **视角** | 基本面、长期价值 | 技术面、短期择时 |
| **回答的问题** | "这家公司好不好？值不值得长期持有？" | "现在能买吗？K线形态怎么样？" |
| **数据** | 财报、股东、治理、分红 | K线、均线、MACD、量能 |
| **报告** | 八段式长报告 | 技术面短报告 |

## 前置依赖

1. 安装 Python 依赖：`pip install python-dotenv requests`
2. 首次使用需完成鉴权（**新版 SMS 验证码登录机制**）：
   - 调用 `skills/company-quality/scripts/auth.py status` 检查认证状态
   - 未认证时按 AGENT.md 引导用户完成协议确认 + 手机号验证码登录
   - 认证信息持久化在 `~/.cxda-cache/.shared/cxda_auth.json`，**跨所有 cxdata Agent 共享**，无需重复认证
   - 数据源 Skill 已内置在 Agent 中，无需额外下载

## 目录结构

```
cxdata-Company-Quality-Assessor-agent/
├── AGENT.md                                       # Agent 整体人设与执行逻辑
├── SOUL.md                                        # 身份、性格、能力边界
├── rules.md                                       # 硬性规则
├── config.json                                    # 元数据配置
├── skills/
│   ├── company-quality/                           # 主分析 Skill
│   │   ├── SKILL.md
│   │   └── scripts/
│   │       ├── fetch_data.py                      # 数据获取（subprocess 调 query.py）
│   │       ├── analyze_data.py                    # 结构化评分（六维 + 风险扣分）
│   │       ├── generate_report.py                 # 输出数值固定的 Markdown 骨架（8 段式）
│   │       ├── auth.py / common.py /              # cxdata 官方鉴权四件套
│   │       ├── cxda_cache_cli.py / query.py
│   │       ├── requirements.txt
│   │       └── data/                              # 中间数据（自动生成，.gitignore 排除）
│   ├── cxdata-stock-basic-information/            # 内置数据源（空壳：SKILL.md + references）
│   ├── cxdata-company-profile/                    # 内置数据源（空壳）
│   ├── cxdata-stock-financial-financial-statement/
│   ├── cxdata-stock-financial-indicator/
│   ├── cxdata-stock-financial-financial-notes/
│   ├── cxdata-stock-financial-industry-statistics/
│   ├── cxdata-stock-shareholder-share/
│   ├── cxdata-stock-financing-dividends/
│   ├── cxdata-stock-equity-incentive/
│   ├── cxdata-stock-material-matters-shareholding-reform/
│   └── cxdata-stock-governance-structure/
└── README.md
```

## 评分体系（满分100）

| 维度 | 满分 | 说明 |
|------|------|------|
| 行业地位 | 25 | 营收排名百分位(10) + ROE排名百分位(10) + 竞争优势(5) |
| 商业模式 | 20 | 收入集中度(15) + 毛利率(5) |
| 成长质量 | 20 | 营收增速(6) + 利润增速(6) + 可持续性(4) + 提质增长(4) |
| 财务质量 | 15 | ROE(4) + 资产负债率(4) + 现金流质量(4) + 预警扣分 |
| 公司治理 | 10 | 控制权结构(3) + 分红(3) + 激励(1) + 审计(3) |
| 风险扣分 | -10 | 关联交易、非经常性损益、盈利质量预警、高负债等 |

## 报告格式（八段式）

1. 质地总评分
2. 商业模式与壁垒
3. 行业地位与竞争优势
4. 成长质量
5. 财务质量
6. 治理与资本配置
7. 主要扣分项
8. 结论

## 变更历史

### 2026-07-13 行业排名口径统一 + 接口积分优化

**行业排名口径统一：**
- `analyze_competitive_position()` 优先按公司所属行业名（`sw_industry`）匹配排名记录，不再取 END_DATE 最大的（碰巧取到一级"电子"506家公司），修正为三级"半导体设备"25家公司
- 报告标签从"行业 ROE（加权平均）"改为"行业 ROE（加权平均·{行业名}）"，明确数据来源行业级别

**接口积分优化（33次/1290积分 → 约15-18次/420-540积分，降幅约60%）：**
- 剔除冗余接口：移除 `getStkInduFinIndexByCond-G`（industry_average.json），该数据加载后从未被使用，省 4 次/200 积分
- 行业衍生指标精简取数：`getStkFinDeriIndexInduByCond-G` 从 `fetch_all_pages`（拉全量 230 条 / 12 次/600 积分）改为 `call_api` + `endDate` 筛选最新年报（1 次/50 积分）
- 全面 `fetch_all_pages` → `call_api`：审计意见、公司简介、实控人、分红预案/实施、股权激励、董事/高管增减持、主营构成、资产负债表附注、盈利质量指标等接口，从 `fetch_all_pages`（会翻页检查多调用）改为 `call_api`（单页精确取数），避免不必要的翻页请求
- `latest_annual_date` 计算提前至步骤2末尾，供步骤3/4/5共用

### 2026-07-13 行业 ROE 口径修正 + 质押指标剔除 + 报告锚点优化

**行业 ROE 口径修正（与产品端对齐）：**
- 行业 ROE 数据源从 `getStkInduFinIndexByCond-G` 的 `INDU_ROE`（行业汇总口径：总利润/总净资产）切换为 `getStkFinDeriIndexInduByCond-G` 的 `ROE_WEI`（加权平均净资产收益率），与产品端数据口径一致
- 行业级别从申万三级行业改为申万二级行业，自动从行业排名数据中提取 `INDU_LEVEL=2` 的行业名
- 报告标签从"行业平均 ROE"改为"行业 ROE（加权平均）"

**质押指标剔除：**
- 剔除质押评分（`pledge_score`）和质押展示（"质押记录数"行），因数据源无法区分质押与解押，累计数据不能反映当前质押情况
- 治理模块满分 10 分重新分配：ctrl(3) + div(3) + incentive(1) + audit(3)，audit 从 2 分调至 3 分
- 删除 `fetch_data.py` 中股权质押取数步骤，`share_pledge.json` 不再生成
- AGENT.md 禁止事项中删除 `pledge_count`，治理指标单位删除"条"

**报告锚点优化：**
- 每个段落标题追加公司简称+代码锚点（如"—— 金海高科（603311）"），防止 AI 解读时混淆名称相似的公司
- AI 解读约束从报告正文移至 AGENT.md 禁止事项第 6 条，不再出现在报告输出中

### 2026-07-02 修复多处 API 字段名错误与数据逻辑问题

对照 API references 文档逐字段核查，修复因字段名写错、单位理解错误、硬编码等导致的数据错误：

**字段名错误（对照 API 文档修正）：**
- 质押：`PLE_VOL`（十大股东接口字段）→ `PLE_SHARE`（质押接口字段），并排除"解除质押"记录
- 分红：`DIV_RMB`/`DIV_TAX_RMB` 是"每10股"金额，未除以10导致每股分红虚高10倍
- 董监高变动：`INDIV_NAME`→`LEAD_NAME`、`CHAN_VOL`→`CHAN_HOLD_VOL`、`CHAN_REAS_PAR`→`CHAN_REAS_DES`

**数据截断问题：**
- 前十大股东 `[:5]`→`[:10]`（只显示了5个）
- 收入结构 `by_industry[:5]`/`by_region[:3]`→去掉截断（数据不完整）
- 高管减持判断 `recent_changes[:5]`→遍历全部（可能漏判减持）

**硬编码/逻辑问题：**
- 主营构成 `endDate: "2024-12-31"`→动态取最新年报日期
- 财务质量/风险扣分中"最新资产负债率"混用季报→统一用年报，删除冗余字段
- 报告"主营业务"行内容超长导致表格列宽问题→移出表格单独显示

**新增：**
- 新增"最新分红方案"字段（如"10转增4.5股派3.8元(含税)"）
- AGENT.md 添加编码前置规则：修改 API 相关代码前必须先读 references 文档

**清理：**
- 删除报告未使用的输出字段：scoring、pledge_details、top10_pledge、insider_trading、audit_firms、is_new_stock、list_date、business_scope、revenue_by_product、core_products

### 2026-06-29 硬编码凭证：cred_crypto 密钥派生退化检测（同步主线）

cred_crypto.py 与主线同源（差异 0），`_derive_key()` 在 host/user 全空（容器环境）时退化成固定弱密钥。同步主线修复：host/user 均空时拒绝生成密钥。三 agent 同步。

### 2026-06-29 路径遍历补漏：list_files / _get_skill_path 的 skill_name 校验（同步主线）

火山扫描报 `cxda_cache_cli.py` 的 `list_files()`/`_get_skill_path()` 未校验 skill_name（`../etc` 可列出/创建任意目录）。此前只加固了 `_get_file_path`。同步主线修复：新增 `_SAFE_NAME_RE` + `_validate_skill_name()`，`_get_skill_path`/`list_files`/`_get_file_path` 三入口统一校验。

**验证**：语法通过；8 个路径遍历变体全拦截，合法名不误伤

### 2026-06-28 对照火山扫描清单全面加固 + 四件套与主线/股票 agent 对齐

对照火山扫描清单（包体合规/人设/权限/代码安全/内容安全）逐项核查，公司质地 agent 此前只做了 1 项加固（cred_crypto 硬依赖），其余 7 项缺失。本次将核心四件套与主线/股票 agent 已验证的加固版对齐（认证机制同为 SMS、渠道码同为 CAXEN，代码同源），一次性获得全部 8 轮安全加固成果：

**代码安全（替换为统一加固版）**：
- `auth/common/query/cxda_cache_cli/cred_crypto` 与主线 agent 逐字对齐
- 覆盖：cred_crypto 硬依赖、env RCE（拒 `..`/绝对路径/PYTHON 文件名校验）、凭证经 stdin 传递、SSRF path 规范化（unquote+normpath）、parse_params 黑名单归一化、_validate_api_id 白名单、私域 write 0o600+O_NOFOLLOW（TOCTOU）、auth 改 POST（phone/code 不进 query）

**包体合规（对照清单【1001/1005】）**：
- 移除全部 `_archive/`（34 个文件，含 11 个 `auth.sh` —— 火山【1001】可执行文件红线），`.gitignore` 新增 `**/_archive/`（本地保留归档，不进交付包）
- `.env` 早已被 `.gitignore` 排除，无硬编码凭证

**文档同步**：`AGENT.md` 认证调用改 stdin（JSON），与前两个 agent 一致

**验证**：5 文件语法通过；安全加固 8 项核查全到位；变体自测（parse_params 大小写、api_id 路径遍历、env `..`、SSRF `../admin`）全过；query/auth 各命令 argparse 正常；fetch_data 经 subprocess 调 query.py 取数链路兼容

### 2026-06-25 对齐同事官方积分机制 + B股排除 + 安全加固 + venv 环境

对齐 cxdata 另两个 agent（主线/股票分析），统一采用同事 6-24 官方积分机制，补齐安全加固与 B 股排除。

**积分机制（对齐同事官方四件套）：**
- 覆盖 query/common/cxda_cache_cli/auth 为同事 6-24 官方版
- 记账改 `append_shared_text` 追加 `cxda_session_calls.jsonl`，天然并发安全无需锁；session_id 会话隔离
- fetch_data 加 session start/summary 规范流程，积分以 session summary 为准
- 验证：完整取数 jsonl 记账 38 次调用 / 1150 积分

**B 股排除：**
- fetch_data.py main 入口加 B 股校验（900/200 开头拒绝），仅分析 A 股

**安全加固（叠加在同事四件套上，与前两个 agent 一致）：**
- SSRF url 白名单、filename 校验、凭证加密（cred_crypto）、文件权限 0o600/0o700、异常脱敏、workspace 校验、cli 路径遍历防护、api_main 白名单

**环境：**
- 新建 .venv 并安装 cryptography/requests/pandas/python-dotenv（凭证加密依赖 cryptography）
- AGENT.md 加「环境准备」说明，所有 python3 命令用 `.venv/bin/python3`

### 2026-06-17 新增 Agent 路由边界与用户使用指引

- **问题**：新设备测试时，AI 在用户指令模糊（如"看看这家公司"、"这股票能不能买"）或指令只有代码没有"质地/基本面"关键词（如"分析下 600519"）时，会误调用主线分析 / 技术分析 / Wind 等其他 agent，导致公司质地 agent 失效或答非所问
- **方案**：
  - **AGENT.md** 顶部新增 Step 0「适用边界判定」：明确 ✅ 命中条件（代码/名称 + 质地/基本面意图）/ ❌ 让出场景（特别是与股票技术分析 agent 的边界）/ ⚠️ 模糊指令强制反问
  - **SKILL.md** description 收紧为"仅处理 A股单只个股的公司质地评估"，并在顶部加路由判断清单
  - **README.md** 使用方式段重写：✅ 规范指令 + ❌ 误路由指令 + 🔀 与其他 agent 边界 + 💡 与技术分析 agent 的区别表

### 2026-06-17 鉴权升级 + 数值固定骨架（与 stock-analysis / mainline-analysis 同构）

- **fetch_data.py** 改为 subprocess 调用官方 `query.py`（内置 token 管理、gzip 解码、积分计数、50 次硬限制），不再调各 skill 的 `api_query.py`
- 新增 `auth.py / common.py / cxda_cache_cli.py / query.py`（拷自新版 cxdata-stock-market-information skill）
- **AGENT.md** 加 Step 1.5 鉴权前置（terms-check + status + SMS 引导）+ Step 2/2.5 session start/summary
- **generate_report.py** 从「输出 prompt + JSON dump」改为「输出数值固定的 Markdown 骨架」，所有表格/数值/字段名由 Python 写死，LLM 只在「**AI 解读：**」槽位填字（参照 cxdata-stock-analysis-agent/analyzer.py 模式）
- **rules.md / AGENT.md** 加数值固定禁止事项：禁止篡改 Python 计算的数值、禁止修改骨架结构、禁止编造数据
- 11 个数据源 skill 目录改名为 `cxdata-` 前缀，`scripts/` 清空（老 `api_query.py / .env / auth.sh` 归档到各自 `_archive/old-scripts/`，避免 LLM 看到通用脚本乱调接口）
- 删除主 skill 老 `.env / .env.example / prompts/`（鉴权改为 `~/.cxda-cache/` 共享缓存）

## 免责声明

本 Agent 基于公开财务数据进行分析，不构成任何投资建议。股市有风险，投资需谨慎。
