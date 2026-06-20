# 上市公司A股限售解禁时间-通用 (getDComRestcDetByCond-G)

**API_ID:** getDComRestcDetByCond-G

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
| LIST_DATE | 可流通起始日 | 日期类型 |
| NEW_FLOAT_A | 本次新增可售A股 | 数值类型 |
| NEW_FLOAT_RATIO | 本次新增可售A股占上期末已流通A股比例 | 数值类型 |
| FLOAT_A | 已流通A股 | 数值类型 |
| NON_FLOAT_A | 待流通A股 | 数值类型 |
| TOT_A_SHARE | A股总数 | 数值类型 |
| FLOAT_A_RATIO | 已流通A股占A股总数比例 | 数值类型 |
| TOT_SHARE | 总股本 | 数值类型 |
| STK_ORI_DES | 本次解禁股份来源说明 | 字符类型 |


