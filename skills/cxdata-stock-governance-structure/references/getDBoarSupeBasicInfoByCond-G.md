# 监事会基础数据-通用 (getDBoarSupeBasicInfoByCond-G)

**API_ID:** getDBoarSupeBasicInfoByCond-G

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
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| END_DATE | 截止日期 | 日期类型 |
| IS_THE_CHAI_ABS | 监事会主席是否缺失 | 数值类型 |
| LEN_OF_ABS_CHAI | 监事会主席缺失时长 | 数值类型 |
| IS_MORE_THAN_ONE_CHAI | 是否存在多名监事会主席 | 数值类型 |
| IS_THE_STAF_SUPE | 是否有职工监事 | 数值类型 |
| IS_STAF_SUPE_CHAI | 职工监事是否为监事会主席 | 数值类型 |
| SUPE_SIZE | 监事会规模 | 数值类型 |
| STAF_SUPE_RATIO | 其中：职工监事占比 | 数值类型 |
| AMOU_OF_SUPE_REMU | 监事薪酬金额 | 数值类型 |
| TOT_SHAR_HOLD | 监事持股 | 数值类型 |
| SUPE_TURN_RATIO | 监事会离职率 | 数值类型 |


