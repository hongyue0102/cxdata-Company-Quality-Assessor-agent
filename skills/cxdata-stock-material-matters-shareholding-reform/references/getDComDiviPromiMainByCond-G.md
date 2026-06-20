# 公司股改股东承诺-通用 (getDComDiviPromiMainByCond-G)

**API_ID:** getDComDiviPromiMainByCond-G

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
| LAT_DECL_DATE | 最新公告日期 | 日期类型 |
| PROMI_SBJ_TYPE_PAR | 承诺主体类型 | 数值类型 |
| EVENT_TYPE_PAR | 事项类型 | 数值类型 |
| IS_VALID_PAR | 是否有效 | 数值类型 |
| HLD_NAME | 股东名称 | 字符类型 |
| PAY_CONSI_STK_SUM | 直接支付对价股份总额 | 数值类型 |
| PAY_CONSI_CASH_SUM | 直接支付对价现金总额 | 数值类型 |
| PAY_CONSI_WARR_SUM | 直接支付对价认股证总额 | 数值类型 |
| SHRI_STK_SUM | 缩股总额 | 数值类型 |
| CONV_CONSI_STK_SUM | 转付对价股份总额 | 数值类型 |
| CONV_CONSI_CASH_SUM | 转付对价现金总额 | 数值类型 |
| OTHER_CONSI_REM | 其他对价说明 | 字符类型 |
| CONSI_PRE_PAY_HOLD | 对价支付前持股数 | 数值类型 |
| PRE_PAY_FLOAT_A | 对价支付前持流通A股股数 | 数值类型 |
| SHARE_ATTR_PAR | 股本性质 | 数值类型 |
| CONSI_PRE_PAY_RATIO | 对价支付前持股比例 | 数值类型 |
| PLE_STK_NUM | 质押股份数量 | 数值类型 |
| FRZ_STK_NUM | 冻结股份数量 | 数值类型 |
| CONSI_AFTER_PAY_HOLD | 对价支付后持股数 | 数值类型 |
| UNRESTC_FLOAT_A | 对价支付后持有无限售流通A股股数 | 数值类型 |
| CONSI_AFTER_PAY_RATIO | 对价支付后持股比例 | 数值类型 |
| LIST_DATE | 上市流通日期 | 日期类型 |
| PROMI_RESTC_REM | 获流通权后承诺限售期限 | 数值类型 |
| RESTC_MATU_REM | 限售期限说明 | 字符类型 |
| PROMI_RATIO_FLOOR | 获流通权后承诺持股比例下限 | 数值类型 |
| PROMI_FLOOR_MATU | 获流通权后最低持股比例承诺期限 | 数值类型 |
| PROMI_FLOOR_END_DATE | 获流通权后最低持股比例截止日 | 日期类型 |
| FIR_CELL_ACF_TOT | 首期出售股份比例上限占总股本(限售期满后) | 数值类型 |
| FIR_CELL_ACF_HOLD | 首期出售股份比例上限占所持有股本(限售期满后) | 数值类型 |
| FIR_PROMI_MATU | 首期出售承诺期限(限售期满后) | 数值类型 |
| SECO_CELL_ACF_TOT | 二期出售股份比例上限占总股本(限售期满后起) | 数值类型 |
| SECO_CELL_ACF_HOLD | 二期出售股份比例上限占所持有股本(限售期满后) | 数值类型 |
| SECO_PROMI_MATU | 二期出售承诺期限(限售期满后起) | 数值类型 |
| PROMI_REST_PRICE | 承诺限制上市触发价格 | 数值类型 |
| LIST_PRICE_DES | 上市价格条件描述 | 字符类型 |
| LIST_PRICE_COND_PAR | 上市价格条件 | 数值类型 |
| LIST_PRICE_MATU_DES | 上市价格期限描述 | 字符类型 |
| LIST_PRICE_VALID_MATU | 上市触发价格有效期限(限售期满后) | 数值类型 |
| LIST_PRICE_END_DATE | 上市触发价格有效期限截止 | 日期类型 |
| LIST_PROMI_REM | 上市承诺说明 | 字符类型 |
| INCRE_TIME_DES | 增持时间描述 | 字符类型 |
| INCRE_START_TYPE_PAR | 增持起始日期类别 | 数值类型 |
| INCRE_MATU | 增持实施期限 | 数值类型 |
| INCRE_PRICE_DES | 增持价格描述 | 字符类型 |
| INCRE_PRICE | 增持股票触发价格 | 数值类型 |
| INCRE_PRICE_COND_PAR | 增持价格条件 | 数值类型 |
| INCRE_SIZE_DES | 增持规模描述 | 字符类型 |
| INCRE_NUM_CELL | 增持股份数量上限 | 数值类型 |
| INCRE_ACF_TOT | 增持比例上限占总股本 | 数值类型 |
| INCRE_CAP_CELL | 增持投入资金上限 | 数值类型 |
| INCRE_RESTC_MATU | 增持股份限售期限 | 数值类型 |
| INCRE_PLAN_DES | 增持计划说明 | 字符类型 |
| SALE_TIME_DES | 出售权实施时间描述 | 字符类型 |
| SALE_START_TYPE_PAR | 出售权起始日期类别 | 数值类型 |
| SALE_MATU | 出售权实施期限 | 数值类型 |
| SALE_COND_DES | 出售权实施条件描述 | 字符类型 |
| SALE_PARICE | 出售权触发价格 | 数值类型 |
| SALE_PRICE_COND_PAR | 出售权价格条件 | 数值类型 |
| SALE_SIZE_DES | 出售权实施规模描述 | 字符类型 |
| SALE_ACF_FLOAT | 出售权股份比例占流通股 | 数值类型 |
| SALE_IMPL_PRICE | 出售权实施价格 | 数值类型 |
| SALE_DES | 出售权说明 | 字符类型 |
| GRANT_TIME_DES | 追送时间描述 | 字符类型 |
| GRANT_START_TYPE_PAR | 追送起始日期类别 | 数值类型 |
| GRANT_MATU | 追送实施期限 | 数值类型 |
| GRANT_COND_REM | 追送触发条件说明 | 字符类型 |
| GRANT_SIZE_DES | 追送规模描述 | 字符类型 |
| GRANT_RATIO | 追送比例(10送X)流通股获付 | 数值类型 |
| GRANT_STK_NUM | 追送股数 | 数值类型 |
| GRANT_ACF_HOLD | 追送占股东持股比例 | 数值类型 |
| GRANT_TIME | 追送次数 | 数值类型 |
| GRANT_REM | 追送说明 | 字符类型 |
| BAL_TIME_DES | 差额支付时间描述 | 字符类型 |
| BAL_START_DATE_TYPE_PAR | 差额支付起始日期类别 | 数值类型 |
| BAL_MATU | 差额支付实施期限 | 数值类型 |
| BAL_COND_DES | 差额支付条件描述 | 字符类型 |
| BAL_PRICE | 差额支付触发价格 | 数值类型 |
| BAL_PRICE_COND_PAR | 差额支付价格条件 | 数值类型 |
| BAL_AMUT_DES | 差额支付金额描述 | 字符类型 |
| BAL_STK_SUM | 差额支付涉及股数 | 数值类型 |
| BAL_PAY_REM | 差额支付说明 | 字符类型 |
| INCE_TIME_DES | 股权激励实施时间描述 | 字符类型 |
| INCE_COND_DES | 股权激励实施条件描述 | 字符类型 |
| PRE_CONSI_INCE | 支付对价前股权激励股数 | 数值类型 |
| AFTER_CONSI_INCE | 支付对价后股权激励股数 | 数值类型 |
| SUBS_PRICE | 认购价格 | 数值类型 |
| SUBS_PRICE_COND_PAR | 认购价格条件 | 数值类型 |
| EXER_PRICE | 行权价格 | 数值类型 |
| INCE_REM | 股权激励说明 | 字符类型 |
| INV_STK_SUM | 涉及股数 | 数值类型 |
| RESTC_STA_PAR | 限售状态(承诺时) | 数值类型 |
| DEFER_MATU | 延长锁定期限 | 数值类型 |
| MATU_END_DATE | 锁定期限截止 | 日期类型 |
| DIV_PROMI_REM | 分红承诺说明 | 字符类型 |
| GOOL_PROMI_REM | 违约承诺说明 | 字符类型 |
| OTHER_PROMI_REM | 其他承诺说明 | 字符类型 |
| PLAN_TYPE | 承诺类型 | 字符类型 |


