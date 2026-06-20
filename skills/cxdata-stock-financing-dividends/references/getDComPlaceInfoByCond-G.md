# 公司配股实施-通用 (getDComPlaceInfoByCond-G)

**API_ID:** getDComPlaceInfoByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| declDate | 配股说明书公告日期 | 日期类型 | 否 |  |
| eventId | 事件ID | 数值类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| STK_TYPE_PAR | 股票类型 | 数值类型 |
| DECL_DATE | 配股说明书公告日期 | 日期类型 |
| PLACE_YEAR | 配股年度 | 数值类型 |
| EVENT_ID | 事件ID | 数值类型 |
| PAR_VAL | 每股面值(人民币) | 数值类型 |
| PLACE_PRICE_RMB | 每股配股价格(人民币) | 数值类型 |
| PLACE_PRICE_FC | 每股配股价格(外币) | 数值类型 |
| BASE_SHARE | 配股股本基数 | 数值类型 |
| ATCU_PLACE_RATIO | 实际配股比例(10配X) | 数值类型 |
| PRI_METH_PAR | 配股价格确定方式 | 数值类型 |
| PRI_METH_DES | 配股价格确定方式说明 | 字符类型 |
| CURY_TYPE_PAR | 货币类型 | 数值类型 |
| PLACE_METH | 配股发行方式 | 字符类型 |
| PLACE_OBJ | 配股对象 | 字符类型 |
| PLAN_PLACE_VOL | 计划配股数量 | 数值类型 |
| UNDE_METH_PAR | 承销方式 | 数值类型 |
| UNDE_START_DATE | 承销期起始日 | 日期类型 |
| UNDE_END_DATE | 承销期截止日 | 日期类型 |
| PLACE_ABBR | 配股简称 | 字符类型 |
| PLACE_CODE | 配股代码 | 字符类型 |
| TRAN_PLACE_RATIO | *转配比(10转配X) | 数值类型 |
| TRAN_PLACE_RMB | *转配价格 | 数值类型 |
| TRAN_PLACE_UNDE_METH_PAR | *转配股承销方式 | 数值类型 |
| TRAN_PLACE_FEE | *每股转配费 | 数值类型 |
| TRAN_PLACE_RADE_DATE | *转配股交易日期 | 日期类型 |
| TRAN_PLACE_RADE_CODE | *转配股交易代码 | 字符类型 |
| TRAN_PLACE_VOL | *转配股 | 数值类型 |
| STATE_TRAN_PLACE_VOL | *其中：国家股转配股数 | 数值类型 |
| LEG_PER_TRAN_VOL | *其中：法人股转配股数 | 数值类型 |
| COLL_LEG_PER_VOL | *其中：募集法人股转配股数 | 数值类型 |
| STATE_LEG_PER_VOL | *其中：国有法人股转配股数 | 数值类型 |
| STAFF_TRAN_PLACE_VOL | *其中：内部职工股 | 数值类型 |
| STOP_TRUSTEE_DATE | *停止托管日 | 日期类型 |
| TRAN_TRUSTEE_DATE | *转托管日 | 日期类型 |
| LAST_TRADE_DATE | 最后交易日 | 日期类型 |
| RIGHT_REG_DATE | 股权登记日 | 日期类型 |
| EXRIGHT_DATE | 除权日 | 日期类型 |
| PAY_START_DATE | 配股交款起始日 | 日期类型 |
| PAY_END_DATE | 配股交款截止日 | 日期类型 |
| LARG_HLD_DES | 大股东认配说明 | 字符类型 |
| PLACE_RESU_DES | 配售结果说明 | 字符类型 |
| ACTU_PLACE_VOL | 实际配股数量 | 数值类型 |
| REST_HLD_VOL | 有限售条件股东配售数量 | 数值类型 |
| NON_HLD_VOL | 无限售条件股东配售数量 | 数值类型 |
| SURP_UNDE_VOL | 余股包销数量 | 数值类型 |
| LIST_DECL_DATE | 上市公告日期 | 日期类型 |
| LIST_DATE | 配股上市日期 | 日期类型 |
| CAP_AMUT_RMB | 募集资金总额(人民币) | 数值类型 |
| CAP_AMUT_FC | 募集资金总额(外币) | 数值类型 |
| CAP_NET_AMUT_RMB | 募集资金净额(人民币) | 数值类型 |
| CAP_NET_AMUT_FC | 募集资金净额(外币) | 数值类型 |
| TO_ACCOUNT_DATE | 募集资金到帐日期 | 日期类型 |
| ISS_COST_RMB | 发行费用总额(人民币) | 数值类型 |
| ISS_COST_FC | 发行费用总额(外币) | 数值类型 |
| FEE_DES | 发行费用说明 | 字符类型 |
| MAIN_UNDE | 主承销商 | 字符类型 |
| CO_MAIN_UNDE | 副主承销商 | 字符类型 |
| RECO_GUAR | 保荐人 | 字符类型 |
| RECO_GUAR_REP | 保荐代表人 | 字符类型 |
| ISS_LAW | 发行人法律顾问 | 字符类型 |
| ISS_LAW_RES | 发行人法律顾问经办人 | 字符类型 |
| CERT_ACC | 会计师事务所 | 字符类型 |
| CERT_ACC_RES | 会计师事务所经办人 | 字符类型 |
| ASE_ESTI | 资产评估机构 | 字符类型 |
| ASE_ESTI_RES | 资产评估机构经办人 | 字符类型 |
| STK_REG | 股票登记机构 | 字符类型 |
| COLL_ORG | 收款机构 | 字符类型 |


