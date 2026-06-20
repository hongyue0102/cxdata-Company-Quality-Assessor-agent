# 上市公司违规信息-通用 (getDComPunishEventMain1ByCond-G)

**API_ID:** getDComPunishEventMain1ByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| PUNISH_DATE | 公告日期 | 日期类型 |
| ENVENT_PERF | 标题 | 字符类型 |
| HANDLE_PEO | 处理单位 | 字符类型 |
| ENVENT_LAW | 违反相关法规 | 字符类型 |
| PUNISH_TYPE | 处罚类别 | 字符类型 |
| PUNISH_MONEY | 处罚金额 | 数值类型 |


