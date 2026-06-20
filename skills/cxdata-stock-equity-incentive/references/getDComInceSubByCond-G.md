# 公司股权激励明细-通用 (getDComInceSubByCond-G)

**API_ID:** getDComInceSubByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| declDate | 公告日期 | 日期类型 | 否 |  |
| chanDate | 变动日期 | 日期类型 | 否 |  |
| subId | 子表关联标识 | 数值类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| DECL_DATE | 公告日期 | 日期类型 |
| CHAN_DATE | 变动日期 | 日期类型 |
| FIR_DECL_DATE | 首次公告日期 | 日期类型 |
| EVENT_PROC_PAR | 事件进程 | 数值类型 |
| EVENT_DES | 事件概述 | 字符类型 |
| STK_ORI_PAR | 股票来源 | 数值类型 |
| STK_TYPE_PAR | 标的股票类型 | 数值类型 |
| PAY_RATIO | 兑换比例 | 数值类型 |
| INCE_STK_VOL | 激励股票剩余数量 | 数值类型 |
| STK_VOL_CHAN | 股票数量本次变动 | 数值类型 |
| INCE_PRICE | 激励价格 | 数值类型 |
| CHAN_REAS_PAR | 变动原因 | 数值类型 |
| CHAN_TYPE_PAR | 激励变动参数 | 数值类型 |
| STK_GRA_TYPE | 激励授予类型 | 数值类型 |
| SUB_ID | 子表关联标识 | 数值类型 |
| INCE_PRICE_DESC | 备注 | 字符类型 |

#### 直接前置依赖
以下参数存在可参考的直接前置接口。是否调用前置接口，取决于当前查询目标、已知条件以及当前接口入参是否已满足。
- 参数 `subId`：可通过调用 **公司股权激励-通用（API_ID:getDComInceMainByCond-G）** 获取

#### 多流程依赖说明
当当前接口的关键入参存在多种补齐方式时，可按以下流程逐级调用，不要预先串行调用所有上游接口。
##### 流程1（补齐参数 `subId`）
1. 调用 **公司股权激励-通用（API_ID:getDComInceMainByCond-G）**，补齐后续所需参数 `subId`
2. 调用 **公司股权激励明细-通用（API_ID:getDComInceSubByCond-G）**，完成当前查询

