# 公司股东股权质押-通用 (getDComSharePleByCond-G)

**API_ID:** getDComSharePleByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| declDate | 公告日期 | 日期类型 | 否 |  |
| typeSelePar | 质押类别 | 数值类型 | 否 |  |
| pleHldName | 出质人 | 字符类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| DECL_DATE | 公告日期 | 日期类型 |
| TYPE_SELE_PAR | 质押类别 | 数值类型 |
| PLE_HLD_NAME | 出质人 | 字符类型 |
| ACCE_NAME | 质权人 | 字符类型 |
| PLE_SHARE | 股数 | 数值类型 |
| START_DATE | 期限起始日 | 日期类型 |
| END_DATE | 期限截止日 | 日期类型 |
| SHARE_ATTR_PAR | 股份性质 | 数值类型 |
| EVENT_DES | 事项描述 | 字符类型 |


