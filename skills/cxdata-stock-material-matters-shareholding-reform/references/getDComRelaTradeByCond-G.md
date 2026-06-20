# 公司日常经营关联交易-通用 (getDComRelaTradeByCond-G)

**API_ID:** getDComRelaTradeByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| endDate | 截止日期 | 日期类型 | 否 |  |
| relaObjName | 关联方名称 | 字符类型 | 否 |  |
| tradeTypePar | 交易类型 | 数值类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| DECL_DATE | 公告日期 | 日期类型 |
| END_DATE | 截止日期 | 日期类型 |
| RELA_OBJ_NAME | 关联方名称 | 字符类型 |
| TRADE_TYPE_PAR | 交易类型 | 数值类型 |
| THIS_TRADE_AMUT | 本期交易金额 | 数值类型 |
| THIS_ACF_AMUT | 本期发生额占比 | 数值类型 |
| PRI_PAR | 定价原则 | 数值类型 |
| CURY_TYPE_PAR | 货币类型 | 数值类型 |
| CAP_COST | 资金费用 | 数值类型 |
| INTE | 利率 | 字符类型 |
| END_BALA | 期末余额 | 数值类型 |
| TRA_NUM | 本年交易笔数 | 字符类型 |
| TRA_PRI | 交易价格 | 字符类型 |
| TRA_DATE | 交易日期 | 字符类型 |
| TRA_LIMI | 交易期限 | 字符类型 |
| TRA_RELA_BANK | 交易涉及的银行 | 字符类型 |
| TRA_CONT | 交易内容 | 字符类型 |
| IF_INFL_PROF | 是否影响公司利润 | 数值类型 |
| INFL_PROF | 交易事项对公司利润的影响 | 字符类型 |
| REM_DES | 备注 | 字符类型 |


