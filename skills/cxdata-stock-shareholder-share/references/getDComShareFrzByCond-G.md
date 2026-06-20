# 公司股东股权冻结-通用 (getDComShareFrzByCond-G)

**API_ID:** getDComShareFrzByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| declDate | 公告日期 | 日期类型 | 否 |  |
| typeSelePar | 冻结类别 | 数值类型 | 否 |  |
| frzHldName | 股权被冻结股东名称 | 字符类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| DECL_DATE | 公告日期 | 日期类型 |
| TYPE_SELE_PAR | 冻结类别 | 数值类型 |
| FRZ_HLD_NAME | 股权被冻结股东名称 | 字符类型 |
| FRZ_SHARE | 涉及股数 | 数值类型 |
| START_DATE | 冻结期限起始日 | 日期类型 |
| END_DATE | 冻结期限截止日/解除冻结日 | 日期类型 |
| IS_PLE_RID | 是否质押后司法冻结 | 数值类型 |
| EVENT_DES | 事项描述 | 字符类型 |


