# 公司股东股权托管-通用 (getDComShareTrusteeByCond-G)

**API_ID:** getDComShareTrusteeByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| declDate | 公告日期 | 日期类型 | 否 |  |
| beTrustName | 股权受托方名称 | 字符类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| DECL_DATE | 公告日期 | 日期类型 |
| TRUST_NAME | 股权委托方名称 | 字符类型 |
| TRUSTEE_NUM | 托管股数 | 数值类型 |
| ACF_TOT_RATIO | 占总股本比例 | 数值类型 |
| SHARE_ATTR_PAR | 托管股份性质 | 数值类型 |
| START_DATE | 托管期限起始日 | 日期类型 |
| END_DATE | 托管期限截止日 | 日期类型 |
| BE_TRUST_NAME | 股权受托方名称 | 字符类型 |
| EVENT_DES | 事项描述 | 字符类型 |


