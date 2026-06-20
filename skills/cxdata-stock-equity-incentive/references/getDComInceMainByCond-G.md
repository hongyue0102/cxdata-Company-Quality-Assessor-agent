# 公司股权激励-通用 (getDComInceMainByCond-G)

**API_ID:** getDComInceMainByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| firDeclDate | 首次公告日期 | 日期类型 | 否 |  |
| inceModePar | 激励模式 | 数值类型 | 否 |  |
| eventProcPar | 事件进程 | 数值类型 | 否 |  |
| mainId | 主表关联标识 | 数值类型 | 否 |  |
| incePlanName | 激励计划名称 | 字符类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| FIR_DECL_DATE | 首次公告日期 | 日期类型 |
| INCE_MODE_PAR | 激励模式 | 数值类型 |
| DIRE_DECL_DATE | 董事会公告日期 | 日期类型 |
| STM_DECL_DATE | 股东大会公告日期 | 日期类型 |
| STK_ORI_PAR | 股票来源 | 数值类型 |
| STK_TYPE_PAR | 标的股票类型 | 数值类型 |
| PRI_DES | 价格确定说明 | 字符类型 |
| VALID_MATU | 有效期 | 数值类型 |
| AUTHO_NUM | 行权/授予次数 | 数值类型 |
| EXER_COND | 行权/授予条件 | 字符类型 |
| EVENT_PROC_PAR | 事件进程 | 数值类型 |
| EVENT_DES | 事件概述 | 字符类型 |
| INCE_TOT_VOL | 激励股票总量 | 数值类型 |
| INCE_PLAN_NAME | 激励计划名称 | 字符类型 |


