# 公司股改对价方案-通用 (getDComDiviConsiMainByCond-G)

**API_ID:** getDComDiviConsiMainByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| FIR_DECL_DATE | 首次公告日期 | 日期类型 |
| LAT_DECL_DATE | 最新公告日期 | 日期类型 |
| IS_VALID_PAR | 对价方案是否有效 | 数值类型 |
| PAYED_SHARE_ATTR_PAR | 获付股东股本性质 | 数值类型 |
| PAYED_CONSI_HLD_HOLD | 获付对价股东持股数 | 数值类型 |
| PAY_NON_FLOAT_HOLD | 支付对价非流通股东持股数占非流通股比例 | 数值类型 |
| ACF_NON_FLOAT | 支付对价非流通股东持股数占非流通股比例 | 数值类型 |
| PLAN_TYPE | 股改方案类型 | 字符类型 |
| COM_PRESE | 流通股东获公司送股数(10送X) | 数值类型 |
| PRESE_NON_CONV_PAY | 流通股东获公司转付股数(10送X) | 数值类型 |
| PRESE_COM_PAYED | 流通股东直接从公司获付股数(10送X) | 数值类型 |
| COM_CONV | 流通股东获公司增股数(10转增X) | 数值类型 |
| CONV_NON_CONV_PAY | 流通股东获公司转增股数(10转增X) | 数值类型 |
| CONV_COM_PAYED | 流通股东直接从公司获增股数(10转增X) | 数值类型 |
| COM_CASH | 流通股东获公司派现额(10派X元) | 数值类型 |
| CASH_NON_CONV_PAY | 流通股东获公司转付派现额(10派X) | 数值类型 |
| CASH_COM_PAYED | 流通股东直接从公司获得派现额(10派X) | 数值类型 |
| COM_CASH_AFTER_TAX | 流通股东获公司派现额(10派X,税后) | 数值类型 |
| COM_WARR | 流通股东获公司认股证数(10送X) | 数值类型 |
| WARR_NON_CONV_PAY | 流通股东获公司转付认股证数(10送X) | 数值类型 |
| WARR_COM_PAYED | 流通股东直接从公司获认股证数(10送X) | 数值类型 |
| COM_STO_DIV | 公司合计送转股数 | 数值类型 |
| COM_CASH_AMUT | 公司合计派现金额 | 数值类型 |
| COM_WARR_SUM | 公司合计认股证份数 | 数值类型 |
| CONSI_STK | 流通股东获非流通股东对价股份(10送X) | 数值类型 |
| CONSI_CASH | 流通股东获非流通股东对价现金(10派X) | 数值类型 |
| CONSI_CASH_AFTER_TAX | 流通股东获非流通股东对价现金(10派X,税后) | 数值类型 |
| CONSI_WARR | 流通股东获非流通股东对价认股证(10送X) | 数值类型 |
| CALL_WARR | 流通股东获非流通股东对价认购证(10送X) | 数值类型 |
| PUT_WARR | 流通股东获非流通股东对价认沽证(10送X) | 数值类型 |
| CONSI_STK_SUM | 非流通股东支付对价股份总额 | 数值类型 |
| CONSI_CASH_SUM | 非流通股东支付对价现金总额 | 数值类型 |
| CONSI_WARR_SUM | 非流通股东支付对价认股证总量 | 数值类型 |
| PRE_SHRI_ACF | 缩股前非流通股占总股本比例 | 数值类型 |
| AFTER_SHRI_ACF | 缩股后非流通股占总股本比例 | 数值类型 |
| NON_FLOAT_SHRI | 非流通股缩股总数 | 数值类型 |
| DIVI_PLAN_DES | 改革方案说明 | 字符类型 |
| PRICE_DES | 定价依据说明 | 字符类型 |


