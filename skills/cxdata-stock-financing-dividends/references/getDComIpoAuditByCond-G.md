# 公司首发审核信息-通用 (getDComIpoAuditByCond-G)

**API_ID:** getDComIpoAuditByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| orgName | 公司名称 | 字符类型 | 否 |  |
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| declDate | 审核公告日期 | 日期类型 | 否 |  |
| eventId | 事件ID | 数值类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| ORG_NAME | 公司名称 | 字符类型 |
| STK_TYPE_PAR | 发行股票类型 | 数值类型 |
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| APPL_DECL_DATE | 申报稿披露日期 | 日期类型 |
| AUDIT_RESULT_DATE | 审核结果公告日 | 日期类型 |
| MEET_DATE | 审核会议召开日 | 日期类型 |
| IS_AUDIT_PASS_PAR | 审核是否通过 | 数值类型 |
| UN_PASS_REAS | 未通过原因 | 字符类型 |
| AUDIT_ISS_STK_VOL | 核准发行股数 | 数值类型 |
| PAR_VAL | 每股面值 | 数值类型 |
| ISS_VOL_CEIL | 计划发行量上限 | 数值类型 |
| ISS_VOL_FLOOR | 计划发行量下限 | 数值类型 |
| DECL_DATE | 审核公告日期 | 日期类型 |
| COMMIT_TYPE_PAR | 委员会类型 | 数值类型 |
| AUDIT_INDIV | 参会委员 | 字符类型 |
| EVENT_ID | 事件ID | 数值类型 |
| INFO_ORI | 信息来源 | 字符类型 |

#### 直接前置依赖
以下参数存在可参考的直接前置接口。是否调用前置接口，取决于当前查询目标、已知条件以及当前接口入参是否已满足。
- 参数 `eventId`：可通过调用 **公司事件主表-通用（API_ID:getDComEventMainByCond-G）** 获取

#### 多流程依赖说明
当当前接口的关键入参存在多种补齐方式时，可按以下流程逐级调用，不要预先串行调用所有上游接口。
##### 流程1（补齐参数 `eventId`）
1. 调用 **公司事件主表-通用（API_ID:getDComEventMainByCond-G）**，补齐后续所需参数 `eventId`
2. 调用 **公司首发审核信息-通用（API_ID:getDComIpoAuditByCond-G）**，完成当前查询

