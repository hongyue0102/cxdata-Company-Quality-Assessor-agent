# 公司发行前主要股东信息表-通用 (getDComIssMajHldInfoByCond-G)

**API_ID:** getDComIssMajHldInfoByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| orgChiName | 公司名称 | 字符类型 | 否 |  |
| declDate | 公告日期 | 日期类型 | 否 |  |
| hldName | 股东名称 | 字符类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| ORG_CHI_NAME | 公司名称 | 字符类型 |
| DECL_DATE | 公告日期 | 日期类型 |
| END_DATE | 截止日期 | 日期类型 |
| HOLD_RANK | 持股排名 | 数值类型 |
| HLD_NAME | 股东名称 | 字符类型 |
| HOLD_VOL | 持股数 | 数值类型 |
| HOLD_RATIO | 持股比例 | 数值类型 |


