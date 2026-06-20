# 公司限售股东持股解禁预测情况-通用 (getDComRestcFloatForeByCond-G)

**API_ID:** getDComRestcFloatForeByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| hldName | 股东名称 | 字符类型 | 否 |  |
| listDate | 预计解禁日期 | 日期类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| STK_TYPE_PAR | 解禁股票类型 | 数值类型 |
| HLD_NAME | 股东名称 | 字符类型 |
| LIST_FLOAT_VOL | 解禁股份数量 | 数值类型 |
| LIST_DATE | 预计解禁日期 | 日期类型 |
| STK_ORI_PAR | 本次解禁股票来源 | 数值类型 |
| RESTC_DES | 限售条件说明 | 字符类型 |


