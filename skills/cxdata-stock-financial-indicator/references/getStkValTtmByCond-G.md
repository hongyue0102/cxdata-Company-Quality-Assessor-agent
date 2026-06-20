# 股票估值相关TTM指标表-通用 (getStkValTtmByCond-G)

**API_ID:** getStkValTtmByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| endDate | 截止日期 | 日期类型 | 否 |  |
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| END_DATE | 截止日期 | 日期类型 |
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| PE_TTM | 市盈率(TTM) | 数值类型 |
| PE_TTM1 | 市盈率(扣除非经常性损益)(TTM) | 数值类型 |
| PCF_TTM | 市现率(经营现金流)(TTM) | 数值类型 |
| PCF_TTM2 | 市现率(现金净流量)(TTM) | 数值类型 |
| PS_TTM | 市销率(TTM) | 数值类型 |
| DIV_YIELD_TTM | 股息率(TTM) | 数值类型 |
| DIV_YIELD_IND | 股息率(预计)(TTM) | 数值类型 |
| PRIC_FCF_RATI | 市值与股东自由现金流(TTM)比率 | 数值类型 |
| PRIC_REV_GRO | 股价/收入(TTM)增长(PEG) | 数值类型 |
| ENT_VAL | 企业价值(含货币资金) | 数值类型 |
| COR_VALUE | 企业价值(剔除货币资金) | 数值类型 |
| PRIC_CASH_FLOW_RATIO | 企业价值/经营现金流(TTM) | 数值类型 |
| ENT_VALU_EBITDA_RATIO | 企业价值与EBITDA(TTM)比率 | 数值类型 |
| ENT_VALU_EBIT_RATIO | 企业价值与EBIT(TTM)比率 | 数值类型 |
| ENT_VALU_INCO_RATIO | 企业价值收入比(TTM) | 数值类型 |
| ENT_VALU_GRO_PRO_RATIO | 企业价值毛利润比(TTM) | 数值类型 |
| ENT_VALU_FCF_RATIO | 企业价值公司自由现金流(TTM)比 | 数值类型 |
| NET_WOR_CAP_PRIC_RATIO | 股价/每股营运资本 | 数值类型 |
| MARK_VALU | 总市值(考虑汇率,A股/B股/H股) | 数值类型 |
| MARK_VALU_NORA | 总市值(不考虑汇率，总股本算) | 数值类型 |
| PRIC_BOO_RATIO_EQU | 市净率(净资产) | 数值类型 |
| PRIC_BOO_RATIO_PAR | 市净率(归属母公司股东权益合计) | 数值类型 |


