# 上市公司固定及无形等资产明细-通用 (getComFinNoteFixIntAsseByCond-G)

**API_ID:** getComFinNoteFixIntAsseByCond-G

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
| ORI_OPEN_BALA | 原值期初数 | 数值类型 |
| ORI_CUR_ADD | 原值本期增加 | 数值类型 |
| ORI_CUR_DECR | 原值本期减少 | 数值类型 |
| ORI_END_BALA | 原值期末数 | 数值类型 |
| DEP_OPEN_BALA | 折旧摊销期初数 | 数值类型 |
| DEP_CUR_ADD | 折旧摊销本期增加 | 数值类型 |
| DEP_CUR_DECR | 折旧摊销本期减少 | 数值类型 |
| DEP_END_BALA | 折旧摊销期末数 | 数值类型 |
| IMP_OPEN_BALA | 减值准备期初数 | 数值类型 |
| IMP_CUR_ADD | 减值准备本期增加 | 数值类型 |
| IMP_CUR_DECR | 减值准备本期减少 | 数值类型 |
| IMP_END_BALA | 减值准备期末数 | 数值类型 |
| BOO_OPEN_BALA | 账面价值期初数 | 数值类型 |
| BOO_CUR_ADD | 账面价值本期增加 | 数值类型 |
| BOO_CUR_DECR | 账面价值本期减少 | 数值类型 |
| BOO_END_BALA | 账面价值期末数 | 数值类型 |


