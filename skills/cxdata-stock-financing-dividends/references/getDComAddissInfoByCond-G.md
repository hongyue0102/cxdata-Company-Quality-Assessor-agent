# 公司增发实施-通用 (getDComAddissInfoByCond-G)

**API_ID:** getDComAddissInfoByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| eventId | 事件ID | 数值类型 | 否 |  |
| declDate | 招股意向书或招股说明书发布日期 | 日期类型 | 否 |  |
| listDeclDate | 股份变动或上市公告日期 | 日期类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| STK_TYPE_PAR | 股票类型 | 数值类型 |
| ADDISS_METH_PAR | 增发类型 | 数值类型 |
| EVENT_ID | 事件ID | 数值类型 |
| DECL_DATE | 招股意向书或招股说明书发布日期 | 日期类型 |
| ISS_START_DATE | 发行日期起始日 | 日期类型 |
| ISS_END_DATE | 发行日期截止日 | 日期类型 |
| SUS_START_DATE | 停牌时间起始日 | 日期类型 |
| SUS_END_DATE | 停牌时间截止日 | 日期类型 |
| RIGHT_REG_DATE | 股权登记日 | 日期类型 |
| EXRI_DATE | 除权日 | 日期类型 |
| LIST_DECL_DATE | 股份变动或上市公告日期 | 日期类型 |
| LIST_DATE | 增发股份上市日期 | 日期类型 |
| PAR_VAL | 每股面值(人民币) | 数值类型 |
| ISS_PRI_METH | 发行定价方式说明 | 字符类型 |
| ISS_OBJ | 发行对象 | 字符类型 |
| UNDE_METH_PAR | 承销方式 | 数值类型 |
| UNDE_START_DATE | 承销期起始日 | 日期类型 |
| UNDE_END_DATE | 承销期截止日 | 日期类型 |
| ISS_PRICE_RMB | 每股发行价(人民币) | 数值类型 |
| ISS_PRICE_FC | 每股发行价(外币) | 数值类型 |
| CURY_TYPE_PAR | 货币类型 | 数值类型 |
| IS_EXRI_PAR | 是否除权 | 数值类型 |
| HLD_PLACE_RATE | 老股东优先配售比例(10配X) | 数值类型 |
| HLD_PLACE_CODE | 老股东优先配售申购代码 | 字符类型 |
| HLD_PLACE_NAME | 老股东优先配售申购简称 | 字符类型 |
| HLD_APPL_DOOR | 老股东有效申购户数 | 数值类型 |
| HLD_APPL_DOOR_ON | 老股东网上有效申购户数 | 数值类型 |
| HLD_APPL_DOOR_OFF | 老股东网下有效申购户数 | 数值类型 |
| HLD_PLACE_RATIO | 老股东配售中签率 | 数值类型 |
| ONLINE_START_DATE | 网上申购起始日 | 日期类型 |
| ONLINE_END_DATE | 网上申购截止日 | 日期类型 |
| ONLINE_CAP_DATE | 网上申购资金解冻日 | 日期类型 |
| ONLINE_APPL_CODE | 网上发行申购代码 | 字符类型 |
| ONLINE_APPL_ABBR | 网上发行申购简称 | 字符类型 |
| ONLINE_APPL_UNIT | 网上发行申购单位 | 数值类型 |
| ONLINE_APPL_CEIL | 网上发行申购上限 | 数值类型 |
| ONLINE_APPL_FLOOR | 网上发行申购下限 | 数值类型 |
| ONLINE_APPL_VOL | 网上有效申购总量 | 数值类型 |
| ONLINE_APPL_DOOR | 网上有效申购户数 | 数值类型 |
| ONLINE_SUBS_MULT | 网上超额认购倍数 | 数值类型 |
| ONLINE_ISS_RATIO | 网上中签率 | 数值类型 |
| OFFLINE_START_DATE | 网下配售申购起始日 | 日期类型 |
| OFFLINE_END_DATE | 网下配售申购截止日 | 日期类型 |
| OFFLINE_CAP_DATE | 网下申购资金退款日 | 日期类型 |
| LEG_APPL_UNIT | 法人网下配售认购单位 | 数值类型 |
| LEG_APPL_FLOOR | 法人网下配售申购下限 | 数值类型 |
| LEG_APPL_CEIL | 法人网下配售申购上限 | 数值类型 |
| PLACE_APPL_VOL | 法人网下配售有效申购总量 | 数值类型 |
| A_PLACE_APPL_VOL | A类法人网下配售有效申购总量 | 数值类型 |
| B_PLACE_APPL_VOL | B类法人网下配售有效申购总量 | 数值类型 |
| PLACE_APPL_DOOR | 法人网下配售有效申购户数 | 数值类型 |
| A_PLACE_APPL_DOOR | A类法人网下配售有效申购户数 | 数值类型 |
| B_PLACE_APPL_DOOR | B类法人网下配售有效申购户数 | 数值类型 |
| PLACE_RATIO | 法人网下配售中签率 | 数值类型 |
| A_PLACE_RATIO | A类法人网下配售中签率 | 数值类型 |
| B_PLACE_RATIO | B类法人网下配售中签率 | 数值类型 |
| PLACE_SUBS_MULT | 法人网下配售超额认购倍数 | 数值类型 |
| HOLD_LOCK_DES | 持股锁定期说明 | 字符类型 |
| ISS_VOL | 实际发行量 | 数值类型 |
| FUND_PLACE_VOL | *投资基金配售股数 | 数值类型 |
| STATE_ISS_VOL | *国有股存量发行股数 | 数值类型 |
| HLD_ACTU_VOL | 老股东实际配售股数 | 数值类型 |
| HLD_ACTU_VOL_ON | 其中：老股东网上实际配售股数 | 数值类型 |
| HLD_ACTU_VOL_OFF | 其中：老股东网下实际配售股数 | 数值类型 |
| ONLINE_ISS_VOL | 网上公开发行股数 | 数值类型 |
| PLACE_ACTU_VOL | 法人网下实际配售股数 | 数值类型 |
| A_PLACE_ACTU_VOL | 其中：A类法人网下实际配售股数 | 数值类型 |
| B_PLACE_ACTU_VOL | 其中：B类法人网下实际配售股数 | 数值类型 |
| CALL_BACK_VOL | 网上网下回拨股数 | 数值类型 |
| SURP_UNDE_VOL | 余股包销数量 | 数值类型 |
| LIST_VOL | 本次上市流通股数 | 数值类型 |
| CAP_AMUT_RMB | 募集资金总额(人民币) | 数值类型 |
| CAP_AMUT_FC | 募集资金总额(外币) | 数值类型 |
| CAP_NET_AMUT_RMB | 募集资金净额(人民币) | 数值类型 |
| CAP_NET_AMUT_FC | 募集资金净额(外币元) | 数值类型 |
| TO_ACCOUNT_DATE | 募集资金到帐日期 | 日期类型 |
| ISS_COST_RMB | 发行费用总额(人民币) | 数值类型 |
| ISS_COST_FC | 发行费用总额(外币) | 数值类型 |
| ISS_COST_PER_RMB | 每股发行费用(人民币) | 数值类型 |
| ISS_COST_PER_FC | 每股发行费用(外币) | 数值类型 |
| UNDE_SPON_FEE | 承销及保荐费用 | 数值类型 |
| LAW_FEE | 律师费用 | 数值类型 |
| CPA_FEE | 会计师费用 | 数值类型 |
| AUDI_FEE | 审计评估及验资费 | 数值类型 |
| REG_FEE | 股份托管登记费用 | 数值类型 |
| ISS_PRO_FEE | 发行手续费用 | 数值类型 |
| MAIN_UNDE | 主承销商 | 字符类型 |
| CO_MAIN_UNDE | 副主承销商 | 字符类型 |
| LIST_SPON | 上市推荐人 | 字符类型 |
| RECO_GUAR | 保荐人 | 字符类型 |
| ISS_LAW | 发行人法律顾问 | 字符类型 |
| CERT_ACC | 会计师事务所 | 字符类型 |
| ASE_ESTI | 资产评估机构 | 字符类型 |
| STK_REG | 股票登记机构 | 字符类型 |
| COLL_ORG | 收款机构 | 字符类型 |
| CAP_DES | 募集资金用途简述 | 字符类型 |


