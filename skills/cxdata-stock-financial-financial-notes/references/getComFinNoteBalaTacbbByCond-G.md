# 上市公司资产负债表附注_通用-通用 (getComFinNoteBalaTacbbByCond-G)

**API_ID:** getComFinNoteBalaTacbbByCond-G

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
| INFO_PUB_DATE | 信息披露日期 | 日期类型 |
| INFO_SOUR | 信息来源 | 数值类型 |
| END_DATE | 截止日期 | 日期类型 |
| SHEET_MARK_PAR | 报表合并标志 | 数值类型 |
| SUBJ_CATE_CODE | 科目大类代码 | 数值类型 |
| SUBJ_NAME | 科目名称 | 字符类型 |
| CURY_TYPE_PAR | 货币类型参数 | 数值类型 |
| INIT_AMOUNT | 期初金额 | 数值类型 |
| INIT_PROV_AMOUNT | 期初计提金额 | 数值类型 |
| CURR_INCR | 本期增加 | 数值类型 |
| CURR_DECR | 本期减少 | 数值类型 |
| FINA_AMOUNT | 期末金额 | 数值类型 |
| FINA_PROV_AMOUNT | 期末计提金额 | 数值类型 |


