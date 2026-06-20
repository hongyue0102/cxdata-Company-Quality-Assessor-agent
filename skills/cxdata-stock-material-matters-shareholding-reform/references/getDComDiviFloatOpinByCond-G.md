# 公司股改流通股东表决-通用 (getDComDiviFloatOpinByCond-G)

**API_ID:** getDComDiviFloatOpinByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| hldName | 股东名称 | 字符类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| FIR_DECL_DATE | 首次公告日期 | 日期类型 |
| RESO_MAIN_TITLE | 议案大标题 | 字符类型 |
| HLD_NAME | 股东名称 | 字符类型 |
| HLD_ATTR_PAR | 股东性质 | 数值类型 |
| HOLD_SUM | 持股数量 | 数值类型 |
| ACF_TOT_SHARE | 持股占总股本的比例 | 数值类型 |
| VOTE_OPIN_PAR | 股东表决意见 | 数值类型 |


