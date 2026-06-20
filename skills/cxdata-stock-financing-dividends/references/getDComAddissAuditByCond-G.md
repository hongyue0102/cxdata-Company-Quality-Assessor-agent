# 公司增发审核-通用 (getDComAddissAuditByCond-G)

**API_ID:** getDComAddissAuditByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| declDate | 审核公告日期 | 日期类型 | 否 |  |
| eventId | 事件ID | 数值类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| STK_TYPE_PAR | 股票类型 | 数值类型 |
| ADDISS_METH_PAR | 增发类型 | 数值类型 |
| DECL_DATE | 审核公告日期 | 日期类型 |
| COMMIT_TYPE_PAR | 审核委员会类型 | 数值类型 |
| AUDIT_TYPE_PAR | 审核类型 | 数值类型 |
| MEET_DATE | 审核会议召开日 | 日期类型 |
| AUDIT_RESULT_DATE | 审核结果公告日 | 日期类型 |
| IS_AUDIT_PASS_PAR | 审核是否通过 | 数值类型 |
| UN_PASS_REAS | 未通过原因 | 字符类型 |
| AUDIT_ISS_STK_VOL | 核准发行股数 | 数值类型 |
| AUDIT_INDIV | 参会委员 | 字符类型 |
| EVENT_ID | 事件ID | 数值类型 |


