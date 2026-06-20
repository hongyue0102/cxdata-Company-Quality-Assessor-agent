# 公司股东户数-通用 (getDComHldTotByCond-G)

**API_ID:** getDComHldTotByCond-G

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
| DECL_DATE | 公告日期 | 日期类型 |
| END_DATE | 截止日期 | 日期类型 |
| HLD_TOT | 股东总户数 | 数值类型 |
| A_HLD_TOT | A股股东户数 | 数值类型 |
| B_HLD_TOT | B股股东户数 | 数值类型 |
| H_HLD_TOT | H股股东户数 | 数值类型 |


