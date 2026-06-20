# 公司首发计划-通用 (getDComIpoPlanByCond-G)

**API_ID:** getDComIpoPlanByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| orgChiName | 公司名称 | 字符类型 | 否 |  |
| eventId | 事件ID | 数值类型 | 否 |  |
| declDate | 公告日期 | 日期类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| ORG_CHI_NAME | 公司名称 | 字符类型 |
| STK_TYPE_PAR | 股票类型参数 | 数值类型 |
| EVENT_ID | 事件ID | 数值类型 |
| DECL_DATE | 公告日期 | 日期类型 |
| PAR_VAL | 每股面值(人民币) | 数值类型 |
| ISS_VOL_CEIL | 计划发行量上限 | 数值类型 |
| ISS_VOL_FLOOR | 计划发行量下限 | 数值类型 |
| ISS_METH | 发行方式 | 字符类型 |
| ISS_OBJ | 发行对象 | 字符类型 |
| EVENT_TITLE | 事件标题 | 字符类型 |
| CURY_TYPE_PAR | 货币类型参数 | 数值类型 |
| PAR_VAL_FC | 每股面值(外币) | 数值类型 |


