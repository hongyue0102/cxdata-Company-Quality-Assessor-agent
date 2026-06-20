# 上市公司研发投入与产出明细-通用 (getComFinNoteRdProdByCond-G)

**API_ID:** getComFinNoteRdProdByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| endDate | 截止日期 | 日期类型 | 否 |  |
| sheetMarkPar | 报表合并标志 | 数值类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| INFO_PUB_DATE | 信息披露日期 | 日期类型 |
| INFO_SOUR | 信息来源 | 数值类型 |
| END_DATE | 截止日期 | 日期类型 |
| SHEET_MARK_PAR | 报表合并标志 | 数值类型 |
| COST_INVE_INPUT | 费用化研发投入 | 数值类型 |
| CAPI_INVE_INPUT | 资本化研发投入 | 数值类型 |
| CAPI_INVE_RATIO | 资本化研发投入占比 | 数值类型 |
| RD_INPUT_TOT | 研发投入合计 | 数值类型 |
| RD_INPUT_RATIO | 研发投入占营业收入比例 | 数值类型 |
| RD_STAFF_VOL | 研发人员数量 | 数值类型 |
| RD_STAFF_VOL_RATIO | 研发人员数量占比 | 数值类型 |
| OTHE_INVE_INPUT | 其他研发投入 | 数值类型 |


