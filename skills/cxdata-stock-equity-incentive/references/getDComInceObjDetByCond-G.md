# 公司股权激励对象明细-通用 (getDComInceObjDetByCond-G)

**API_ID:** getDComInceObjDetByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| declDate | 公告日期 | 日期类型 | 否 |  |
| indivName | 姓名 | 字符类型 | 否 |  |
| subId | 子表关联标识 | 数值类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| DECL_DATE | 公告日期 | 日期类型 |
| INCE_STAT_PAR | 激励状态参数 | 数值类型 |
| CONF_NUM | 权益期次 | 字符类型 |
| INDIV_NAME | 姓名 | 字符类型 |
| POSI_NAME | 职位名称 | 字符类型 |
| CONF_RIGHT_NUM | 获授限制性股票/期权数量 | 数值类型 |
| CONF_RATIO | 占本期授予数量比例 | 数值类型 |
| SHARE_RATIO | 占公司总股本比例 | 数值类型 |
| AUTHO_RIGTH_NUM | 本次可行权期权数量 | 数值类型 |
| START_DATE | 本次可行权起始日 | 日期类型 |
| END_DATE | 本次可行权截止日 | 日期类型 |
| SUB_ID | 子表关联标识 | 数值类型 |

#### 直接前置依赖
以下参数存在可参考的直接前置接口。是否调用前置接口，取决于当前查询目标、已知条件以及当前接口入参是否已满足。
- 参数 `subId`：可通过调用 **公司股权激励-通用（API_ID:getDComInceMainByCond-G）** 获取

#### 多流程依赖说明
当当前接口的关键入参存在多种补齐方式时，可按以下流程逐级调用，不要预先串行调用所有上游接口。
##### 流程1（补齐参数 `subId`）
1. 调用 **公司股权激励-通用（API_ID:getDComInceMainByCond-G）**，补齐后续所需参数 `subId`
2. 调用 **公司股权激励对象明细-通用（API_ID:getDComInceObjDetByCond-G）**，完成当前查询

