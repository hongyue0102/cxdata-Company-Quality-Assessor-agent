# 上市公司财务指标行业排名-通用 (getStkFinIndexInduRankByCond-G)

**API_ID:** getStkFinIndexInduRankByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| endDate | 截止日期 | 日期类型 | 否 |  |
| sheetMarkPar | 报表合并标志 | 数值类型 | 否 |  |
| busiTypePar | 企业类型 | 数值类型 | 否 |  |
| induSysPar | 行业分类体系参数 | 数值类型 | 否 |  |
| induLevel | 行业级别 | 字符类型 | 否 |  |
| induName | 行业名称 | 字符类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| END_DATE | 截止日期 | 日期类型 |
| SHEET_MARK_PAR | 报表合并标志 | 数值类型 |
| BUSI_TYPE_PAR | 企业类型 | 数值类型 |
| INDU_SYS_PAR | 行业分类体系参数 | 数值类型 |
| INDU_LEVEL | 行业级别 | 字符类型 |
| INDU_NAME | 行业名称 | 字符类型 |
| COM_NUM | 行业上市公司数量 | 数值类型 |
| L01_PRI_EAR_RAT_RANK | 市盈率(FY)排名 | 数值类型 |
| L01_PRIC_EARN_RATIO_NET | 市盈率(FY,扣除非经常性损益)排名 | 数值类型 |
| L01_PRI_SAL_RAT_RANK | 市销率(FY)排名 | 数值类型 |
| L01_PRI_BOO_RAT_RANK | 市净率(MRQ,归母股东权益)排名 | 数值类型 |
| L01_PRIC_BOO_RATIO_EQU | 市净率(MRQ,净资产)排名 | 数值类型 |
| L01_PRIC_CASH_RATIO | 市现率(FY,经营性净现金流)排名 | 数值类型 |
| L01_PRIC_CASH_RATIO_ACC | 市现率(FY,现金及现金等价物净增加额)排名 | 数值类型 |
| L01_NET_PRO_RANK | 销售净利率排名 | 数值类型 |
| L01_GRO_PRO_RANK | 销售毛利率排名 | 数值类型 |
| L01_RET_ON_ASS_RANK | 资产净利率排名 | 数值类型 |
| L01_RET_ON_EQU_RANK | 净资产收益率排名 | 数值类型 |
| L01_RET_TOT_ASS_RANK | 总资产报酬率排名 | 数值类型 |
| L01_OPE_PRO_RANK | 营业利润率排名 | 数值类型 |
| L01_COS_INC_RAT_RANK | 成本费用利润率排名 | 数值类型 |
| L02_SHA_EQU_RAT_RANK | 股东权益比率排名 | 数值类型 |
| L02_EQU_RAT_RANK | 产权比率排名 | 数值类型 |
| L02_TAN_NET_RANK | 有形净值债务率排名 | 数值类型 |
| L02_CUR_RAT_RANK | 流动比率排名 | 数值类型 |
| L02_QUI_RAT_RANK | 速动比率排名 | 数值类型 |
| L02_DEB_ASS_RAT_RANK | 资产负债率排名 | 数值类型 |
| L02_INT_COV_RAT_RANK | 已获利息倍数排名 | 数值类型 |
| L02_CAS_MAT_DEB_RANK | 现金到期债务比排名 | 数值类型 |
| L02_CAS_TOT_DEB_RANK | 现金债务总额比排名 | 数值类型 |
| L02_CAS_CUR_LIA_RANK | 现金流动负债比排名 | 数值类型 |
| L03_NET_PROF_RANK | 净利润排名 | 数值类型 |
| L03_OPER_INC_RANK | 营业收入排名 | 数值类型 |
| L03_TOT_ASE_RANK | 总资产排名 | 数值类型 |
| L03_OPE_REV_GRO_RANK | 营业收入增长率排名 | 数值类型 |
| L03_OPE_PRO_GRO_RANK | 营业利润增长率排名 | 数值类型 |
| L03_NET_PRO_GRO_RANK | 净利润增长率排名 | 数值类型 |
| L03_TOT_ASS_GRO_RANK | 总资产增长率排名 | 数值类型 |
| L03_OPE_CAS_GRO_RANK | 经营现金流量净额增长率排名 | 数值类型 |
| L03_BAS_EAR_PER_RANK | 基本每股收益增长率排名 | 数值类型 |
| L04_EAR_PER_SHAR_RANK | 每股收益排名 | 数值类型 |
| L04_NET_ASS_VAL_RANK | 每股净资产排名 | 数值类型 |
| L04_OPE_CAS_FLO_RANK | 每股经营现金流量排名 | 数值类型 |
| L04_CAS_RET_ON_RANK | 全部资产现金回收率排名 | 数值类型 |
| L04_CAS_FLO_SAL_RANK | 销售现金比率排名 | 数值类型 |
| L04_CAS_FLO_ADE_RANK | 现金满足投资比率排名 | 数值类型 |
| L04_CAS_DIV_COV_RANK | 现金股利保障倍数排名 | 数值类型 |
| L04_OPE_IND_RANK | 营运指数排名 | 数值类型 |
| L04_CAS_EAR_COV_RANK | 盈余现金保障倍数排名 | 数值类型 |
| L04_OPE_CAS_RAT_RANK | 营业收现比排名 | 数值类型 |
| L05_INV_TUR_RANK | 存货周转率排名 | 数值类型 |
| L05_ACC_REC_TUR_RANK | 应收账款周转率排名 | 数值类型 |
| L05_ACC_PAY_TUR_RANK | 应付账款周转率排名 | 数值类型 |
| L05_TOT_ASS_TUR_RANK | 总资产周转率排名 | 数值类型 |
| L05_OPE_CYC_RANK | 营业周期排名 | 数值类型 |
| L05_CUR_ASS_TUR_RANK | 流动资产周转率排名 | 数值类型 |
| L05_LON_DEB_EQU_RANK | 长期负债权益比率排名 | 数值类型 |
| L06_ACC_REC_RAT_RANK | 应收账款比例排名 | 数值类型 |
| L06_INV_RAT_RANK | 存货比例排名 | 数值类型 |
| L06_GOO_RAT_RANK | 商誉比例排名 | 数值类型 |
| L07_TOT_VALUE_RATE_RANK | 总市值排名 | 数值类型 |
| L07_FLO_VAL_RATE_RANK | 流通市值排名 | 数值类型 |
| L07_TOT_SHARE_RANK | 总股本(股)排名 | 数值类型 |


