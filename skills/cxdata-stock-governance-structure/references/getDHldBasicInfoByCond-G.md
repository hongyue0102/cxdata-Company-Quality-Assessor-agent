# 股东基础数据表-通用 (getDHldBasicInfoByCond-G)

**API_ID:** getDHldBasicInfoByCond-G

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
| OWN_CONCE10 | 股权集中度-前十大股东持股比例 | 数值类型 |
| OWN_CONCE1 | 股权集中度-第一大股东持股比例 | 数值类型 |
| HOLD_RESTC_VOL10 | 前十大股东有限售股数量 | 数值类型 |
| HOLD_VOL10 | 前十大股东无限售股数量 | 数值类型 |
| FRZ_SHARE | 冻结总股数 | 数值类型 |
| ADDI_SHARE | 股东增持股数 | 数值类型 |
| REDU_SHARE | 股东减持股数 | 数值类型 |
| ACTU_PLACE_VOL | 配股实际获配数量 | 数值类型 |
| VETO_DIRE_NUM | 股东大会否决董监高人次 | 数值类型 |


