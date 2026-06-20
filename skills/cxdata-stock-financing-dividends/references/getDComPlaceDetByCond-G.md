# 公司大股东认配明细-通用 (getDComPlaceDetByCond-G)

**API_ID:** getDComPlaceDetByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| declDate | 公告日期 | 日期类型 | 否 |  |
| eventId | 事件ID | 数值类型 | 否 |  |
| hldName | 股东名称 | 字符类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| STK_TYPE_PAR | 股票类型 | 数值类型 |
| DECL_DATE | 公告日期 | 日期类型 |
| EVENT_ID | 事件ID | 数值类型 |
| HLD_NAME | 股东名称 | 字符类型 |
| PLACE_METH | 认配方式 | 字符类型 |
| PLACE_VOL | 配售股数 | 数值类型 |


