# 公司股改股东大会出席情况-通用 (getDComDiviMeetAtteByCond-G)

**API_ID:** getDComDiviMeetAtteByCond-G

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
| MEET_DECL_DATE | 股东大会公告日期 | 日期类型 |
| MEET_REG_DATE | 股东大会登记日 | 日期类型 |
| MEET_DATE | 股东大会召开日 | 日期类型 |
| ATTE_TYPE_PAR | 股东出席类别 | 数值类型 |
| NETW_VOTE_CODE | 网络投票代码 | 字符类型 |
| VOTE_SHORT_NAME | 投票简称 | 字符类型 |
| HLD_REPR_NUM | 出席股东及代表人数 | 数值类型 |
| REPR_SHARE | 代表股份 | 数值类型 |
| ACF_TOT_SHARE | 占总股份比例 | 数值类型 |
| NON_HLD_SUM | 非流通股东人数 | 数值类型 |
| NON_HLD_SUM_OUT | 外资非流通股东人数 | 数值类型 |
| NON_HLD_SHARE | 非流通股东代表股份 | 数值类型 |
| NON_HLD_SHARE_OUT | 外资非流通股东代表股份 | 数值类型 |
| FLOAT_HLD_SUM | 流通股东人数 | 数值类型 |
| FLOAT_A_HLD_SUM | 流通A股股东人数 | 数值类型 |
| FLOAT_HLD_SHARE | 流通股东代表股份 | 数值类型 |
| FLOAT_A_HLD_SHARE | 流通A股股东代表股份 | 数值类型 |
| MEET_COMPE | 大会主持人 | 字符类型 |
| LAW_OFFI | 见证律师事务所 | 字符类型 |
| MEET_LAWY | 经办律师 | 字符类型 |


