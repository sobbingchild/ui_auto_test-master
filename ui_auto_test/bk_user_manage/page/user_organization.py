###切换界面
# 组织架构
Switch_Org = '//div[@class="header-left"]/p/a[1]'
# 用户目录
Switch_Catalog = '//div[@class="header-left"]/p/a[2]'
# 审计
Switch_Audit = '//div[@class="header-left"]/p/a[3]'
# 设置
Switch_Setting = '//div[@class="header-left"]/p/a[4]'

##默认目录操作
Main_Option = '//div[@class="tree-drag-node node-li"]/div/div/div'
Main_New_Org = '//div[@class="show-dropdown-list"]/div[1]/a[1]'
New_Department = '//div[@class="new-department"]//input'

import random as r
import time

time_now = int(time.time())
timeArray = time.localtime(time_now)
otherStyleTime = time.strftime("%m%d%H%M%S", timeArray)

# 填入的组织名称
a1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'ii', 'jj', 'k', 'll', 'm', 'nn']
a2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'ii', 'jj', 'ki', 'll', 'm', 'nn']
a3 = ['ac', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'ii', 'jj', 'k', 'll', 'm', 'nn']
a4 = ['a', 'b', 'c', 'd', 'e', 'f', 'gu', 'h', 'ii', 'jj', 'k', 'll', 'm', 'nn']
a5 = ['a-', 'bw', 'c', 'd', 'e', 'f', 'gw', 'h', 'ii', 'jj', 'k', 'll', 'm', 'nn']
a6 = ['a', 'b', 'c', 'd', 'e', 'fh', 'g', 'h-', 'ii', 'jj', 'k', 'll', 'ml', 'nn']
a7 = ['a', 'bq', 'c', 'd', 'ez', 'f', 'g', 'h', 'i-i', 'jj', 'k', 'll', 'm', 'nn']
a8 = ['ac', 'b', 'c', 'd', 'e', 'f-', 'g', 'h', 'ii', 'jj', 'k', 'lnl', 'm', 'nn']
a9 = ['a', 'b', 'cx', 'd-', 'e', 'f', 'g', 'h', 'ii', 'jvj', 'kb', 'll', 'm', 'nn']
a10 = ['在', '啊', '额', '去', '我', '惹', '她', '有', '哦', '排', '是', '的', '分', '这', "会", "里"]
# for i in range(15):
# Department_Name_Input =r.choice(a1)+r.choice(a6)+r.choice(a7)+r.choice(a8)+r.choice(a9)+otherStyleTime
Department_Name_Input = '自动化测试目录'
Department_Name_2_Input = '自动化测试等待拉取目录'
# Department_Name_Input = "test"
Child_Rename = '修改名称啊啊'

##根组织操作
# 指定名称定位
DepartmentName = "//span[@class='node-title'][contains(text(),'自动化测试目录')]"
DepartmentName2 = "//span[@class='node-title'][contains(text(),'自动化测试等待拉取目录')]"
# 切换到第1个组织
Switch_Department_1 = '//div[@class="tree-content-wrapper"]/ul/li/ul/li[1]/div/div[2]'
# 搜索框
Department_Search = '//input[@placeholder="搜索"]'
Department_Result = '//li[@class="match-item active"]'
Department_Result_Switch = '//div[@class="tree-node first-tree-node active"]/div[1]'
# 组织名称断言
Department_Name = '//span[@class="profile-name text-overflow"]'
# 组织的操作
Department_Option = '//div[@class="tree-node expand active"]/div[3]/i'
Department_Delete = '//div[@class="dropdown-list"]/div[7]'
# Department_New_Child = '//div[@class="dropdown-list"]/div[1]'
Department_New_Child= "//span[@class='node-title node-selected'][contains(text(),'自动化测试目录')]/../div/div/div[1]/a[1]"
Department_Move_Down = '//div[@class="dropdown-list"]/div[3]'
Department_Move_Up = '//div[@class="dropdown-list"]/div[2]'

# 复制ID 复制名称
Department_Copy_Message = '//div[@class="bk-message-content ellipsis"]'
Department_CopyID = '//div[@class="dropdown-list"]/div[5]'
Department_CopyName = '//div[@class="dropdown-list"]/div[6]'
Department_Rename = '//div[@class="dropdown-list"]/div[4]'
#错误信息提示
Message_Error = '//div[@class="bk-message-content ellipsis"]'
None_AllName_Message = "//span[@class='text'][contains(text(),'请填写正确全名')]"

#确认删除
Delete_Confirm = '//div[@class="bk-dialog bk-info-box"]/div/div[4]/div/button[1]'

