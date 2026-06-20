# 上市公司主营业务构成-通用 (getComFinNoteMainBusiByCond-G)

**API_ID:** getComFinNoteMainBusiByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| endDate | 截止日期 | 日期类型 | 否 |  |
| sheetMarkPar | 报表合并标志 | 数值类型 | 否 |  |
| projClass | 分类方式 | 数值类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| INFO_PUB_DATE | 信息发布日期 | 日期类型 |
| END_DATE | 截止日期 | 日期类型 |
| INFO_SOUR | 信息来源 | 数值类型 |
| SHEET_MARK_PAR | 报表合并标志 | 数值类型 |
| PROJ_CLASS | 分类方式 | 数值类型 |
| CURY_TYPE | 货币类型 | 数值类型 |
| PRO_NAME_NEW | 项目名称 | 字符类型 |
| PARE_NAME | 上级科目名称 | 字符类型 |
| MAIN_BUSI_INCO | 主营业务收入 | 数值类型 |
| MAIN_BUSI_COST | 主营业务成本 | 数值类型 |
| MAIN_BUSI_PROF | 主营业务利润 | 数值类型 |
| GROSS_MARG | 毛利率 | 数值类型 |
| MAIN_BUSI_INCO_LAST_YEAR | 上年同期主营业务收入 | 数值类型 |
| MAIN_BUSI_COST_LAST_YEAR | 上年同期主营业务成本 | 数值类型 |
| MAIN_BUSI_PROF_LAST_YEAR | 上年同期主营业务利润 | 数值类型 |
| GROSS_MARG_LAST_YEAR | 上年同期毛利率 | 数值类型 |
| MAININCOMEGROWRATEYOY | 主营业务收入同比 | 数值类型 |
| MAINICOSTGROWRATEYOY | 主营业务成本同比 | 数值类型 |
| MAINPROFITGROWRATEYOY | 主营业务利润同比 | 数值类型 |
| GROSSPROFITYOY | 毛利率同比 | 数值类型 |
| GROSSPROFITINCREASE | 毛利率比上年同期增减 | 数值类型 |


