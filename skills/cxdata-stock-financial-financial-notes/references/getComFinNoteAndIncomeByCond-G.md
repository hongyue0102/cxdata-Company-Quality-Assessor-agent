# 上市公司利润分配表附注_通用-通用 (getComFinNoteAndIncomeByCond-G)

**API_ID:** getComFinNoteAndIncomeByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| endDate | 截止日期 | 日期类型 | 否 |  |
| sheetMarkPar | 报表合并标志 | 数值类型 | 否 |  |
| subjCateCode | 科目大类代码 | 数值类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| INFO_PUB_DATE | 信息发布日期 | 日期类型 |
| END_DATE | 截止日期 | 日期类型 |
| SHEET_MARK_PAR | 报表合并标志 | 数值类型 |
| INFO_SOUR | 信息来源 | 数值类型 |
| SUBJ_CATE_CODE | 科目大类代码 | 数值类型 |
| SUBJ_NAME | 科目名称 | 字符类型 |
| CURY_UNIT_PAR | 货币类型 | 数值类型 |
| CUR_BALA | 金额 | 数值类型 |


