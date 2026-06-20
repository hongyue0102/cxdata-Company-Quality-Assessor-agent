# 公司证券投资情况-通用 (getComSecuInveInfoByCond-G)

**API_ID:** getComSecuInveInfoByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| endDate | 截止日期 | 日期类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| DECL_DATE | 公告日期 | 日期类型 |
| END_DATE | 截止日期 | 日期类型 |
| SEC_VARI | 证券品种 | 字符类型 |
| SEC_TYPE_PAR | 证券类型参数 | 数值类型 |
| SEC_CODE | 证券代码 | 字符类型 |
| SEC_SHORT_NAME | 证券简称 | 字符类型 |
| INI_INVE_AMUT | 最初投资成本 | 数值类型 |
| ACC_MEAS_MODE | 会计计量模式 | 字符类型 |
| INI_BOOK_VAL | 期初账面价值 | 数值类型 |
| CUR_FAIR_INVE_PROF_LOSS | 本期公允价值变动损益 | 数值类型 |
| ACC_FAIR_VAL_CHAN_EQU | 计入权益的累计公允价值变动 | 数值类型 |
| CUR_PUR_AMUT | 本期购买金额 | 数值类型 |
| CUR_SALE_AMUT | 本期出售金额 | 数值类型 |
| REP_PROF_LOSS | 本期投资损益 | 数值类型 |
| END_BOOK_VAL | 期末账面价值 | 数值类型 |
| ACCU_SUBJ_PAR | 会计核算科目 | 字符类型 |
| FUND_SOUR | 资金来源 | 字符类型 |


