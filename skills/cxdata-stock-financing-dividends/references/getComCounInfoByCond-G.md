# 公司辅导备案及境外上市信息-通用 (getComCounInfoByCond-G)

**API_ID:** getComCounInfoByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| orgName | 公司名称 | 字符类型 | 否 |  |
| acceDate | 受理日期 | 日期类型 | 否 |  |
| oriName | 业务类型 | 数值类型 | 否 |  |
| declDate | 公告日期 | 日期类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| ORG_NAME | 公司名称 | 字符类型 |
| ACCE_DATE | 受理日期 | 日期类型 |
| AREA_INFO | 所属地区 | 字符类型 |
| INDU_CLASS_NAME | 所属行业 | 字符类型 |
| STK_CODE | 证券代码 | 字符类型 |
| PRO_TYPE | 备案审核类型 | 数值类型 |
| COUN_ORG | 辅导机构 | 字符类型 |
| COUN_DISP_ORG | 辅导派出机构 | 字符类型 |
| PRO_LIST_EXCH | 拟上市证券交易所 | 字符类型 |
| IF_SIM_ISSU | 是否挂牌同时发行 | 数值类型 |
| SPON_NAME | 主办券商 | 字符类型 |
| ACC_OFFI | 律师事务所 | 字符类型 |
| LAW_OFFI | 会计师事务所 | 字符类型 |
| ASE_EVAL_INS | 资产评估机构 | 字符类型 |
| CRE_RATE_INS | 资信评级机构 | 字符类型 |
| ORI_NAME | 业务类型 | 数值类型 |
| DECL_DATE | 公告日期 | 日期类型 |
| AUD_STAT | 备案审核状态 | 字符类型 |
| AUD_STAT_PAR | 备案审核状态参数 | 数值类型 |
| REG_STAT | 注册状态 | 字符类型 |
| APPR_DATE | 审核通过日 | 日期类型 |
| DISC_DATE | 方案披露日 | 日期类型 |
| NEW_REGS_DATE | 新增股份登记日 | 日期类型 |
| LAT_INQU_DATE | 最新问询日 | 日期类型 |
| LAT_REPL_DATE | 最新回复日 | 日期类型 |


