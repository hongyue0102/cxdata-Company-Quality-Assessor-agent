# 公司外部监督基础表-通用 (getDComExtSupBasicInfoByCond-G)

**API_ID:** getDComExtSupBasicInfoByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| endDate | 截止日期 | 日期类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| END_DATE | 截止日期 | 日期类型 |
| EVA_END_PAR | 交易所信息披露评级 | 数值类型 |
| S017 | 诉讼败诉率 | 数值类型 |
| PUNISH_NUM1 | 被处罚次数(上市公司) | 数值类型 |
| PUNISH_FIN_AMOUT1 | 被罚款总金额(上市公司) | 数值类型 |
| PUNISH_NUM2 | 被处罚人次(高管) | 数值类型 |
| PUNISH_FIN_AMOUT2 | 被罚款总金额(高管) | 数值类型 |
| AUDIT_TYPE_PAR1 | 年报意见 | 数值类型 |
| S016 | 敏感舆情指数年度值 | 数值类型 |


