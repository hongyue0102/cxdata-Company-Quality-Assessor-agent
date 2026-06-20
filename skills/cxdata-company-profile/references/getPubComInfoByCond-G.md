# 公司基本信息-通用 (getPubComInfoByCond-G)

**API_ID:** getPubComInfoByCond-G

#### 输入参数

| 参数名 | 参数中文名 | 数据类型 | 是否必填 | 默认值 |
|--------|------------|----------|----------|----------|
| comChiName | 公司中文名称 | 字符类型 | 否 |  |
| comNameHist | 公司曾用名 | 字符类型 | 否 |  |
| regAddr | 公司注册地址 | 字符类型 | 否 |  |
| estDate | 公司成立日期 | 字符类型 | 否 |  |
| uniSocCreCode | 统一社会信用代码 | 字符类型 | 否 |  |
| pageNum | 页码 | Integer | 是 | 1 |
| pageSize | 每页条数 | Integer | 是 |  |

#### 输出参数

| 参数名 | 参数中文名 | 数据类型 |
|--------|------------|----------|
| COM_CHI_NAME | 公司中文名称 | 字符类型 |
| COM_CHI_SHORT_NAME | 公司中文简称 | 字符类型 |
| COM_ENG_NAME | 公司英文名称 | 字符类型 |
| COM_ENG_SHORT_NAME | 公司英文简称 | 字符类型 |
| COM_SPE_SHORT_NAME | 公司拼音简称 | 字符类型 |
| COM_NAME_HIST | 公司曾用名 | 字符类型 |
| REG_CAP | 注册资本 | 数值类型 |
| CURY_TYPE_PAR | 货币类型 | 数值类型 |
| AREA_CHI_SHORT_NAME1 | 注册地所属省/直辖市 | 字符类型 |
| AREA_CHI_SHORT_NAME2 | 注册地所在市/区 | 字符类型 |
| REG_ADDR | 公司注册地址 | 字符类型 |
| AREA_UNI_CODE | 注册地所属区域 | 数值类型 |
| REG_ADDR_POST | 公司注册地址邮编 | 字符类型 |
| OFFI_ADDR | 公司办公地址 | 字符类型 |
| OFFI_ADDR_POST | 公司办公地址邮编 | 字符类型 |
| COM_ADDR | 公司联系地址 | 字符类型 |
| COM_ADDR_POST | 公司联系地址邮编 | 字符类型 |
| COM_WEB | 公司网址 | 字符类型 |
| LEG_PER | 法人代表 | 字符类型 |
| GEN_MAN | 总经理 | 字符类型 |
| COM_TEL | 公司电话 | 字符类型 |
| CUS_CON_TEL | 客服联系电话 | 字符类型 |
| COM_FAX | 公司传真 | 字符类型 |
| MAIL_ADDR | 公司电子邮件地址 | 字符类型 |
| EST_DATE | 公司成立日期 | 字符类型 |
| IC_REG_CODE | 工商登记号_营业执照注册号 | 字符类型 |
| TYPE_BIG_PAR | 公司类型 | 数值类型 |
| TYPE_MID_PAR | 公司类型中类 | 数值类型 |
| TYPE_SMA_PAR | 公司类型小类 | 数值类型 |
| STA_PAR | 公司状态 | 数值类型 |
| COM_ATTR_PAR | 公司性质 | 数值类型 |
| PARE_COM_CODE | 母公司码 | 数值类型 |
| TOP_ORG_CODE | 顶级机构代码 | 数值类型 |
| HIGH_LEVEL_ORG_CODE | 上一级机构代码 | 数值类型 |
| MAIN_BUS | 公司主营业务 | 字符类型 |
| SID_BUS | 公司兼营业务 | 字符类型 |
| COM_PRO | 公司简介 | 字符类型 |
| COM_HIS | 成立情况与历史沿革 | 字符类型 |
| TER_ACC_OFFI_CODE | 境内会计师事务所 | 数值类型 |
| TER_ACC | 境内会计师 | 字符类型 |
| LAWER_OFFI_CODE | 律师事务所 | 数值类型 |
| COM_LAWER | 经办律师 | 字符类型 |
| CAP_ESTI_ORG_CODE | 资产评估机构 | 数值类型 |
| ESTI_STAFF | 经办评估人员 | 字符类型 |
| DIS_DATE | 解散日期 | 日期类型 |
| DIS_REAS | 解散原因 | 字符类型 |
| COM_STP | 董事会秘书 | 字符类型 |
| STP_TEL | 董秘联系电话 | 字符类型 |
| STP_TAX | 董秘传真 | 字符类型 |
| STP_CON_ADDR | 董秘联系地址 | 字符类型 |
| STP_MAIL | 董秘电子邮件地址 | 字符类型 |
| SEC_REPR_NAME | 证券事务代表姓名 | 字符类型 |
| SEC_REPR_TEL | 证券事务代表电话 | 字符类型 |
| SEC_REPR_TAX | 证券事务代表传真 | 字符类型 |
| SEC_REPR_CON_ADDR | 证券事务代表联系地址 | 字符类型 |
| SEC_REPR_MAIL | 证券事务代表电子邮件地址 | 字符类型 |
| INFO_DISC_PER | 信息披露人 | 字符类型 |
| COM_CON_PER | 公司联系人 | 字符类型 |
| COM_ORGA_FORM_PAR | 企业组织形式 | 数值类型 |
| INDU_UNI_CODE_Z | 证监会行业代码 | 数值类型 |
| INDU_UNI_CODE_S | 申万行业代码 | 数值类型 |
| INDU_UNI_CODE_Q | 全球行业代码 | 数值类型 |
| IF_ISS_BOND | 是否发行债券 | 数值类型 |
| COM_LIST_PAR | 公司上市状态 | 数值类型 |
| LIST_MKT | 上市地点 | 数值类型 |
| STK_UNI_CODE_A | A股股票代码 | 数值类型 |
| STK_UNI_CODE_B | B股股票代码 | 数值类型 |
| UNI_SOC_CRE_CODE | 统一社会信用代码 | 字符类型 |
| ORG_CLA_PAR | 企业类型 | 字符类型 |
| OPER_COND | 经营状态 | 字符类型 |
| OPER_STA_DATE | 经营期限自 | 字符类型 |
| OPER_END_DATE | 经营期限至 | 字符类型 |
| PERMIT_DATE | 核准日期 | 字符类型 |
| REG_AUTH | 登记机关 | 字符类型 |
| ORG_DELE | 企业代表 | 字符类型 |
| ORG_DELE_PAR | 企业代表类型参数 | 数值类型 |