##重命名
Department_Rename_Input = '//div[@class="editor-department-wrapper"]/ul/li/div/input'
Rename_Confirm = '//div[@class="bk-dialog-wrapper"]/div/div/div[4]/div/button[1]'

# 下级组织操作
Child_Name_Input = '//div[@class="add-child-wrapper"]/ul/li/div/input'
Child_Name = '下级组织'
Child_Name2 = '下级组织1'
Child_Confirm = '//div[@class="add-child-wrapper"]/../../../div[4]/div/button[1]'
Child_Switch = '//div[@class="tree-content-wrapper"]/ul/li/ul/li[2]/ul'
Child_Position = "//div[@class='depart-name'][contains(text(),'下级组织')]"
Child_BeRename = "//div[@class='depart-name'][contains(text(),'下级组织1')]"

# 组织名称
Department_Name_Text = '//div[@class="tree-content-wrapper"]/ul/li/ul/li[4]/div/div[2]/div[2]'

##用户操作
# 首次添加用户
New_User_First = '//div[@class="button-container"]/button[1]'
# 二次添加用户
New_User_Step1 = '//div[@class="table-actions-left-container local-type"]/div[1]/div[1]/button'
# 新增用户
New_User_Step2 = '//div[@class="table-actions-left-container local-type"]/div[1]/div[3]/ul/li[1]/a'
# 从其它组织拉取
New_User_Step3 = '//div[@class="table-actions-left-container local-type"]/div[1]/div[3]/ul/li[2]/a'
# 拉取输入
Pull_User_Name = '//div[@class="batch-content-wrapper"]/div/div[1]'
Pull_User_Name_Search = '//input[@class="bk-select-search-input"]'
Pull_User_Name_Select = '//div[@class="bk-options-wrapper"]/ul/li[1]/div/div/span'
Pull_Confirm = '//div[@class="bk-dialog-wrapper"]/div/div/div[4]/div/button[1]'
Pull_Close_Down = '//div[@class="batch-content-wrapper"]/div/div[1]'
# 搜索
Search_User = '//div[@data-placeholder="输入用户名/中文名，按Enter搜索"]'
Search_User_List = '//ul[@class="bk-search-list-menu"]/li[1]'
# 选择第一条结果
# Check_User = '//div[@class="tbody-container table-container"]/table/tbody/tr/td/label/input'
Check_User = '//div[@class="thead-container table-container"]/table/thead/tr/th/label/input'
# 更多操作
User_MoreOption = '//div[@class="table-actions-left-container local-type"]/div[2]/div[1]/button'
# 设置所在组织
User_Org = '//div[@class="table-actions-left-container local-type"]/div[2]/div[3]/ul/li[1]/a'
##移除组织
User_RemoveOrg = '//div[@class="selected-content"]/ul/li[1]/i'

# 批量删除
User_Delete = '//div[@class="table-actions-left-container local-type"]/div[2]/div[3]/ul/li[1]/a'

##新增用户输入框
User_Name = '//div[@class="fill-infor-wrapper"]/div[1]/form/div[1]/div/div/div/div/input'
User_AllName = '//div[@class="fill-infor-wrapper"]/div[1]/form/div[2]/div/div/div/div/input'
User_Email = '//div[@class="fill-infor-wrapper"]/div[1]/form/div[3]/div/div/div/div/input'
User_Number = '//div[@class="fill-infor-wrapper"]/div[1]/form/div[4]/div/div/div/input'
User_Date = '//div[@class="bk-date-picker-rel"]'
Date_NextYear = '//i[@class="bk-icon icon-angle-double-right"]'
Date_Select = '//div[@class="bk-date-picker-cells"]/span[20]'
##操作第一个用户
User_Select = '//div[@class="tbody-container table-container"]/table/tbody/tr[1]'
##编辑按钮
User_Edit = '//button[@class="editor-btn bk-primary bk-button-normal bk-button"]'
#充值密码
User_Reset_Password = '//div[@class="reset"]'
User_Reset_Input = '//input[@autocomplete="new-password"]'
Reset_Confirm = '//div[@class="reset-btn"]/button[1]'
Reset_Cancel = '//div[@class="reset-btn"]/button[2]'
Reset_Password_Input = ''

# 禁用按钮
User_Close = '//div[@class="action-btn-wrapper"]/button[2]'
# 断言是否禁用
User_Close_Assert = '//p[@class="forbid-text"]'
##删除按钮
# User_Delete = '//div[@class="action-btn-wrapper"]/button[3]'
##批量删除
All_Delete = '//div[@class="table-actions-left-container local-type"]/div[2]/div[3]/ul/li[2]'

##
Button_Save = '//button[@class="btn bk-primary bk-button-normal bk-button"]'
