# 公司分红预案-通用 (getDComDivPlanByCond-G)

**API_ID:** getDComDivPlanByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| endDate | 截止日期 | 日期类型 | 否 |  |
| isDivPar | 是否分红 | 数值类型 | 否 |  |
| planPublDate | 预案公布日 | 日期类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| STK_TYPE_PAR | 股票类型 | 数值类型 |
| END_DATE | 截止日期 | 日期类型 |
| IS_DIV_PAR | 是否分红 | 数值类型 |
| PLAN_PUBL_DATE | 预案公布日 | 日期类型 |
| STM_RESO_PUBL_DATE | 股东大会决议公告日 | 日期类型 |
| IS_PASS_PAR | 预案是否通过 | 数值类型 |
| BASE_SHARE | 分红股本基数 | 数值类型 |
| BONUS_RATIO | 每10股/份送股 | 数值类型 |
| TRAN_ADD_RATIO | 每10股/份转增股 | 数值类型 |
| DIV_TAX_RMB | 每10股/份派现(含税/人民币) | 数值类型 |
| DIV_TAX_FC | 每10股派现(含税/外币) | 数值类型 |
| CURY_TYPE_PAR | 货币类型 | 数值类型 |
| NON_DIST_DES | 利润不分配说明 | 字符类型 |
| PLAN_CHAN_DES | 方案变动说明 | 字符类型 |
| DIV_CONT | 分红方案 | 字符类型 |


