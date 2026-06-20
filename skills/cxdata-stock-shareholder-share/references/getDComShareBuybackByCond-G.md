# 公司股份回购表-通用 (getDComShareBuybackByCond-G)

**API_ID:** getDComShareBuybackByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| iniPublDate | 首次信息发布日期 | 日期类型 | 否 |  |
| saleName | 股份被回购方名称 | 字符类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| INI_PUBL_DATE | 首次信息发布日期 | 日期类型 |
| PLAN_PUBL_DATE | 预案公布日 | 日期类型 |
| STM_RESO_PUBL_DATE | 股东大会通过日期 | 日期类型 |
| WRIT_OFF_PUBL_DATE | 回购并注销股份公告书发布日 | 日期类型 |
| BUYBACK_PURP_DES | 回购目的描述 | 字符类型 |
| CONTR_SIGN_DATE | 回购协议签署日 | 日期类型 |
| SALE_NAME | 股份被回购方名称 | 字符类型 |
| BUYBACK_METH_PAR | 回购股份方式 | 数值类型 |
| SHARE_TYPE_PAR | 股份性质 | 数值类型 |
| BUYBACK_NUM | 拟回购股数 | 数值类型 |
| ACF_TOT_RATIO | 占总股本比例 | 数值类型 |
| PRIC_METH_DES | 回购定价方式说明 | 字符类型 |
| BUYBACK_PRI | 拟回购价格 | 数值类型 |
| BUYBACK_AMUT | 拟用于回购总金额 | 数值类型 |
| CAP_ORI_DES | 拟用于回购资金来源描述 | 字符类型 |
| START_DATE | 回购期限起始日 | 日期类型 |
| END_DATE | 回购期限截至日 | 日期类型 |
| PAY_METH_PAR | 回购支付方式 | 数值类型 |
| CHAN_PUBL_DATE | 回购后股本变动公告日 | 日期类型 |
| PAY_DATE | 回购资金划出日 | 日期类型 |
| IC_REG_DATE | 工商变更登记日 | 日期类型 |
| EVENT_PROC_PAR | 事件进程 | 数值类型 |
| PROC_DESC | 进展情况描述 | 字符类型 |
| ACTU_TOT_RATIO | 实际占总股本比例 | 数值类型 |
| PRI_MAX | 实际交易最高价 | 数值类型 |
| PRI_MIN | 实际交易最低价 | 数值类型 |
| PRI_AVG | 实际平均交易价 | 数值类型 |
| USED_CAP_AMUT | 实际使用资金总额 | 数值类型 |


