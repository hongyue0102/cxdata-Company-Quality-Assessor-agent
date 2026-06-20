# 承销商信息-通用 (getDUndeInfoByCond-G)

**API_ID:** getDUndeInfoByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| declDate | 招股公告书日期 | 日期类型 | 否 |  |
| eventId | 事件ID | 数值类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| DECL_DATE | 招股公告书日期 | 日期类型 |
| AGENT_TYPE_PAR | 承销商类型 | 数值类型 |
| EVENT_ID | 事件ID | 数值类型 |
| AGENT_NAME | 承销商名称 | 字符类型 |
| UNDE_VOL | 承销数量 | 数值类型 |
| UNDE_RATIO | 承销比例 | 数值类型 |


