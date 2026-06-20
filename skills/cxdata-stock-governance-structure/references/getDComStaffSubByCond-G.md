# 公司职工构成明细-通用 (getDComStaffSubByCond-G)

**API_ID:** getDComStaffSubByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| endDate | 截止日期 | 日期类型 | 否 |  |
| mergeMarkPar | 合并标志 | 数值类型 | 否 |  |
| classMethPar | 分类方式 | 数值类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| END_DATE | 截止日期 | 日期类型 |
| MERGE_MARK_PAR | 合并标志 | 数值类型 |
| CLASS_METH_PAR | 分类方式 | 数值类型 |
| PROJ_NAME | 项目名称 | 字符类型 |
| STAFF_VOL | 员工数量 | 数值类型 |
| STAFF_SUM | 员工总数 | 数值类型 |
| ACF_SUM_PCT | 占员工总数比例 | 数值类型 |


