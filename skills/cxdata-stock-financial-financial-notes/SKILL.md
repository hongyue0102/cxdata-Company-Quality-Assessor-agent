---
name: stock-financial-financial-notes
description: 存储上市公司定期报告中披露的附注明细情况，并对原始披露的科目名称进行了标准化归类处理(科目代码)。主要包括：财务费用明细、收入成本明细、固定资产及无形等资产的明细、研发投入及产出数据等数据。
metadata:
  version: "1.0.0"
  author: "财新数据"
  website: "guizhi.io"
  tags: ["finance-costs", "notes-payable", "accounts-payable", "stock-financial"]
---

# 执行标准程序 (Recommended Workflow)

当用户发起查询时，AI 推荐按照以下步骤执行：

1. **Step 1: 调用统一工具**
- 使用 `python ./scripts/api_query.py <API_ID> key=value [key=value] ...` 命令获取接口数据
- 工具会自动完成：加载配置 → 获取token → 发送请求 → 解压数据 → 输出JSON结果
- **调用方式**：所有接口统一使用 key=value 格式传参

2. **Step 2: 解析结果**
- 工具输出为格式化的JSON数据，直接解析并呈现给用户

# 数据处理说明

## 配置说明
本技能所有接口需要认证token，配置方式：
1. 在 `./scripts/.env` 文件中配置 `USER_KEY` 和 `BASE_URL`
2. 调用 `./scripts/api_query.py` 时会自动获取并使用token

## 脚本功能
`./scripts/api_query.py` 脚本功能：
- 自动加载 `./scripts/.env` 配置文件
- 自动获取 `authtoken`
- 构建请求URL并发送GET请求
- 自动处理 Base64 解码和 Gzip 解压
- 输出格式化的JSON结果

# 使用场景

- 用户查询三板挂牌公司定期报告中披露的主营业务收入构成明细数据，主要包括：股票代码、股票简称、截止日期、分类方式、项目名称、本期主营业务收入、本期主营业务成本、本期主营业务利润、上期主营业务利润等
- 用户查询上市公司定期报告中披露的资产负债表相关附注明细情况，并对原始披露的科目名称进行了标准化归类处理(科目代码)。主要包括：股票代码、股票简称、截止日期、报表合并标志、科目名称、期末金额等。科目类别包括：货币资金、应付票据、应付账款、交易性金融资产等
- 用户查询上市公司定期报告中披露的固定资产及无形等资产的明细情况，主要包括：股票代码、股票简称、截止日期、报表合并标志、资产的原值、累计折旧、减值准备、账面价值、净值等各项的期初、期间变化和期末数据等
- 用户查询上市公司定期报告中披露的财务费用明细构成数据，主要包括：股票代码、股票简称、截止日期、报表合并标志、利息支出、利息收入、汇兑损益、手续费及其他等
- 用户查询上市公司公告中披露的工业产权等无形资产相关的数据，主要包括：股票代码、股票简称、无形资产类别、名称、所有权归属、取得或使用方式、项目具体说明等
- 用户查询上市公司定期报告中披露的研发投入及产出数据，主要包括：股票代码、股票简称、截止日期、报表合并标志、费用化研发投入、资本化研发投入、研发人员数量等
- 用户查询上市公司定期报告中披露的收入成本明细，主要包括：股票代码、股票简称、截止日期、报表合并标志、分类方式、项目名称、主营业务收入、主营业务成本、主营业务利润、毛利率等
- 用户查询上市公司定期报告中披露的非经常性损益数据，主要包括：股票代码、股票简称、截止日期、报表合并标志、项目名称、项目类别、金额、计价货币等
- 用户查询上市公司定期报告中披露的利润分配表附注的明细情况，主要包括：股票代码、股票简称、截止日期、报表合并标志、科目名称、金额等。科目类别包括：管理费用、税金及附加、销售费用、研发费用等



## 调用方式

所有接口统一使用 `api_query.py` 工具调用，参数采用 `key=value` 格式：

```bash
python ./scripts/api_query.py <API_ID> key=value [key=value] ...
```

## 接口清单
> ⚠️ **注意事项**：
> 1. 所有接口输入输出需要严格按照接口文档规范
> 2. 所有接口标识必须严格按照 API_ID 进行请求，不得杜撰不存在的接口
> 3. 调用接口之前必须阅读接口文档

