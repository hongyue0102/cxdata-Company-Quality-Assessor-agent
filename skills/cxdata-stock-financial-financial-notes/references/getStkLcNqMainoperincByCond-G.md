# 三板主营收入构成-通用 (getStkLcNqMainoperincByCond-G)

**API_ID:** getStkLcNqMainoperincByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| enddate | 截止日期 | 日期类型 | 否 |  |
| mark | 合并调整标志 | 数值类型 | 否 |  |
| classification | 分类方式 | 数值类型 | 否 |  |
| project | 项目名称 | 字符类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| INFOPUBLDATE | 公告日期 | 日期类型 |
| ENDDATE | 截止日期 | 日期类型 |
| MARK | 合并调整标志 | 数值类型 |
| INFOSOURCE | 信息来源 | 字符类型 |
| CLASSIFICATION | 分类方式 | 数值类型 |
| PROJECT | 项目名称 | 字符类型 |
| REGANDBUSINESS | 地区与业务性质 | 数值类型 |
| OPERINCOME | 本期主营业务收入 | 数值类型 |
| OPERINCRATIO | 本期主营业务收入占比 | 数值类型 |
| OPERCOST | 本期主营业务成本 | 数值类型 |
| OPERPROFIT | 本期主营业务利润 | 数值类型 |
| GROSSPROFIT | 毛利率 | 数值类型 |
| OPERINCOMELY | 上期主营业务收入 | 数值类型 |
| OPERINCLYRAT | 上期收入占比 | 数值类型 |
| OPERCOSTLY | 上期主营业务成本 | 数值类型 |
| OPERPROFITLY | 上期主营业务利润 | 数值类型 |


