# 经营层基础数据-通用 (getDManBasicInfoByCond-G)

**API_ID:** getDManBasicInfoByCond-G

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
| END_DATE | 截止日期 | 日期类型 |
| IS_ROTA_PRES_SYS | 是否有轮值总裁制度 | 数值类型 |
| AMOU_OF_MAN_ALLO_COM | 经营层年度报酬合计 | 数值类型 |
| MAN_DIR_TURN_RATIO | 董监高离职率 | 数值类型 |
| MAN_TURN_RATIO | 其中：经营层离职率 | 数值类型 |
| TOT_SHAR_HOLD | 经营层持股 | 数值类型 |
| TOT_SHAR_HOLD_INCR | 经营层增持股数 | 数值类型 |
| TOT_SHAR_HOLD_REDU | 经营层减持股数 | 数值类型 |


