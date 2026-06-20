# B股首次发行与上市-通用 (getDComIpoInfoBByCond-G)

**API_ID:** getDComIpoInfoBByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| eventId | 事件ID | 数值类型 | 否 |  |
| declDate | 上市公告日期 | 日期类型 | 否 |  |
| listDate | 上市日期 | 日期类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| EVENT_ID | 事件ID | 数值类型 |
| DES_PUBL_DATE | 招股说明书发布日期 | 日期类型 |
| PAR_VAL | 每股面值(人民币) | 数值类型 |
| ISS_VOL_CEIL | 计划发行量上限 | 数值类型 |
| ISS_VOL_FLOOR | 计划发行量下限 | 数值类型 |
| ISS_METH | 发行方式 | 字符类型 |
| ISS_OBJ | 发行对象 | 字符类型 |
| UNDE_METH_PAR | 承销方式 | 数值类型 |
| UNDE_START_DATE | 承销期起始日 | 日期类型 |
| UNDE_END_DATE | 承销期截止日 | 日期类型 |
| ISS_PRICE_RMB | 每股发行价(人民币) | 数值类型 |
| ISS_PRICE_FC | 每股发行价(外币) | 数值类型 |
| CURY_TYPE_PAR | 货币类型 | 数值类型 |
| ISS_START_DATE | 发行起始日 | 日期类型 |
| ISS_END_DATE | 发行截止日 | 日期类型 |
| PE_DILU_AFTER | 发行后市盈率(全面摊薄) | 数值类型 |
| PE_WEIGH_AFTER | 发行后市盈率(加权平均) | 数值类型 |
| ROAD_START_DATE | 路演开始日期 | 日期类型 |
| ROAD_END_DATE | 路演截止日期 | 日期类型 |
| ROAD_WEB | 路演网站 | 字符类型 |
| ISS_VOL | 实际发行量 | 数值类型 |
| STRA_PLACE_VOL | 向战略投资者配售数量 | 数值类型 |
| SUBS_PLACE_VOL | 发行时超额配售股数 | 数值类型 |
| SURP_UNDE_VOL | 余股包销数量 | 数值类型 |
| DECL_DATE | 上市公告日期 | 日期类型 |
| LIST_DATE | 上市日期 | 日期类型 |
| IPO_FLOAT | 本次上市流通股数 | 数值类型 |
| CAP_AMUT_RMB | 募集资金总额(人民币) | 数值类型 |
| CAP_AMUT_FC | 募集资金总额(外币) | 数值类型 |
| CAP_NET_AMUT_RMB | 募集资金净额(人民币) | 数值类型 |
| CAP_NET_AMUT_FC | 募集资金净额(外币) | 数值类型 |
| TO_ACCOUNT_DATE | 募集资金到帐日期 | 日期类型 |
| ISS_COST_RMB | 发行费用总额(人民币) | 数值类型 |
| ISS_COST_FC | 发行费用总额(外币) | 数值类型 |
| ISS_COST_PER_RMB | 每股发行费用(人民币) | 数值类型 |
| ISS_COST_PER_FC | 每股发行费用(外币) | 数值类型 |
| MAIN_UNDE | 主承销商 | 字符类型 |
| CO_MAIN_UNDE | 副主承销商 | 字符类型 |
| LIST_SPON | 上市推荐人 | 字符类型 |
| INTER_COORD | 国际协调人 | 字符类型 |
| ISS_LAW | 发行人法律顾问 | 字符类型 |
| ISS_LAW_RES | 发行人法律顾问经办人 | 字符类型 |
| UNDE_LAW | 承销商法律顾问 | 字符类型 |
| UNDE_LAW_RES | 承销商法律顾问经办人 | 字符类型 |
| UNDE_LAW_OUTSIDE | 承销商境外法律顾问 | 字符类型 |
| UNDE_LAW_OUTSIDE_RES | 承销商境外法律顾问经办人 | 字符类型 |
| CERT_ACC | 会计师事务所 | 字符类型 |
| CERT_ACC_RES | 会计师事务所经办人 | 字符类型 |
| CERT_ACC_OUTSIDE | 境外会计师事务所 | 字符类型 |
| CERT_ACC_OUTSIDE_RES | 境外会计师事务所经办人 | 字符类型 |
| ASE_ESTI | 资产评估机构 | 字符类型 |
| ASE_ESTI_RES | 资产评估机构经办人 | 字符类型 |
| LAND_ESTI | 土地评估机构 | 字符类型 |
| LAND_ESTI_RES | 土地评估机构经办人 | 字符类型 |
| STK_REG | 股票登记机构 | 字符类型 |
| COLL_ORG | 收款机构 | 字符类型 |
| BANK_ACCO | 收款账号 | 字符类型 |
| ISS_INDIV_TAX | 发行时所得税税率 | 数值类型 |
| ISS_INDIV_PAR | 发行时所得税税率类型 | 数值类型 |


