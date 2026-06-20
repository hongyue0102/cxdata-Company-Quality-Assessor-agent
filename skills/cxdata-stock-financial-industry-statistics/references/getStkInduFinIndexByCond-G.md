# 行业财务分析指标-通用 (getStkInduFinIndexByCond-G)

**API_ID:** getStkInduFinIndexByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| endDate | 截止日期 | 日期类型 | 否 |  |
| induSysPar | 行业分类体系 | 数值类型 | 否 |  |
| induClassName | 行业名称 | 字符类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| END_DATE | 截止日期 | 日期类型 |
| INDU_SYS_PAR | 行业分类体系 | 数值类型 |
| INDU_CLASS_CODE | 行业代码 | 字符类型 |
| INDU_CLASS_NAME | 行业名称 | 字符类型 |
| LIQU_ASE | 行业流动资产 | 数值类型 |
| TOT_ASE | 行业总资产 | 数值类型 |
| AVG_ASE | 行业平均总资产 | 数值类型 |
| NET_ASE | 行业净资产 | 数值类型 |
| LIQU_LIAB | 行业流动负债 | 数值类型 |
| TOT_LIAB | 行业负债总额 | 数值类型 |
| OPER_INC | 行业营业收入 | 数值类型 |
| OPER_COST | 行业营业成本 | 数值类型 |
| OPER_PROF | 行业营业利润 | 数值类型 |
| NET_PROF | 行业净利润 | 数值类型 |
| INDU_EBIT | 行业息税前利润（EBIT） | 数值类型 |
| OPER_NET_CASH | 行业经营活动产生的现金净流量净额 | 数值类型 |
| LIQU_RATIO | 行业流动比率 | 数值类型 |
| NTPRO_INC_RATIO | 行业销售净利率 | 数值类型 |
| GPRO_INC_RATIO | 行业销售毛利率 | 数值类型 |
| OPER_PROF_RATIO | 行业营业利润率 | 数值类型 |
| RETU_ON_ASE | 行业资产净利率 | 数值类型 |
| INDU_ROE | 行业净资产收益率 | 数值类型 |
| ASE_LIAB_RATIO | 行业资产负债率 | 数值类型 |
| OPER_INC_GROW | 行业营业收入增长率 | 数值类型 |
| OPER_PROF_GROW | 行业营业利润增长率 | 数值类型 |
| NET_PROF_GROW | 行业净利润增长率 | 数值类型 |
| TOT_ASE_GROW | 行业总资产增长率 | 数值类型 |
| NET_ASE_GROW | 行业净资产增长率 | 数值类型 |


