# 公司配股计划-通用 (getDComPlacePlanByCond-G)

**API_ID:** getDComPlacePlanByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| planPublDate | 预案公布日 | 日期类型 | 否 |  |
| eventId | 事件ID | 数值类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| STK_TYPE_PAR | 股票类型 | 数值类型 |
| PLAN_PUBL_DATE | 预案公布日 | 日期类型 |
| EVENT_ID | 事件ID | 数值类型 |
| VALID_START_DATE | 预案有效期起始日 | 日期类型 |
| VALID_END_DATE | 预案有效期截止日 | 日期类型 |
| PLAN_RATIO | 计划配股比例(10配X) | 字符类型 |
| STM_RESO_PUBL_DATE | 股东大会决议公告日期 | 日期类型 |
| PLAN_CHAN_PAR | 方案变动类型 | 数值类型 |
| PLAN_CHAN_DES | 方案变动说明 | 字符类型 |


