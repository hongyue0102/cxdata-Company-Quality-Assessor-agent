# 公司信息披露统计-通用 (getDComInfoDiscStatByCond-G)

**API_ID:** getDComInfoDiscStatByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| statYear | 统计年度 | 数值类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| STAT_YEAR | 统计年度 | 数值类型 |
| SEAS_INC_NUM | 季报披露延时次数(当年累计) | 数值类型 |
| SEAS_INC_DAYS | 季报披露延时天数(当年累计) | 数值类型 |
| IS_HALF_YEAR_REW_DURA | 半年报披露是否延时(当年) | 数值类型 |
| HALF_YEAR_REW_DURA_DAYS | 半年报披露延时天数(当年) | 数值类型 |
| IS_YEAR_REW_DURA | 年报披露是否延时(当年) | 数值类型 |
| YEAR_REW_DURA_DAYS | 年报披露延时天数(当年) | 数值类型 |


