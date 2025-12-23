#新增目录按钮
New_Catalog = '//div[@class="button-container"]/button'

#首页操作(仅限第二条,多余需要清除)
###停用/启用切换
SwitcherButton = "//span[@class='text-overflow-hidden'][contains(text(),'敬东测试1')]/../../../../td[4]/div/label/input"
##删除
DeleteButton = "//span[@class='text-overflow-hidden'][contains(text(),'敬东测试1')]/../../../../td[5]/div/span[3]"
DeleteMicrosoftButton = "//span[@class='text-overflow-hidden'][contains(text(),'敬东测试1')]/../../../../td[5]/div/span[2]"
##进入目录的编辑界面
EditButton = "//span[@class='text-overflow-hidden'][contains(text(),'敬东测试1')]"


#选择目录类型
###本地目录
Local_Catalog = '//ul[@class="catalog-list"]/li[1]'
Microsoft_Catalog = '//ul[@class="catalog-list"]/li[2]'
OpenLDAP_Catalog = '//ul[@class="catalog-list"]/li[3]'
##本地目录操作
#目录名
LocalCatalog_Name = '//div[@class="name-container"]/div[1]/div[2]/div/input'
LocalCatalogName = '敬东测试1'
LocalCatalog_Domain = '//div[@class="catalog-setting-step set-basic"]/div[2]/div[2]/div[1]/input'
LocalCatalogDomain = 'test1'
#密码长度
Local_Number = '//div[@class="catalog-setting-step local-passport"]/div[1]/div[2]/div/input'
#密码包含
Password_Lower = '//div[@class="catalog-setting-step local-passport"]/div/div[2]/div[2]/label[1]/span[1]'
Password_Upper = '//div[@class="catalog-setting-step local-passport"]/div/div[2]/div[2]/label[2]/span[1]'
Password_Int = '//div[@class="catalog-setting-step local-passport"]/div/div[2]/div[2]/label[3]/span[1]'
Password_Special = '//div[@class="catalog-setting-step local-passport"]/div/div[2]/div[2]/label[4]/span[1]'
#密码有效期
Date_1Month = '//div[@class="catalog-setting-step local-passport"]/div/div[4]/div[2]/button[3]'
Date_3Month = '//div[@class="catalog-setting-step local-passport"]/div/div[4]/div[2]/button[2]'
Date_6Month = '//div[@class="catalog-setting-step local-passport"]/div/div[4]/div[2]/button[3]'
Date_1Year = '//div[@class="catalog-setting-step local-passport"]/div/div[4]/div[2]/button[4]'
Date_Forever = '//div[@class="catalog-setting-step local-passport"]/div/div[4]/div[2]/button[5]'
#密码错误次数
Error_3Times = '//div[@class="catalog-setting-step local-passport"]/div/div[5]/div[2]/button[1]'
Error_5Times = '//div[@class="catalog-setting-step local-passport"]/div/div[5]/div[2]/button[2]'
Error_10Times = '//div[@class="catalog-setting-step local-passport"]/div/div[5]/div[2]/button[3]'
#自动解锁时间
Unlock_Time = '//div[@class="catalog-setting-step local-passport"]/div/div[6]/div[2]/div[1]/input'
#初始密码获取方式
Random_Password = '//div[@class="email-config-container"]/label/input'
Init_Password = '//div[@class="catalog-setting-step local-passport"]/div/div[7]/div[2]/label/input'
Email_Password = '//div[@class="catalog-setting-step local-passport"]/div/div[7]/div[3]/div/label/input'
#提交按钮
Password_Submit = '//div[@class="catalog-setting-step local-passport"]/div[4]/button[3]'

#Microsoft操作
#根目录
# M_King_Input = '//input[@placeholder="例如：ldap://127.0.0.1:389 或 ldaps://127.0.0.1:636"]'
M_King_Input = '//div[@class="catalog-setting-step set-connection"]/div[1]/div[2]/div/input'
M_BaseDN= '//div[@class="catalog-setting-step set-connection"]/div[5]/div[2]/div[1]/input'
M_BaseDN_Input = '范德萨'
M_King_Url = 'ldap://198.168.1.1:389'
#用户名,密码
M_Username= '//div[@class="catalog-setting-step set-connection"]/div[6]/div[2]/div[1]/input'
M_Username_Input = 'aaa'
M_Password = '//div[@class="catalog-setting-step set-connection"]/div[7]/div[2]/div[1]/input'
M_Password_Input= 'bbb'
#字段设置
M_Agent = '//div[@class="set-field"]/div[1]/div[1]/div[2]/div[1]/div[2]/div/input'
M_Agent_Name = 'aaa'
#Microsoft下一步
M_Nextstep = '//div[@class="catalog-setting-step set-connection"]/div[9]/button[3]'
#字段设置下一步
M_Commit = '//div[@class="set-field"]/div[6]/button[3]'


###编辑界面操作
Base_Settings = '//div[@class="steps set-steps"]/div[3]'
Index_Settings = '//div[@class="steps set-steps"]/div[4]'
#保存按钮
SaveButton = '//div[@class="scroll-container"]/div[1]/div[3]/button[1]'
SaveButton2 = '//div[@class="catalog-setting-step set-connection"]/div[9]/button[1]'
SaveButton3 = '//div[@class="set-field"]/div[5]/button[1]'



#下一步按钮
LocalCatalog_Confirm = '//div[@class="catalog-setting-step set-basic"]/div[3]/button[2]'
Account_Confirm = '//div[@class="catalog-setting-step set-account"]/div[4]/button[3]'


###继续按钮
NewCatalogConfirm = '//button[@class="king-button bk-primary bk-button-normal bk-button"]'