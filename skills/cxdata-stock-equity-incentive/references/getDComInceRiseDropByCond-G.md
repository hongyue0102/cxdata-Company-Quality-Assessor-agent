# 激励计划发布后涨跌幅-通用 (getDComInceRiseDropByCond-G)

**API_ID:** getDComInceRiseDropByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| firDeclDate | 激励计划公布日 | 日期类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| FIR_DECL_DATE | 激励计划公布日 | 日期类型 |
| RISE_DROP_RANGE5 | T+5日涨跌幅(%) | 数值类型 |
| RISE_DROP_RANGE10 | T+10日涨跌幅(%) | 数值类型 |


