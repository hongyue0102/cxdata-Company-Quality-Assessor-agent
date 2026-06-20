# 公司十大股东-通用 (getDComTenHldByCond-G)

**API_ID:** getDComTenHldByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| declDate | 公告日期 | 日期类型 | 否 |  |
| endDate | 截止日期 | 日期类型 | 否 |  |
| hldName | 股东名称 | 字符类型 | 否 |  |
| holdRatio | 持股比例 | 数值类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| DECL_DATE | 公告日期 | 日期类型 |
| END_DATE | 截止日期 | 日期类型 |
| HLD_NAME | 股东名称 | 字符类型 |
| HLD_TYPE_PAR | 股东性质 | 数值类型 |
| HOLD_RANK | 持股排名 | 数值类型 |
| HOLD_VOL | 持股数 | 数值类型 |
| HOLD_RATIO | 持股比例 | 数值类型 |
| STK_ATTR_PAR | 股份性质 | 数值类型 |
| HOLD_RESTC_VOL | 其中：有限售股数 | 数值类型 |
| PLE_FRZ_VOL | 质押、冻结或托管总股数 | 数值类型 |
| PLE_VOL | 其中：质押数量 | 数值类型 |
| FRZ_VOL | 其中：冻结数量 | 数值类型 |
| TRUSTEE_VOL | 其中：托管股份 | 数值类型 |
| PLE_FRZ_DES | 质押、冻结或托管情况说明 | 字符类型 |


