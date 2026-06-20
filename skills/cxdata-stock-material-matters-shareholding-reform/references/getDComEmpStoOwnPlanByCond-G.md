# 公司员工持股计划-通用 (getDComEmpStoOwnPlanByCond-G)

**API_ID:** getDComEmpStoOwnPlanByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| progName | 计划名称 | 字符类型 | 否 |  |
| planPublDate | 预案公告日 | 日期类型 | 否 |  |
| eventProcPar | 事件进程参数 | 数值类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| PROG_NAME | 计划名称 | 字符类型 |
| PLAN_PUBL_DATE | 预案公告日 | 日期类型 |
| MEET_DECL_DATE | 股东大会公告日 | 日期类型 |
| SHARE_ORI | 股份来源 | 数值类型 |
| EVENT_PROC_PAR | 事件进程参数 | 数值类型 |
| EVENT_DES | 事件概述 | 字符类型 |
| STAFF_CONTRI_LIMIT | 其中：员工自筹资金上限 | 数值类型 |
| RAISE_SHARE_LIMIT | 拟募集股票规模上限 | 数值类型 |
| PARTIC_DES | 参与对象 | 字符类型 |
| PARTIC_NUM_MAX | 参与人数上限 | 数值类型 |
| MATU_PERIOD | 存续期 | 数值类型 |
| MATU_PERIOD_DES | 存续期说明 | 字符类型 |
| LOCK_UP_PERIOD_DES | 锁定期说明 | 字符类型 |
| ASSET_MANAG_ORG | 资产管理机构 | 字符类型 |
| COMMEN_IMPLE_DATE | 开始实施公告日 | 日期类型 |
| COMPLE_IMPLE_DATE | 完成实施公告日 | 日期类型 |
| SHARE_PURCH_COMPLE_DATE | 股份购买完成日 | 日期类型 |
| PURCH_COST | 购买成本 | 数值类型 |
| TOT_SUB_FUNDS | 实际认购资金总额 | 数值类型 |
| ACTU_HOLD_VOL | 实际持股数量 | 数值类型 |
| ACTU_HOLD_RATIO | 实际持股比例 | 数值类型 |
| SALE_DECL_DATE | 股份出售完毕公告日 | 日期类型 |
| DURA_START_DATE | 存续期起始日 | 日期类型 |
| DURA_END_DATE | 存续期截止日 | 日期类型 |
| LOCKUP_PERI_START_DATE | 锁定期起始日 | 日期类型 |
| LOCKUP_PERI_END_DATE | 锁定期截止日 | 日期类型 |


