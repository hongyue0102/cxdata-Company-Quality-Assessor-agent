# 公司股权分置-通用 (getDComEquityDiviMainByCond-G)

**API_ID:** getDComEquityDiviMainByCond-G

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
| LAT_DECL_DATE | 最新公告日期 | 日期类型 |
| EVENT_PROC_PAR | 事件进程 | 数值类型 |
| DIVI_PUBL_DATE | 改革事项公告日期 | 日期类型 |
| DIVI_INIT_INTEN | 股改初步意向 | 字符类型 |
| CON_FAX | 传真 | 字符类型 |
| E_MAIL | 电子邮箱 | 字符类型 |
| CON_PER | 联系人 | 字符类型 |
| RECO_GUAR_ORG | 保荐机构名称 | 字符类型 |
| RECO_GUAR_ORG_HOLD | 保荐机构持股 | 数值类型 |
| DIRE_AUDIT_DATE | 董事会审议改革方案日 | 日期类型 |
| DIRE_RESO_DATE | 董事会决议公布日 | 日期类型 |
| NETW_VOTE_START_DATE | 网络投票起始日 | 日期类型 |
| NETW_VOTE_END_DATE | 网络投票截至日 | 日期类型 |
| HLD_MEET_REG_DATE | 股东大会登记日 | 日期类型 |
| HLD_MEET_DATE | 股东大会召开日 | 日期类型 |
| HLD_MEET_ADDR | 股东大会召开地址 | 字符类型 |
| VOTE_OPT_PER | 投票权征集人 | 字符类型 |
| CONF_PLAN_PUBL_DATE | 沟通确认方案公布日 | 日期类型 |
| PLAN_TYPE | 股改方案类型 | 字符类型 |
| PLAN_CHAN_TYPE_PAR | 调整方案 | 数值类型 |
| VOTE_OPT_START_DATE | 独立董事征集投票权起始日 | 日期类型 |
| VOTE_OPT_END_DATE | 独立董事征集投票权截至日 | 日期类型 |
| PLAN_APPR_ORG | 方案实施上级批准部门 | 字符类型 |
| IS_APPR_PAR | 是否获批 | 数值类型 |
| IS_OUT_CAP_APPR_PAR | 外资法人股是否获批 | 数值类型 |
| APPR_DATE | 获批日 | 日期类型 |
| STM_RESO_PUBL_DATE | 股东大会决议公布日 | 日期类型 |
| IS_CHAN_PASS_PAR | 股改方案是否通过 | 数值类型 |
| CHAN_IMPL_PUBL_DATE | 改革方案实施公告日期 | 日期类型 |
| IMPL_EQUITY_REG_DATE | 方案实施的股权登记日 | 日期类型 |
| IMPL_SUSP_DATE | 实施后停牌日 | 日期类型 |
| IMPL_TRADE_DATE | 实施后交易首日 | 日期类型 |
| CONSI_STK_PAY_DATE | 对价股票支付日 | 日期类型 |
| CONSI_STK_TRADE_DATE | 对价股票上市流通日 | 日期类型 |
| CONSI_CASH_PAY_DATE | 对价现金发放日 | 日期类型 |
| WARR_ISS_DATE | 权证发行日 | 日期类型 |
| BASE_SHARE | 基准股本 | 数值类型 |
| NON_FLOAT | 非流通股 | 数值类型 |
| NON_FLOAT_STAFF_STK | 非流通股_限期上市职工股 | 数值类型 |
| NON_FLOAT_LIST_STAFF_STK | 非流通股_暂不上市职工股 | 数值类型 |
| NON_FLOAT_OUT_STK | 非流通股_外资法人股 | 数值类型 |
| FLOAT_STK | 流通股 | 数值类型 |
| FLOAT_A | 流通A股 | 数值类型 |
| FLOAT_B | 流通B股 | 数值类型 |
| FLOAT_H | 流通H股 | 数值类型 |
| FLOAT_OTHER | 其他流通股 | 数值类型 |
| IMPL_TOT_SHARE | 方案实施后总股本 | 数值类型 |
| REST_FLOAT | 有限售条件流通股 | 数值类型 |
| REST_FLOAT_STAFF_STK | 有限售条件流通股_限期上市职工股 | 数值类型 |
| REST_FLOAT_LIST_STAFF_STK | 有限售条件流通股_暂不上市职工股 | 数值类型 |
| REST_FLOAT_OUT_STK | 有限售条件流通股_外资法人股 | 数值类型 |
| UNREST_FLOAT | 无限售条件流通股 | 数值类型 |
| UNREST_FLOAT_A | 无限售条件_流通A股 | 数值类型 |
| UNREST_FLOAT_B | 无限售条件_流通B股 | 数值类型 |
| UNREST_FLOAT_H | 无限售条件_流通H股 | 数值类型 |
| UNREST_FLOAT_OTHER | 无限售条件_其他流通股 | 数值类型 |
| COM_STO_DIV_SUM | 公司合计送转股数 | 数值类型 |
| COM_CASH_DIV_AMUT | 公司合计派现金额 | 数值类型 |
| COM_SHARE_WARR_NUM | 公司合计认股证份数 | 数值类型 |
| NON_HLD_CONSI_STK_SUM | 非流通股东对价股份总额 | 数值类型 |
| NON_HLD_CONSI_CASH_SUM | 非流通股东对价现金总额 | 数值类型 |
| NON_HLD_CONSI_WARR_SUM | 非流通股东对价认股证总额 | 数值类型 |
| NON_HLD_SHRI_STK_SUM | 非流通股东缩股总额 | 数值类型 |
| COM_PLAN_PAR | 上市公司配套方案 | 数值类型 |
| PLAN_DES | 配套方案说明 | 字符类型 |
| DIVI_REM | 备注 | 字符类型 |


