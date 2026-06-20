# 监事层持股薪酬情况-通用 (getDComManHold2ByCond-G)

**API_ID:** getDComManHold2ByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| endDate | 截止日期 | 日期类型 | 否 |  |
| manName | 姓名 | 字符类型 | 否 |  |
| posiName | 职位 | 字符类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| END_DATE | 截止日期 | 日期类型 |
| MAN_NAME | 姓名 | 字符类型 |
| POSI_NAME | 职位 | 字符类型 |
| EAR_HOLD_VOL | 期初持股数 | 数值类型 |
| END_HOLD_VOL | 期末直接持股数 | 数值类型 |
| END_HOLD_RATIO | 期末直接持股比例 | 数值类型 |
| INDIR_HOLD_VOL | 期末间接持股数 | 数值类型 |
| INDIR_HOLD_RATIO | 期末间接持股比例 | 数值类型 |
| IS_PAY_PAR | 是否在股东方或关联方领取报酬 | 数值类型 |
| YEAR_PAY | 年度报酬 | 数值类型 |
| PAY_ALLO | 其中:补贴津贴 | 数值类型 |
| IS_TAX_PAR | 是否为税前报酬 | 数值类型 |
| EXER_STK_SUM | 可行权股数 | 数值类型 |
| EXERED_SUM | 已行权数量 | 数值类型 |
| EXER_PRI | 行权价 | 数值类型 |
| REST_HOLD | 授予的限制性股票数量 | 数值类型 |
| REST_HOLD_NEW | 报告期新授予限制性股票数量 | 数值类型 |
| REST_HOLD_PRI | 限制性股票的授予价格（除权前） | 数值类型 |
| END_REST_HOLD | 期末持有限制性股票数量 | 数值类型 |
| CHAN_REAS_DES | 持股变动原因说明 | 字符类型 |


