# 上市公司历年审计意见-通用 (getDComAuditOpinNewByCond-G)

**API_ID:** getDComAuditOpinNewByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| endDate | 截止日期 | 日期类型 | 否 |  |
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| END_DATE | 截止日期 | 日期类型 |
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| AUDIT_FEES_TOAL | 审计费用合计(废弃) | 数值类型 |
| CURY_UNIT_PAR | 货币单位(废弃) | 数值类型 |
| CHU_FII_PAR1 | 事务所性质 | 数值类型 |
| ACC_OFFI_IN1 | 会计师事务所 | 字符类型 |
| REG_ACC1 | 审计师 | 字符类型 |
| DECL_DATE1 | 签署日期 | 日期类型 |
| AUDIT_TYPE_PAR1 | 审计意见类型 | 数值类型 |
| AUDIT_OPIN1 | 审计意见全文 | 字符类型 |
| OTH_AUDIT_FEES1 | 其他相关费用 | 数值类型 |
| CURY_TYPE_PAR1 | 货币类型 | 数值类型 |
| CURY_UNIT_PAR1 | 货币单位 | 数值类型 |
| AUDIT_LIFE1 | 事务所连续服务年限 | 数值类型 |
| AUDIT_FEES_DES1 | 审计费用说明 | 字符类型 |
| CPA_AUDIT_LIFE1 | 注册会计师审计服务的连续年限 | 字符类型 |


