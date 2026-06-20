# A股首次发行与上市-通用 (getDComIpoInfoAByCond-G)

**API_ID:** getDComIpoInfoAByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| eventId | 事件ID | 数值类型 | 否 |  |
| intentPublDate | 招股意向书发布日期 | 日期类型 | 否 |  |
| issStartDate | 发行起始日 | 日期类型 | 否 |  |
| resuDeclDate | 发行结果公告日期 | 日期类型 | 否 |  |
| declDate | 上市公告日期 | 日期类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| EVENT_ID | 事件ID | 数值类型 |
| INTENT_PUBL_DATE | 招股意向书发布日期 | 日期类型 |
| DES_PUBL_DATE | 招股说明书发布日期 | 日期类型 |
| ISS_START_DATE | 发行起始日 | 日期类型 |
| ISS_END_DATE | 发行截止日 | 日期类型 |
| ONLINE_START_DATE | 网上申购起始日 | 日期类型 |
| ONLINE_END_DATE | 网上申购截止日 | 日期类型 |
| ONLINE_CAP_DATE | 网上申购资金解冻日 | 日期类型 |
| OFFLINE_START_DATE | 网下申购起始日 | 日期类型 |
| OFFLINE_END_DATE | 网下申购截止日 | 日期类型 |
| OFFLINE_CAP_DATE | 网下申购资金退款日 | 日期类型 |
| RESU_DECL_DATE | 发行结果公告日期 | 日期类型 |
| DECL_DATE | 上市公告日期 | 日期类型 |
| LIST_DATE | 上市日期 | 日期类型 |
| PAR_VAL | 每股面值 | 数值类型 |
| ISS_METH | 发行方式 | 字符类型 |
| ISS_PRI_METH | 发行价定价方式 | 字符类型 |
| ISS_OBJ | 发行对象 | 字符类型 |
| HLD_PRO_DES | 发行前股东持股限制及股东自愿锁定承诺 | 字符类型 |
| UNDE_METH_PAR | 承销方式 | 数值类型 |
| UNDE_START_DATE | 承销期起始日 | 日期类型 |
| UNDE_END_DATE | 承销期截止日 | 日期类型 |
| PRICE_CEIL_RMB | 计划发行价上限 | 数值类型 |
| PRICE_FLOOR_RMB | 计划发行价下限 | 数值类型 |
| ISS_VOL_CEIL | 计划发行量上限 | 数值类型 |
| ISS_VOL_FLOOR | 计划发行量下限 | 数值类型 |
| ONLINE_ISS_PLAN | 网上计划发行量 | 数值类型 |
| OFFLINE_ISS_PLAN | 网下配售计划发行量 | 数值类型 |
| STRA_ISS_PLAN | 战略配售计划发行量 | 数值类型 |
| ORIENT_ISS_PLAN | 定向配售计划发行量 | 数值类型 |
| ISS_PRICE_RMB | 每股/份发行价 | 数值类型 |
| NAPS_BEFORE_ISS | 发行前每股净资产 | 数值类型 |
| NAPS_AFTER_ISS | 发行后每股净资产 | 数值类型 |
| PE_BEF | 发行前市盈率 | 数值类型 |
| PE_DILU_AFTER | 发行后市盈率(全面摊薄) | 数值类型 |
| PE_WEIGH_AFTER | 发行后市盈率(加权平均) | 数值类型 |
| ROAD_START_DATE | 路演开始日期 | 日期类型 |
| ROAD_END_DATE | 路演截止日期 | 日期类型 |
| ROAD_WEB | 路演网站 | 字符类型 |
| ONLINE_APPL_CODE | 网上发行申购代码 | 字符类型 |
| ONLINE_APPL_ABBR | 网上发行申购简称 | 字符类型 |
| ONLINE_APPL_UNIT | 网上发行认购单位 | 数值类型 |
| ONLINE_APPL_CEIL | 网上发行申购上限 | 数值类型 |
| ONLINE_APPL_FLOOR | 网上发行申购下限 | 数值类型 |
| OFFLINE_APPL_CODE | 网下配售申购代码 | 字符类型 |
| OFFLINE_APPL_ABBR | 网下配售申购简称 | 字符类型 |
| OFFLINE_APPL_UNIT | 网下配售认购单位 | 数值类型 |
| OFFLINE_APPL_CEIL | 网下配售申购上限 | 数值类型 |
| OFFLINE_APPL_FLOOR | 网下配售申购下限 | 数值类型 |
| ONLINE_APPL_VOL | 网上发行有效申购总量 | 数值类型 |
| ONLINE_FRZ_CAP | 网上发行冻结资金 | 数值类型 |
| ONLINE_APPL_DOOR | 网上发行有效申购户数 | 数值类型 |
| ONLINE_SUBS_MULT | 网上发行超额认购倍数 | 数值类型 |
| ONLINE_ISS_RATIO | 网上发行中签率 | 数值类型 |
| OFFLINE_BID_NUM_N | 网下初步询价询价配售对象家数 | 数值类型 |
| OFFLINE_UNM_VALID | 网下初步询价提供有效报价配售家数 | 数值类型 |
| OFFLINE_APPL_VOL | 网下配售有效申购总量 | 数值类型 |
| OFFLINE_APPL_CAP | 网下配售有效申购资金 | 数值类型 |
| OFFLINE_FRZ_CAP | 网下配售冻结资金 | 数值类型 |
| OFFLINE_APPL_DOOR | 网下配售有效申购户数 | 数值类型 |
| OFFLINE_SUBS_MULT | 网下配售超额认购倍数 | 数值类型 |
| OFFLINE_PLACE_RATIO | 网下配售中签率 | 数值类型 |
| SEC_PLACE_RATIO | *二级市场配售中签率 | 数值类型 |
| HOLD_LOCK_DES | 持股锁定期说明 | 字符类型 |
| HOLD_LOCK | 持股锁定期限 | 数值类型 |
| ISS_VOL | 实际发行量 | 数值类型 |
| STATE_ISS_VOL | 其中：*国有股存量发行股数 | 数值类型 |
| FUND_PLACE_VOL | 其中：*投资基金优先配售股数 | 数值类型 |
| SEC_ACTU_PLACE_VOL | 其中：*二级市场实际配售股数 | 数值类型 |
| STAFF_PLACE_VOL | 其中：*公司职工配售股数 | 数值类型 |
| ONLINE_ISS_VOL | 其中：网上实际发行股数 | 数值类型 |
| OFFLINE_ACTU_VOL | 其中：网下实际配售股数 | 数值类型 |
| STRA_PLACE_VOL | 其中：向战略投资者配售数量 | 数值类型 |
| LEG_ORI_VOL | 其中：法人定向配售数量 | 数值类型 |
| ORIENT_PLACE_VOL | 其中：其它定向配售股数 | 数值类型 |
| ORIENT_PLACE_RES | 定向配售结果说明 | 字符类型 |
| SURP_UNDE_VOL | 余股包销数量 | 数值类型 |
| SUBS_PLACE_VOL | 发行时超额配售股数 | 数值类型 |
| CALLBACK_VOL | 网上网下回拨数量 | 数值类型 |
| OPT_PUBL_DATE | 绿鞋行使情况公告日 | 日期类型 |
| OPT_START_DATE | 绿鞋行使起始日 | 日期类型 |
| OPT_END_DATE | 绿鞋行使截止日 | 日期类型 |
| SEC_BUY_VOL | 二级市场买入股数 | 数值类型 |
| ISS_SUP_VOL | 绿鞋行使超额配售股数 | 数值类型 |
| IPO_FLOAT | 本次上市流通股数 | 数值类型 |
| CAP_AMUT_RMB | 募集资金总额 | 数值类型 |
| CAP_NET_AMUT_RMB | 募集资金净额 | 数值类型 |
| TO_ACCOUNT_DATE | 募集资金到帐日期 | 日期类型 |
| ISS_COST_RMB | 发行费用总额 | 数值类型 |
| FEE_DES | 发行费用说明 | 字符类型 |
| UNDE_FEE | 其中：承销费用 | 数值类型 |
| SPON_FEE | 其中：保荐费用 | 数值类型 |
| UNDE_SPON_FEE | 其中：承销及保荐费用 | 数值类型 |
| LAW_FEE | 其中：律师费用 | 数值类型 |
| TAX_FEE | 其中：印花税 | 数值类型 |
| CPA_FEE | 其中：会计师费用 | 数值类型 |
| AUDI_FEE | 其中：审计评估及验资费 | 数值类型 |
| REG_FEE | 其中：股份托管登记费用 | 数值类型 |
| ISS_PRO_FEE | 其中：发行手续费用 | 数值类型 |
| INFO_DEL_FEE | 其中：信息披露费 | 数值类型 |
| MAIN_UNDE | 主承销商 | 字符类型 |
| CO_MAIN_UNDE | 副主承销商 | 字符类型 |
| RECO_GUAR | 保荐人 | 字符类型 |
| RECO_GUAR_REP | 保荐代表人 | 字符类型 |
| ISS_LAW | 发行人法律顾问 | 字符类型 |
| ISS_LAW_RES | 发行人法律顾问经办人 | 字符类型 |
| UNDE_LAW | 承销商法律顾问 | 字符类型 |
| UNDE_LAW_RES | 承销商法律顾问经办人 | 字符类型 |
| CERT_ACC | 会计师事务所 | 字符类型 |
| CERT_ACC_RES | 会计师事务所经办人 | 字符类型 |
| ASE_ESTI | 资产评估机构 | 字符类型 |
| ASE_ESTI_RES | 资产评估机构经办人 | 字符类型 |
| LAND_ESTI | 土地评估机构 | 字符类型 |
| LAND_ESTI_RES | 土地评估机构经办人 | 字符类型 |
| STK_REG | 股票登记机构 | 字符类型 |
| COLL_ORG | 收款机构 | 字符类型 |
| BANK_ACCO | 收款账号 | 字符类型 |
| ISS_INDIV_TAX | 发行时所得税税率 | 数值类型 |
| ISS_INDIV_PAR | 发行时所得税税率类型 | 数值类型 |
| VAL_CURY_TYPE_PAR | 面值货币类型参数 | 数值类型 |
| OFFLINE_ABA_SUB_QUA | 网下放弃认购数量 | 数值类型 |
| ONLINE_ABA_SUB_QUA | 网上放弃认购数量 | 数值类型 |
| WIN_NUM_DECL_DATE | 中签号公告日 | 日期类型 |
| WIN_CON_DATE | 中签缴款日期 | 日期类型 |
| ISS_DECL_DATE | 发行公告日期 | 日期类型 |
| COU_START_DATE | 询价起始日 | 日期类型 |
| COU_END_DATE | 询价截止日 | 日期类型 |
| TOT_CAP_CEIL | 计划募集资金总额 | 字符类型 |
| NET_CAP_CEIL | 计划募集资金净额 | 字符类型 |


