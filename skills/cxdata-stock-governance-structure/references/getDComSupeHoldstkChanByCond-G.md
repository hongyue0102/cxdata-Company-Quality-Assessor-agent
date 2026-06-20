# 监事层及关联人持股变动-通用 (getDComSupeHoldstkChanByCond-G)

**API_ID:** getDComSupeHoldstkChanByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| chanDate | 变动日期 | 日期类型 | 否 |  |
| leadName | 监事姓名 | 字符类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| CHAN_DATE | 变动日期 | 日期类型 |
| REP_DATE | 填报日期 | 日期类型 |
| LEAD_NAME | 监事姓名 | 字符类型 |
| POSI_NAME | 职务 | 字符类型 |
| STK_CHAN_NAME | 股份变动人名称 | 字符类型 |
| LEAD_RELA | 股份变动人与监事关系 | 字符类型 |
| STK_TYPE_PAR | 变动股份类型 | 数值类型 |
| CHAN_BEF_HOLD_VOL | 变动前持股数 | 数值类型 |
| CHAN_HOLD_VOL | 变动股数 | 数值类型 |
| CHAN_MEAN | 变动均价 | 数值类型 |
| CURY_TYPE_PAR | 货币类型 | 数值类型 |
| CHAN_PCT | 变动比例 | 数值类型 |
| CHAN_AFTER_HOLD | 变动后持股数 | 数值类型 |
| CHAN_REAS_DES | 持股变动原因 | 字符类型 |


