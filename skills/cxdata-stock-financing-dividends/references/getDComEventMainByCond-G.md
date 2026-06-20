# 公司事件主表-通用 (getDComEventMainByCond-G)

**API_ID:** getDComEventMainByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| eventId | 事件ID | 数值类型 | 否 |  |
| listSectPar | 拟上市板块参数 | 数值类型 | 否 |  |
| secMarPar | 拟上市证券市场 | 数值类型 | 否 |  |
| orgChiName | 机构中文名称 | 字符类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| EVENT_ID | 事件ID | 数值类型 |
| STK_TYPE_PAR | 股票类别参数 | 数值类型 |
| EVENT_TYPE_PAR | 事件类别参数 | 数值类型 |
| FIR_DECL_DATE | 首次信息发布日期 | 日期类型 |
| FIR_DECL_YEAR | 首次信息发布年度 | 数值类型 |
| EVENT_TITLE | 事件标题 | 字符类型 |
| EVENT_DES | 事件概述 | 字符类型 |
| LIST_SECT_PAR | 拟上市板块参数 | 数值类型 |
| SEC_MAR_PAR | 拟上市证券市场 | 数值类型 |
| ORG_CHI_NAME | 机构中文名称 | 字符类型 |


