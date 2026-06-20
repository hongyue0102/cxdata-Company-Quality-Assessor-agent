# 上市公司非经常性损益明细-通用 (getComFinNoteProfAndLossByCond-G)

**API_ID:** getComFinNoteProfAndLossByCond-G

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
| INFO_PUB_DATE | 信息发布日期 | 日期类型 |
| INFO_SOUR | 信息来源 | 数值类型 |
| END_DATE | 截止日期 | 日期类型 |
| SHEET_MARK_PAR | 报表合并标志 | 数值类型 |
| ITEM_NAME | 项目名称 | 字符类型 |
| ITEM_CODE | 项目类别 | 数值类型 |
| CURY_UNIT_PAR | 货币单位 | 数值类型 |
| RELA_ACOUT | 金额 | 数值类型 |


