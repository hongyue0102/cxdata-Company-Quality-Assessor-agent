# 公司关联方账务往来-通用 (getDComRelaAccoByCond-G)

**API_ID:** getDComRelaAccoByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| endDate | 截止日期 | 日期类型 | 否 |  |
| relaObjName | 关联方名称 | 字符类型 | 否 |  |
| payName | 款项名称 | 字符类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| DECL_DATE | 公告日期 | 日期类型 |
| END_DATE | 截止日期 | 日期类型 |
| RELA_OBJ_NAME | 关联方名称 | 字符类型 |
| ACCO_TYPE_PAR | 账款类型 | 数值类型 |
| THIS_ACCO_AMUT | 本期期末余额 | 数值类型 |
| THIS_ACF_AMUT | 本期期末余额占该账项比例 | 数值类型 |
| PAY_NAME | 款项名称 | 字符类型 |


