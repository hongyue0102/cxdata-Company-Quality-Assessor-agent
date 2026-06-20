# 公司股权激励统计-通用 (getDComInceStatByCond-G)

**API_ID:** getDComInceStatByCond-G

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
| INCE_TOT_VOL | 激励累计总数量 | 数值类型 |
| INCE_TOT_VOL_R | 其中：限制性股票累计总数量 | 数值类型 |
| INCE_TOT_VOL_O | 其中：股票期权累计总数量 | 数值类型 |
| STK_VOL_CHAN | 本次变动数量 | 数值类型 |
| INCE_STK_VOL | 激励剩余数量 | 数值类型 |
| INCE_STK_VOL_R | 其中：限制性股票剩余数量 | 数值类型 |
| INCE_STK_VOL_O | 其中：股票期权剩余数量 | 数值类型 |


