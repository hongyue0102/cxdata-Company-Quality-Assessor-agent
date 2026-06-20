# 公司控股股东及实际控制人-通用 (getDComHldActuContlrByCond-G)

**API_ID:** getDComHldActuContlrByCond-G

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
| CONTL_HLD | 控股股东 | 字符类型 |
| CONTL_HLD_RATIO | 控股股东持股比例 | 数值类型 |
| CONTL_HLD_VOL | 控股股东持股数量 | 数值类型 |
| ACTU_CONTLR | 实际控制人 | 字符类型 |
| INDIV_INFO_DES | 实际控制人背景 | 字符类型 |
| IS_ACTU_CONTLR_CHAN | 实际控制人是否变更 | 数值类型 |


