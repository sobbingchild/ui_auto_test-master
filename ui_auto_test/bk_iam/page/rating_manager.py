# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     rating_manager.py
   Description : 
   Author :       v_adanchen
   date：          2022/4/21
-------------------------------------------------
"""

# 右上角超级管理员
super_admin = "//p[@data-test-id='header_btn_triggerSwitchRole']"

# 身份搜索
search_id = "//section[@class='iam-grading-admin-list-wrapper']//div[@class='bk-input-text']/input"

# 搜索匹配的管理员选项
search_admin = "//section[@class='iam-grading-admin-list-wrapper']/ul/li[1]"

rating_admin = "TESTUI分级管理员"

# 导航栏权限模板
nav_perm_model = "//div[@data-test-id='nav_menu_switchNav_permTemplateNav']"
new_model = "//button[@data-test-id='permTemplate_btn_create']"
model_name_input = "//div[@data-test-id='permTemplate_input_templateName']//input"
dev_check = "//label[@data-test-id='permTemplate_checkbox_action']"
commit_model = "//button[@data-test-id='permTemplate_btn_createSubmit']"

model_name = "test_ui_temp_name"

# 用户组权限

nav_userg = "//div[@data-test-id='nav_menu_switchNav_userGroupNav']"
# 新建用户组
new_user_g = "//button[@data-test-id='group_btn_create']"
# 用户组名称
user_g_name_input = "//div[@data-test-id='group_input_groupName']//input"
# 用户组名

user_g_name = "test_ui_user_name"
# 用户描述
user_g_desc = "//div[@data-test-id='group_input_groupDesc']//textarea"
# 添加组权限
add_g_perm = "//div[@data-test-id='group_btn_showAddGroupPerm']"
# 勾选模板
model_check = "//span[@title='test_ui_temp_name']/../../..//span[@class='bk-checkbox']"

# 点击确定
model_confirm = "//button[@data-test-id='group_btn_addGroupConfirm']"
# 点击添加组成员
user_g_menber = "//div[@data-test-id='group_btn_showAddGroupMember']"
# 点击默认目录
def_fdir = "//div[@data-test-id='group_addGroupMemberDialog_tree_member']/div[@class='render-wrapper']//span"

# 选择组织架构的总公司
user_g_check = "//div[@data-test-id='group_addGroupMemberDialog_tree_member']//div[@class='node-item'][2]/div[@class='node-radio']"

# 确定添加成员
user_g_confirm = "//button[@data-test-id='group_btn_addMemberConfirm']"
# 创建用户组
user_commit = "//button[@data-test-id='group_btn_createSubmit']"
'''
删除用户组
'''
# 删除用户组
del_user_g = "//span[@title='test_ui_user_name']/../../..//span[contains(.,'删除')]"
del_userg_confirm = "//div[@class='operate-buttons']//span[contains(.,'确定')]"

# 删除模板
del_model = "//span[@title='test_ui_temp_name']/../../..//span[contains(.,'删除')]"
del_model_confirm = "//div[@class='footer-wrapper']//span[contains(.,'确定')]"

'''
#移除用户组成员
'''
# 点击用户组名 user_g_name


# 点击移除

remove_users = ""

# 确定移除
remove_comfirm = ""

# 点击返回

come_back = ""
