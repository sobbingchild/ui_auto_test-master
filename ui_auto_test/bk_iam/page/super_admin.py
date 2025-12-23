import time

# 右上角的admin
right_username = "//div[@class='user fr']/p[@class='user-name']"
#身份搜索
search_id="//section[@class='iam-grading-admin-list-wrapper']//div[@class='bk-input-text']/input"

# 搜索匹配的管理员选项
search_admin = "//section[@class='iam-grading-admin-list-wrapper']/ul/li[1]"

#超级管理员文本

super_admin="超级管理员"


# 普通用户iam退出登录
iam_login_out = "//section//div[@class='operation right']/div"

##################权限模板
# 左侧导航朗-权限模板
nav_permi_temp = "//div[@data-test-id='nav_menu_switchNav_permTemplateNav']"

# 新建模板按钮
new_perm_temp = "//button[@data-test-id='permTemplate_btn_create']"
# m模板名称输入按钮
temp_name_input = "//div[@data-test-id='permTemplate_input_templateName']/div/input"

# 勾选访问开发者中心
check_dev = "//label[@data-test-id='permTemplate_checkbox_action']/span"

# 提交模板
temp_commit = "//button[@data-test-id='permTemplate_btn_createSubmit']"

# 模板名称
temp_name = "test_ui_perm_temp"

#################用户组
# 左侧导航栏
nav_usermg = "//div[@data-test-id='nav_menu_switchNav_userGroupNav']"
# 新建按钮
new_usermg = "//button[@data-test-id='group_btn_create']"
# 用户组名
usermg_name_input = "//div[@data-test-id='group_input_groupName']/div/input"

# 用户组描述
usermg_desc_input = "//div[@data-test-id='group_input_groupDesc']/div/textarea"

# 用户组名
user_name = "test_ui_usermg_name"
single_user_gname = "test_ui_single_usermg_name"

# 用户组描述名
user_desc = "TEST_UI_DESC"
# 添加用户组权限
add_perm_g = "//div[@data-test-id='group_btn_showAddGroupPerm']"
# 添加用户组成员
add_user_g = "//div[@data-test-id='group_btn_showAddGroupMember']"

# 勾选模板名
check_temp_name = "//div[@data-test-id='group_table_selectPermTemplate']//span[@title='test_ui_perm_temp']/../../..//label"
# 提交用户组权限
user_perm_commit = "//button[@data-test-id='group_btn_addGroupConfirm']"

# 展开用户组
sp_user_g = "//div[@data-test-id='group_addGroupMemberDialog_tree_member']//div[@class='node-item']"
# 目录
def_dir = "//div[@data-test-id='group_addGroupMemberDialog_tree_member']//span[@title='默认目录']"

# 选择总公司,index=1
user_g_check = "//div[@data-test-id='group_addGroupMemberDialog_tree_member']//div[@class='node-item']//div[1]/span"

# 用户组确定按钮
user_g_confirm = "//div[@class='bk-dialog-footer']//button[@data-test-id='group_btn_addMemberConfirm']"

# 提交用户组
usermg_commit = "//button[@data-test-id='group_btn_createSubmit']"

# 手动输入
button_input_menber = "//section[@data-test-id='group_addGroupMemberDialog_tab_switch'][2]"

# 人员输入框
input_erea = "//div[@data-test-id='group_addGroupMemberDialog_input_manualUser']//textarea"

# 添加人员button

button_add_menber = "//button[@data-test-id='group_addGroupMemberDialog_btn_addManualUser']"

# 确定添加
button_comfirm = "//button[@data-test-id='group_btn_addMemberConfirm']"

# 删除用户组
del_user_g = "//span[@title='test_ui_usermg_name']/../../..//span[contains(.,'删除')]"
del_userg_confirm = "//div[@class='operate-buttons']//span[contains(.,'确定')]"

# 删除模板
del_model = "//span[@title='test_ui_perm_temp']/../../..//span[contains(.,'删除')]"
del_model_confirm = "//div[@class='footer-wrapper']//span[contains(.,'确定')]"

####分级管理员

nav_rating_manager = "//div[@class='nav-slider-list']//div[@data-test-id='nav_menu_switchNav_gradingAdminNav']"

new_rating_manager = "//button[@data-test-id='grading_btn_create']"
# 分级管理员名称输入框
name_rating_manager = "//div[@data-test-id='grading_input_name']//input"

# 选择资源授权范围
range_action = "//section[@data-test-id='grading_btn_showAddAction']"
# paas访问权限全选
select_visit = "//span[contains(.,'访问权限')]/../span[@data-test-id='grading_btn_selectAllAction']"
# paas开发者中心
select_dev = "//span[contains(.,'开发者权限')]/../span[@data-test-id='grading_btn_selectAllAction']"

# paas管理权限
select_manager = "//span[contains(.,'管理权限')]/../span[@data-test-id='grading_btn_selectAllAction']"

# 提交资源范围
action_man = "//button[@data-test-id='grading_btn_addActionConfirm']"
# 选择资源实例
man_app = "//div[@class='content']/div[@class='iam-condition-item']/div"
# 无限制
no_limit = "//div[@class='no-limit-wrapper']//label/span"
# 保存资源实例
save_source = "//div[@class='bk-sideslider-footer']//button//span[contains(.,'保存')]"

# 选择人员授权范围
range_menber = "//section[@data-test-id='grading_btn_showAddMember']/span"

# 默认目录
def_dirs = "//span[@title='默认目录']/../i[1]"
# 总公司的radio
company_radio = "//span[@title='总公司']/../div"

comfirm_menber = "//button[@data-test-id='group_btn_addMemberConfirm']"

# 提交
button_commit = "//button[@data-test-id='grading_btn_createSubmit']"

test_ui_rating_name = "TESTUI分级管理员"

# 分级管理员页面的
main_bar = "//div[@class='main-scroller']"

admin = "admin"

# 导航栏-管理员

nav_admin = "//div[@data-test-id='nav_menu_switchNav_settingNav']"
# 点击系统管理员

sys_man = "//ul/li[2]/div"

# paas平台的系统管理员
paas_menber = "//div[contains(.,'PaaS平台')]/../../td//div[@class='user-wrapper']"

paas_menber_hover = "//div[contains(.,'PaaS平台')]/../../td//div[@class='user-wrapper is-hover']"

paas_menber_selector = "//div[contains(.,'PaaS平台')]/../../td//div[@class='user-selector']"
paas_menber_selector_span = "//div[contains(.,'PaaS平台')]/../../td//div[@data-test-id='set_userSelector_editSystemManager']//span"
#第二个用户
paas_menber_selector_span2 = "//div[contains(.,'PaaS平台')]/../../td//div[@data-test-id='set_userSelector_editSystemManager']//span[2]"
#第三个用户，用来删除用的
paas_menber_selector_span3 = "//div[contains(.,'PaaS平台')]/../../td//div[@data-test-id='set_userSelector_editSystemManager']//span[3]"



# 退出用户组
quit_usereg = "//span[@title='test_ui_user_name']/../../../td[6]//span[contains(.,'退出')]"
confirm_quit_userg = "//div[@class='operate-buttons']/button//span[contains(.,'确定')]"
nav_user = "//div[@data-test-id='nav_menu_switchNav_userNav']"


def rating_man_name(name):
    name = name + time.time()
    return name
