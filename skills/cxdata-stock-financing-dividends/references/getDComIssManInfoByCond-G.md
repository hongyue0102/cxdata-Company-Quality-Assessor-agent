# 公司发行前高管信息表-通用 (getDComIssManInfoByCond-G)

**API_ID:** getDComIssManInfoByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| orgChiName | 公司名称 | 字符类型 | 否 |  |
| indivName | 人物姓名 | 字符类型 | 否 |  |
| declDate | 公告日期 | 日期类型 | 否 |  |
| posiPar | 职位参数 | 数值类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| ORG_CHI_NAME | 公司名称 | 字符类型 |
| INDIV_NAME | 人物姓名 | 字符类型 |
| DECL_DATE | 公告日期 | 日期类型 |
| POSI_PAR | 职位参数 | 数值类型 |
| POSI_NAME | 职位名称 | 字符类型 |
| POSI_START_DATE | 任职起始日 | 日期类型 |
| POSI_END_DATE | 任职截止日 | 日期类型 |
| POSI_TYPE_PAR | 职位类别参数 | 数值类型 |
| IS_REPR_POSI_PAR | 是否代理职位参数 | 数值类型 |


