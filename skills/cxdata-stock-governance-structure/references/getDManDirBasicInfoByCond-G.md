# 董事会基础数据-通用 (getDManDirBasicInfoByCond-G)

**API_ID:** getDManDirBasicInfoByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| endDate | 截止日期 | 日期类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 |  |
| STK_SHORT_NAME | 股票简称 |  |
| END_DATE | 截止日期 |  |
| DIR_IN_SEN_MAN_RATIO | 董事在高管中任职比例 |  |
| IS_CHAI_GEN_MAN | 董事长是否兼任总经理 |  |
| WHET_DIR_IS_ABNO | 董事离职交接是否异常 |  |
| IS_THE_CHAI_ABS | 董事长是否缺失 |  |
| LEN_OF_ABS_CHAI | 董事长缺失时长 |  |
| IS_MORE_THAN_ONE_CHAI | 是否存在多名董事长 |  |
| BOA_SIZE | 董事会规模 |  |
| SCA_OF_INDE_DIR | 其中：独立董事规模 |  |
| INDE_DIR_RATIO | 独立董事占董事比例 |  |
| TOT_SHAR_HOLD | 董事持股总数 |  |
| AMOU_OF_DIR_REMU | 董事薪酬总额 |  |
| AMOU_OF_INDE_DIR | 其中：独立董事薪酬总额 |  |
| INCOME_INDE_DIR_RATIO | 独立董事薪酬占公司收入比例 |  |
| DIR_TURN_RATIO | 董事会离职率 |  |


