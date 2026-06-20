# 公司增发计划-通用 (getDComAddissPlanByCond-G)

**API_ID:** getDComAddissPlanByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| planPublDate | 预案公布日期 | 日期类型 | 否 |  |
| eventId | 事件ID | 数值类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| STK_TYPE_PAR | 增发股票类型 | 数值类型 |
| ADDISS_METH_PAR | 增发类型 | 数值类型 |
| PLAN_PUBL_DATE | 预案公布日期 | 日期类型 |
| EVENT_ID | 事件ID | 数值类型 |
| VALID_START_DATE | 预案有效期起始日 | 日期类型 |
| VALID_END_DATE | 预案有效期截止日 | 日期类型 |
| PRICE_CEIL_RMB | 计划发行价上限(人民币) | 数值类型 |
| PRICE_FLOOR_RMB | 计划发行价下限(人民币) | 数值类型 |
| ISS_VOL_CEIL | 计划发行数量上限 | 数值类型 |
| ISS_VOL_FLOOR | 计划发行数量下限 | 数值类型 |
| STM_RESO_PUBL_DATE | 股东大会决议公告日期 | 日期类型 |
| PLAN_CHAN_PAR | 方案变动类型 | 数值类型 |
| PLAN_CHAN_DES | 方案变动说明 | 字符类型 |
| CAP_DES | 募集资金用途简述 | 字符类型 |


