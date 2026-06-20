# 公司关联关系信息-通用 (getDComRelaInfoByCond-G)

**API_ID:** getDComRelaInfoByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| endDate | 截止日期 | 日期类型 | 否 |  |
| relaObjName | 关联方名称 | 字符类型 | 否 |  |
| relaPar | 关联关系 | 数值类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| REP_TYPE_PAR | 公告类型 | 数值类型 |
| DECL_DATE | 公告日期 | 日期类型 |
| END_DATE | 截止日期 | 日期类型 |
| RELA_OBJ_NAME | 关联方名称 | 字符类型 |
| RELA_PAR | 关联关系 | 数值类型 |
| RELA_COM_CTR_RIGHT | 关联公司控制权益比例 | 数值类型 |
| LIST_COM_CTR_RIGHT | 上市公司直接持股比例 | 数值类型 |
| RELA_COM_REG_CAP | 关联公司注册资本 | 数值类型 |
| CURY_TYPE_PAR | 货币类型 | 数值类型 |
| MAIN_BUS | 关联公司主营业务 | 字符类型 |
| RELA_COM_ADDR | 关联方所在地 | 字符类型 |
| LIST_COM_IND_RIGHT | 上市公司间接持股比例 | 数值类型 |
| ASSO_DESC | 关联关系说明 | 字符类型 |