| 接口名称 | 接口文档 | API_ID | 接口描述 |
|----------|----------|--------|----------|
| 三板主营收入构成-通用 | ./references/getStkLcNqMainoperincByCond-G.md | getStkLcNqMainoperincByCond-G | 存储三板挂牌公司定期报告中披露的主营业务收入构成明细数据，主要包括：股票代码、股票简称、截止日期、分类方式、项目名称、本期主营业务收入、本期主营业务成本、本期主营业务利润、上期主营业务利润等。 |
| 上市公司主营业务构成-通用 | ./references/getComFinNoteMainBusiByCond-G.md | getComFinNoteMainBusiByCond-G | 存储上市公司定期报告中披露的收入成本明细，主要包括：股票代码、股票简称、截止日期、报表合并标志、分类方式、项目名称、主营业务收入、主营业务成本、主营业务利润、毛利率等。 |
| 上市公司利润分配表附注_通用-通用 | ./references/getComFinNoteAndIncomeByCond-G.md | getComFinNoteAndIncomeByCond-G | 存储上市公司定期报告中披露的利润分配表附注的明细情况，主要包括：股票代码、股票简称、截止日期、报表合并标志、科目名称、金额等。科目类别包括：管理费用、税金及附加、销售费用、研发费用等。 |
| 上市公司固定及无形等资产明细-通用 | ./references/getComFinNoteFixIntAsseByCond-G.md | getComFinNoteFixIntAsseByCond-G | 存储上市公司定期报告中披露的固定资产及无形等资产的明细情况，主要包括：股票代码、股票简称、截止日期、报表合并标志、资产的原值、累计折旧、减值准备、账面价值、净值等各项的期初、期间变化和期末数据等。 |
| 上市公司研发投入与产出明细-通用 | ./references/getComFinNoteRdProdByCond-G.md | getComFinNoteRdProdByCond-G | 存储上市公司定期报告中披露的研发投入及产出数据，主要包括：股票代码、股票简称、截止日期、报表合并标志、费用化研发投入、资本化研发投入、研发人员数量等。 |
| 上市公司资产负债表附注_通用-通用 | ./references/getComFinNoteBalaTacbbByCond-G.md | getComFinNoteBalaTacbbByCond-G | 存储上市公司定期报告中披露的资产负债表相关附注明细情况，并对原始披露的科目名称进行了标准化归类处理(科目代码)。主要包括：股票代码、股票简称、截止日期、报表合并标志、科目名称、期末金额等。科目类别包括：货币资金、应付票据、应付账款、交易性金融资产等。 |
| 上市公司非经常性损益明细-通用 | ./references/getComFinNoteProfAndLossByCond-G.md | getComFinNoteProfAndLossByCond-G | 存储上市公司定期报告中披露的非经常性损益数据，主要包括：股票代码、股票简称、截止日期、报表合并标志、项目名称、项目类别、金额、计价货币等。 |
| 主营业务与产品_工业产权等无形资产-通用 | ./references/getStkLcIntangibleassetByCond-G.md | getStkLcIntangibleassetByCond-G | 存储上市公司公告中披露的工业产权等无形资产相关的数据，主要包括：股票代码、股票简称、无形资产类别、名称、所有权归属、取得或使用方式、项目具体说明等。 |
| 财务费用-通用 | ./references/getD2StkFinNoteFinColByCond-G.md | getD2StkFinNoteFinColByCond-G | 存储上市公司定期报告中披露的财务费用明细构成数据，主要包括：股票代码、股票简称、截止日期、报表合并标志、利息支出、利息收入、汇兑损益、手续费及其他等。 |



### API_ID 参数

- `API_ID` 用于指定要调用的具体接口，根据查询类型选择
- 示例API_ID：
- `getStkLcNqMainoperincByCond-G`: 三板主营收入构成-通用
- `getComFinNoteMainBusiByCond-G`: 上市公司主营业务构成-通用
- `getComFinNoteAndIncomeByCond-G`: 上市公司利润分配表附注_通用-通用
- 更多API_ID请参考接口[接口清单](#接口清单)

## 故障排除

- **调用失败**：检查 `./scripts/.env` 文件是否存在并正确配置了 `CXDA_USER_KEY` 和 `BASE_URL`，确认网络连接正常，token未过期。
- **输出为空**：确认输入参数是否正确，检查API_ID是否匹配查询类型。
- **权限问题**：接口返回无权限或者权限到期时，提示用户前往`https://yun.ccxe.com.cn/`联系客服
- **scripts路径问题**：文档中描述的是skill相对路径，请求时确认路径是否正确
- **相同含义字段说明**：ORG_UNI_CODE==COM_UNI_CODE;STK_UNI_CODE==BOND_UNI_CODE；如无明确说明股票代码不需要携带SH、HK等交易所代码
- **接口输入字段不明确**：接口输入参数是ORG_UNI_CODE、STK_UNI_CODE等参数时可以先通过对应的基础接口调用尝试获取，获取不到时反馈并停止
- **其他异常**：出现其他异常时停止输出并返回异常原因
