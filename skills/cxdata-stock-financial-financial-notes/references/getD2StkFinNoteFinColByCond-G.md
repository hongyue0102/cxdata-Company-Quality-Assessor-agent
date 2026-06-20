# 财务费用-通用 (getD2StkFinNoteFinColByCond-G)

**API_ID:** getD2StkFinNoteFinColByCond-G

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
| END_DATE | 截止日期 | 日期类型 |
| SHEET_MARK_PAR | 报表合并标志 | 数值类型 |
| SUBJ_NAME | 科目名称 | 字符类型 |
| OPEN_BALA | 上年同期金额 | 数值类型 |
| CUR_ADD | 本期增加 | 数值类型 |
| CUR_DECR | 本期减少 | 数值类型 |
| END_BALA | 本期金额 | 数值类型 |


