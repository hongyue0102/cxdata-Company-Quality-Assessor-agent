# 公司分红实施-通用 (getDComDivImplByCond-G)

**API_ID:** getDComDivImplByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| endDate | 截止日期 | 日期类型 | 否 |  |
| divImpDate | 分红实施公告日 | 日期类型 | 否 |  |
| exrigheDate | 除权除息日 | 日期类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| STK_TYPE_PAR | 股票类型 | 数值类型 |
| END_DATE | 截止日期 | 日期类型 |
| DIV_IMP_DATE | 分红实施公告日 | 日期类型 |
| DIV_CONT | 分红实施内容 | 字符类型 |
| IS_DIV_PAR | 是否分红 | 数值类型 |
| DIV_OBJ_DES | 分红对象 | 字符类型 |
| BASE_SHARE | 分红股本基数 | 数值类型 |
| BONUS_RATIO | 每10股/份送股 | 数值类型 |
| TRAN_ADD_RATIO | 每10股/份转增股 | 数值类型 |
| DIV_TAX_RMB | 每10股/份派现(含税/人民币) | 数值类型 |
| DIV_RMB | 每10股/份实派(税后/人民币) | 数值类型 |
| DIV_TAX_FC | 每10股派现(含税/外币) | 数值类型 |
| DIV_FC | 每10股实派(税后/外币) | 数值类型 |
| DIV_PAY_NUM | A股(含B股)分红总额 | 数值类型 |
| CURY_TYPE_PAR | 货币类型 | 数值类型 |
| RIGHT_REG_DATE | 股权登记日 | 日期类型 |
| EXRIGHE_DATE | 除权除息日 | 日期类型 |
| SHARE_LIST_DATE | 送转股上市日 | 日期类型 |
| LAST_TRADE_DATE | 最后交易日 | 日期类型 |
| TRAN_TOT_SHARE | 送转后总股本 | 数值类型 |
| TO_ACCY_DATE | 股息到帐日期 | 日期类型 |
| BOBUS_DES | 红利发放说明 | 字符类型 |
| BONUS_START_DATE | 红利发放起始日 | 日期类型 |
| BONUS_END_DATE | 红利发放截止日 | 日期类型 |
| REM_DES | 备注 | 字符类型 |
| RIGHT_DATE_PRI | 股权登记日收盘价 | 数值类型 |
| EXRIGHE_DATE_PRI | 除权除息日收盘价 | 数值类型 |
| TOT_DIV_PAY_NUM | 全体股东分红总额 | 数值类型 |


