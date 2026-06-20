# 公司股东股权转让-通用 (getDComHldShareTranByCond-G)

**API_ID:** getDComHldShareTranByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| iniPublDate | 首次公告日期 | 日期类型 | 否 |  |
| equityTranPar | 股权转让方式 | 数值类型 | 否 |  |
| tranrName | 股份出让方名称 | 字符类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| INI_PUBL_DATE | 首次公告日期 | 日期类型 |
| EQUITY_TRAN_PAR | 股权转让方式 | 数值类型 |
| TRANR_NAME | 股份出让方名称 | 字符类型 |
| START_DATE | 协议签署日期 | 日期类型 |
| END_DATE | 正式过户日期 | 日期类型 |
| TRADE_SHARE | 交易股份数量 | 数值类型 |
| PCT_ACF_TOT | 占总股本比例 | 数值类型 |
| SHARE_TYPE_PAR | 交易股份性质 | 数值类型 |
| TRADE_PRI_FLOOR | 交易价格 | 数值类型 |
| TRADE_PRI_CEIL | 交易价格上限 | 数值类型 |
| TRADE_AMUT | 交易金额 | 数值类型 |
| SUM_BEF_TRANR | 出让前持股总数 | 数值类型 |
| PCT_BEF_TRANR | 出让前持股比例 | 数值类型 |
| SUM_AFTER_TRANR | 出让后持股总数 | 数值类型 |
| PCT_AFTER_TRANR | 出让后持股比例 | 数值类型 |
| TRANE_NAME | 股份受让方名称 | 字符类型 |
| SUM_AFTER_TRANE | 受让后持股总数 | 数值类型 |
| PCT_AFTER_TRANE | 受让后持股比例 | 数值类型 |
| EVENT_DES | 事项描述与进展说明 | 字符类型 |
| IS_STOP | 是否终止实施 | 数值类型 |


