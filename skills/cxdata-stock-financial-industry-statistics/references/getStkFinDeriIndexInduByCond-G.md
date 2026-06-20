# 财务衍生指标行业统计-通用 (getStkFinDeriIndexInduByCond-G)

**API_ID:** getStkFinDeriIndexInduByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| induClassName | 行业名称 | 字符类型 | 否 |  |
| endDate | 截止日期 | 日期类型 | 否 |  |
| induSysPar | 行业分类体系参数 | 数值类型 | 否 |  |
| induLevel | 行业级别 | 字符类型 | 否 |  |
| indexStatTypePar | 指标统计类型参数 | 数值类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| INDU_CLASS_NAME | 行业名称 | 字符类型 |
| END_DATE | 截止日期 | 日期类型 |
| INDU_SYS_PAR | 行业分类体系参数 | 数值类型 |
| INDU_LEVEL | 行业级别 | 字符类型 |
| INDEX_STAT_TYPE_PAR | 指标统计类型参数 | 数值类型 |
| NTPRO_CUT | 扣非归母净利润 | 数值类型 |
| NTPRO_CUT_GRO | 扣非归母净利润同比增长率 | 数值类型 |
| NET_PRO_GRO | 净利润同比增长率 | 数值类型 |
| OPER_INC | 营业总收入同比增长率 | 数值类型 |
| BAS_EPS | 基本每股收益 | 数值类型 |
| BAS_EPS_CUT | 扣非每股收益 | 数值类型 |
| DIL_EPS | 稀释每股收益 | 数值类型 |
| NET_ASS_VAL | 每股净资产 | 数值类型 |
| PER_SHA_CAP | 每股资本公积金 | 数值类型 |
| UND_PRO_PER | 每股未分配利润 | 数值类型 |
| OPE_CAS_FLO | 每股经营现金流 | 数值类型 |
| PRI_EAR_RAT | 市盈率(FY) | 数值类型 |
| PRIC_EARN_RATIO_NET | 市盈率(FY,扣除非经常性损益) | 数值类型 |
| PRI_SAL_RAT | 市净率(MRQ,归母股东权益) | 数值类型 |
| PRIC_BOO_RATIO_EQU | 市净率(MRQ,净资产) | 数值类型 |
| PRI_BOO_RAT | 市销率(FY) | 数值类型 |
| PRIC_CASH_RATIO | 市现率(FY,经营性净现金流) | 数值类型 |
| PRIC_CASH_RATIO_ACC | 市现率(FY,现金及现金等价物净增加额) | 数值类型 |
| NET_PRO | 销售净利率 | 数值类型 |
| GRO_PRO | 营业毛利率 | 数值类型 |
| ROE_END | 净资产收益率(摊薄) | 数值类型 |
| ROE_WEI | 净资产收益率(加权) | 数值类型 |
| ROE_CUT_WEI | 净资产收益率(扣非/加权) | 数值类型 |
| RET_ON_ASS | 总资产收益率(ROA) | 数值类型 |
| RET_ON_INV_CAP | 投资资本回报率 | 数值类型 |
| OPER_CYC | 营业周期 | 数值类型 |
| INV_TUR | 存货周转率 | 数值类型 |
| INV_TUR_DAYS | 存货周转天数 | 数值类型 |
| ACC_REC_TUR | 应收账款周转率 | 数值类型 |
| ACC_REC_DAYS | 应收账款周转天数 | 数值类型 |
| CUR_ASS_TUR | 流动资产周转率 | 数值类型 |
| TOT_ASS_TUR | 总资产周转率 | 数值类型 |
| ACC_PAY_TUR | 应付账款周转率 | 数值类型 |
| EQU_TURN | 股东权益周转率 | 数值类型 |
| FIX_ASS_TURN | 固定资产周转率 | 数值类型 |
| PRO_OF_FIX_ASS | 固定资产与收入比 | 数值类型 |
| CUR_RAT | 流动比率 | 数值类型 |
| QUI_RAT | 速动比率 | 数值类型 |
| SUP_QUI_RAT | 保守速动比率 | 数值类型 |
| EQU_RAT | 产权比率 | 数值类型 |
| EQU_MUL | 权益乘数 | 数值类型 |
| DEB_ASS_RAT | 资产负债率 | 数值类型 |
| CASH_FLO_RAT | 现金流量比率 | 数值类型 |
| CASH_RAT | 现金比率 | 数值类型 |
| SAL_REC_CASH | 销售收到现金比率  | 数值类型 |
| CASH_FLO_TO_INC | 盈余现金保障倍数 | 数值类型 |
| CASH_TO_PRO | 现金与利润总额比 | 数值类型 |
| OPER_CAS_RAT | 营业收现比 | 数值类型 |


