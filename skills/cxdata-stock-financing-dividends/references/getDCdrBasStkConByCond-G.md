# CDR与基础股票转换-通用 (getDCdrBasStkConByCond-G)

**API_ID:** getDCdrBasStkConByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| eventId | 事件ID | 数值类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| DRSHARESNUM | 存托凭证份数 | 数值类型 |
| BASICSECUSHARESNUM | 基础股票股数 | 数值类型 |
| STK_TYPE_PAR | 基础股票类型 | 数值类型 |
| TRANSRATIO | 基础股票与CDR之间的转换比例(1份转X股) | 数值类型 |
| DRPARVALUE | 存托凭证面值 | 数值类型 |
| DRPARVALUEUNIT | 存托凭证面值单位 | 数值类型 |
| BASICSECUPARVALUE | 基础股票面值 | 数值类型 |
| BASICSECUPARVALUEUNIT | 基础股票面值单位 | 数值类型 |
| EVENT_ID | 事件ID | 数值类型 |


