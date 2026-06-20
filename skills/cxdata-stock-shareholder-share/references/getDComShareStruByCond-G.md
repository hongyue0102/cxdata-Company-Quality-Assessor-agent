# 公司股本结构变动-通用 (getDComShareStruByCond-G)

**API_ID:** getDComShareStruByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| endDate | 截止日期 | 日期类型 | 否 |  |
| declDate | 公告日期 | 日期类型 | 否 |  |
| chanType | 股本变动原因类别 | 数值类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| END_DATE | 截止日期 | 日期类型 |
| DECL_DATE | 公告日期 | 日期类型 |
| DISC_FORM_PAR | 股本披露格式 | 数值类型 |
| TOT_SHARE | 总股本 | 数值类型 |
| A_SHARE | A股 | 数值类型 |
| B_SHARE | B股 | 数值类型 |
| H_SHARE | H股 | 数值类型 |
| S_SHARE | S股 | 数值类型 |
| N_SHARE | N股 | 数值类型 |
| OTHER_SHARE | 其他股本 | 数值类型 |
| FLOAT_SHARE | 无限售流通股份合计 | 数值类型 |
| FLOAT_A_SHARE | 1.流通A股 | 数值类型 |
| FLOAT_B_SHARE | 2.流通B股 | 数值类型 |
| RESTC_SHARE_HOLD | 有限售条件股份合计 | 数值类型 |
| RESTC_A_SHARE | 1.有限售A股 | 数值类型 |
| RESTC_B_SHARE | 2.有限售B股 | 数值类型 |
| STATE_HOLD | A.国家持股_有限售 | 数值类型 |
| STATE_LEG_PER_HOLD | B.国有法人持股_有限售 | 数值类型 |
| OTHER_DOME_CAP_HOLD | C.其他内资持股_有限售 | 数值类型 |
| DOME_LEG_PER_HOLD | a.境内法人持股_有限售 | 数值类型 |
| DOME_NATR_PER_HOLD | b.境内自然人持股_有限售 | 数值类型 |
| FORE_CAP_HOLD | D.外资持股_有限售 | 数值类型 |
| FORE_LEG_PER_HOLD | a.境外法人持股_有限售 | 数值类型 |
| FORE_NATR_PER_HOLD | b.境外自然人持股_有限售 | 数值类型 |
| MAN_HOLD | E.高管持股_有限售 | 数值类型 |
| OTHER_RESTC_HOLD | F.其他有限售_有限售 | 数值类型 |
| DIR_MAN_HOLD | G.董事、监事、高管_有限售 | 数值类型 |
| CON_ACT_HOLD | H.控股股东、实际控制人_有限售 | 数值类型 |
| NON_FLOAT_SHARE | 未上市流通股份合计 | 数值类型 |
| NON_FLOAT_A | 未流通A股 | 数值类型 |
| NON_FLOAT_B | 未流通B股 | 数值类型 |
| SPON_SHARE | 1.发起人股份_未流通 | 数值类型 |
| STATE_SHARE | (1)国家股_未流通 | 数值类型 |
| STATE_LEG_PER_SHARE | (2)国有法人股_未流通 | 数值类型 |
| DOME_LEG_PER_SHARE | (3)境内法人股_未流通 | 数值类型 |
| FORE_LEG_PER_SHARE | (4)外资法人股_未流通 | 数值类型 |
| OTHER_SPO_SHARE | (5)其他发起人股_未流通 | 数值类型 |
| COLL_LEG_PER_SHARE | 2.募集/定向法人股份_未流通 | 数值类型 |
| STAFF_SHARE | 3.内部职工股_未流通 | 数值类型 |
| TRAN_PLACE_SHARE | 4.转配股_未流通 | 数值类型 |
| PRE_OTHER_SHARE | 5.优先股或其他_未流通 | 数值类型 |
| CHAN_TYPE | 股本变动原因类别 | 数值类型 |
| CHAN_REAS | 股本变动原因说明 | 字符类型 |


