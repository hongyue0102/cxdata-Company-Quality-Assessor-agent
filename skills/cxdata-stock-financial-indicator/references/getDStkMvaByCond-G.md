# 企业价值表-通用 (getDStkMvaByCond-G)

**API_ID:** getDStkMvaByCond-G

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
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| END_DATE | 截止日期 | 日期类型 |
| ENT_VAL | 企业价值(含货币资金) | 数值类型 |
| ENT_VAL2 | 企业价值(剔除货币资金) | 数值类型 |
| EV_EBITDA | 企业倍数1 | 数值类型 |
| EV_EBITDA2 | 企业倍数2 | 数值类型 |
| MVA | 市场附加价值 | 数值类型 |
| COM_DIV_RATE | 公司股息率 | 数值类型 |
| PRI_SAL_RAT | 市净率(MRQ,归母股东权益) | 数值类型 |
| PRIC_BOO_RATIO_EQU | 市净率(MRQ,净资产) | 数值类型 |
| PRI_EAR_RAT | 市盈率(FY) | 数值类型 |
| PRIC_EARN_RATIO_NET | 市盈率(FY,扣除非经常性损益) | 数值类型 |
| PRI_BOO_RAT | 市销率(FY) | 数值类型 |
| PRIC_CASH_RATIO | 市现率(FY,经营性净现金流) | 数值类型 |
| PRIC_CASH_RATIO_ACC | 市现率(FY,现金及现金等价物净增加额) | 数值类型 |


