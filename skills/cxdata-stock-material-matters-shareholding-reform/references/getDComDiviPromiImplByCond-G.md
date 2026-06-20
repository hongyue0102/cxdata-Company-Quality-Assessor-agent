# 公司股改承诺实施-通用 (getDComDiviPromiImplByCond-G)

**API_ID:** getDComDiviPromiImplByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| firDeclDate | 首次公告日期 | 日期类型 | 否 |  |
| hldName | 股东名称 | 字符类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| FIR_DECL_DATE | 首次公告日期 | 日期类型 |
| LAT_DECL_DATE | 最新公告日期 | 日期类型 |
| PROMI_OBJ_PAR | 承诺主体 | 数值类型 |
| EVENT_TYPE_PAR | 事项类型 | 数值类型 |
| INFO_TYPE_PAR | 信息类别 | 数值类型 |
| HLD_NAME | 股东名称 | 字符类型 |
| PROMI_TYPE_PAR | 承诺类别 | 数值类型 |
| PROMI_START_DATE | 承诺实施日期起始 | 日期类型 |
| PROMI_END_DATE | 承诺实施日期截止 | 日期类型 |
| PROMI_PRICE | 承诺触发价格 | 数值类型 |
| VALID_DATE | 股改方案生效日期 | 日期类型 |
| CHAN_REAS_PAR | 变动原因 | 数值类型 |
| PROMI_REM | 承诺事项说明 | 字符类型 |
| END_DATE | 截止日期 | 日期类型 |
| IS_IMPL_PAR | 是否实施 | 数值类型 |
| REAS_TYPE_PAR | 原因类别 | 数值类型 |
| IMPL_REM | 实施情况说明 | 字符类型 |
| THIS_IMPL_STK_NUM | 本次实施股数 | 数值类型 |
| THIS_IMPL_AMUT | 本次实施金额 | 数值类型 |
| CUML_IMPL_STK_NUM | 累计实施股数 | 数值类型 |
| CUML_IMPL_AMUT | 累计实施金额 | 数值类型 |
| IMPL_PRICE_FLOOR | 实施价格区间起始 | 数值类型 |
| IMPL_PRICE_CELL | 实施价格区间截止 | 数值类型 |


