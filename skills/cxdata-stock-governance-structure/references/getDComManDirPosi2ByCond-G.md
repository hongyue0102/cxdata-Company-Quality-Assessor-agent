# 监事会任职情况-通用 (getDComManDirPosi2ByCond-G)

**API_ID:** getDComManDirPosi2ByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| newDeclDate | 公告日期 | 日期类型 | 否 |  |
| indivName | 人物姓名 | 字符类型 | 否 |  |
| posiPar | 职位参数 | 数值类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| NEW_DECL_DATE | 公告日期 | 日期类型 |
| INDIV_NAME | 人物姓名 | 字符类型 |
| POSI_NAME | 职位名称 | 字符类型 |
| POSI_START_DATE | 任职起始日 | 日期类型 |
| POSI_END_DATE | 任职截止日 | 日期类型 |
| IS_REPR_POSI_PAR | 是否代理职位 | 数值类型 |
| CHAN_REAS_DES | 变动原因说明 | 字符类型 |
| POSI_PAR | 职位参数 | 数值类型 |
| CHAN_REAS_PAR | 变动原因类别 | 数值类型 |


