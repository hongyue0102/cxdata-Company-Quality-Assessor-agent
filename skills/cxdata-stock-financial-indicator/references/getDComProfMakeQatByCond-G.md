# 公司盈利质量分析-通用 (getDComProfMakeQatByCond-G)

**API_ID:** getDComProfMakeQatByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| stkCode | 股票代码 | 字符类型 | 否 |  |
| stkShortName | 股票简称 | 字符类型 | 否 |  |
| endDate | 截止日期 | 日期类型 | 否 |  |
| sheetMarkPar | 报表合并标志 | 数值类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 | 20 |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| STK_CODE | 股票代码 | 字符类型 |
| STK_SHORT_NAME | 股票简称 | 字符类型 |
| END_DATE | 截止日期 | 日期类型 |
| SHEET_MARK_PAR | 报表合并标志 | 数值类型 |
| NTT_PRO_CASH | 净溢余现金 | 数值类型 |
| NTT_PRO_CASH_PS | 每股净赚钱 | 数值类型 |
| MON_ABI | 赚钱能力所属类型 | 数值类型 |
| NET_PRO_CONT | 净利润的含金量 | 数值类型 |
| NET_PRO_CONT_INDEX | 含金量指数 | 数值类型 |
| MON_ADJU | 应调节额 | 数值类型 |
| MON_TOTAL | 股东专属赚钱总额 | 数值类型 |
| MON_TOTAL_PS | 每股总赚钱 | 数值类型 |
| REAL_NET_ASSE | 真实净资产 | 数值类型 |
| REAL_NET_ASSE_PS | 每股真实净资产 | 数值类型 |
| WELL_DEGR | 殷实度 | 数值类型 |
| WELL_DEGR_PS | 每股殷实度 | 数值类型 |
| WARN_SIGN | 预警信号 | 数值类型 |


