# 公司股改股东大会表决-通用 (getDComDiviHldMeetByCond-G)

**API_ID:** getDComDiviHldMeetByCond-G

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
| FIR_DECL_DATE | 首次公告日期 | 日期类型 |
| AGRE_SHARE | 全部股东同意票数 | 数值类型 |
| AGRE_ACF | 全部股东同意票数占本次全部股东有效表决权票数比率 | 数值类型 |
| AGAI_SHARE | 全部股东反对票数 | 数值类型 |
| AGAI_ACF | 全部股东反对票数占本次全部股东有效表决权票数比率 | 数值类型 |
| DISCL_SHARE | 全部股东弃权票数数 | 数值类型 |
| DISCL_ACF | 全部股东弃权票数占本次全部股东有效表决权票数比率 | 数值类型 |
| NON_AGRE_SHARE | 非流通股东同意票数 | 数值类型 |
| NON_AGRE_ACF | 非流通股东同意票数占本次非流通股东有效表决权票数比率 | 数值类型 |
| NON_AGAI_SHARE | 非流通股东反对票数 | 数值类型 |
| NON_AGAI_ACF | 非流通股东反对票数占本次非流通股东有效表决权票数比率 | 数值类型 |
| NON_DISCL_SHARE | 非流通股东弃权票数 | 数值类型 |
| NON_DISCL_ACF | 非流通股东弃权票数占本次非流通股东有效表决权票数比率 | 数值类型 |
| FLOAT_AGRE_SHARE | 流通股东同意票数 | 数值类型 |
| FLOAT_AGRE_ACF | 流通股东同意票数占本次流通股东有效表决权票数比率 | 数值类型 |
| FLOAT_A_AGRE_SHARE | 流通A股股东同意票数 | 数值类型 |
| FLOAT_AGAI_SHARE | 流通股东反对票数 | 数值类型 |
| FLOAT_AGAI_ACF | 流通股东反对票数占本次流通股东有效表决权票数比率 | 数值类型 |
| FLOAT_A_AGAI_SHARE | 流通A股股东反对票数 | 数值类型 |
| FLOAT_DISCL_SHARE | 流通股东弃权票数 | 数值类型 |
| FLOAT_DISCL_ACF | 流通股东弃权票数占本次流通股东有效表决权票数比率 | 数值类型 |
| FLOAT_A_DISCL_SHARE | 流通A股股东弃权票数 | 数值类型 |


