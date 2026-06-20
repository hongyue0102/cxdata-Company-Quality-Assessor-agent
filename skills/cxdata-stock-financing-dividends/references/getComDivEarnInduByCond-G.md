# 上市公司分红与盈利按行业统计-通用 (getComDivEarnInduByCond-G)

**API_ID:** getComDivEarnInduByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| endDate | 截止日期 | 日期类型 | 否 |  |
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
| COM_NUM | 行业内公司家数 | 数值类型 |
| EARN_NUM | 盈利家数 | 数值类型 |
| LOSS_NUM | 亏损家数 | 数值类型 |
| DIV_NUM | 分红家数 | 数值类型 |
| EARN_RATIO | 盈利/全部家数 | 数值类型 |
| DIV_EARN_RATIO | 分红/盈利家数 | 数值类型 |
| DIV_RATIO | 分红/全部家数 | 数值类型 |
| TOT_NET_PROF | 全行业净利润合计 | 数值类型 |
| RAEN_NET_PROF | 盈利公司净利润合计 | 数值类型 |
| TOT_PROF | 分红总额 | 数值类型 |
| RAEN_PAY_RATIO | 盈利公司股利支付率 | 数值类型 |
| TOT_PAY_RATIO | 全行业股利支付率 | 数值类型 |


