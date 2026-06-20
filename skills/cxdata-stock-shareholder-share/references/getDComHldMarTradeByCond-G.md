# 公司股东交易所增持减持-通用 (getDComHldMarTradeByCond-G)

**API_ID:** getDComHldMarTradeByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| declDate | 公告日期 | 日期类型 | 否 |  |
| shareChanPar | 股份变动方向参数 | 数值类型 | 否 |  |
| hldName | 股东名称 | 字符类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| DECL_DATE | 公告日期 | 日期类型 |
| SHARE_CHAN_PAR | 股份变动方向参数 | 数值类型 |
| HLD_NAME | 股东名称 | 字符类型 |
| OBJ_NAME | 交易对象名称 | 字符类型 |
| START_DATE | 起始日期 | 日期类型 |
| END_DATE | 截止日期 | 日期类型 |
| TRADE_SHARE | 交易股数 | 数值类型 |
| PCT_ACF_TOT | 占总股本比例 | 数值类型 |
| TRADE_PRI_FLOOR | 交易价格下限 | 数值类型 |
| TRADE_PRI_CEIL | 交易价格上限 | 数值类型 |
| SUM_BEF_TRAN | 变动前持股数量 | 数值类型 |
| PCT_BEF_TRAN | 变动前占总股本比例 | 数值类型 |
| RANK_BEF_TRAN | 变动前股东排名 | 数值类型 |
| SUM_AFTER_TRAN | 变动后持股数量 | 数值类型 |
| PCT_AFTER_TRAN | 变动后占总股本比例 | 数值类型 |
| RANK_AFTER_TRAN | 变动后股东排名 | 数值类型 |
| EVENT_DES | 事项描述与计划说明 | 字符类型 |


