# 激励解禁上市日股价与激励价格对比-通用 (getDComIncePriceCompByCond-G)

**API_ID:** getDComIncePriceCompByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| listDate | 上市流通日期 | 日期类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| LIST_DATE | 上市流通日期 | 日期类型 |
| CLOSE_PRICE | 上市流通日收盘价 | 数值类型 |
| INCE_PRICE | 激励价格 | 数值类型 |
| RISE_DROP | 涨跌 | 数值类型 |


