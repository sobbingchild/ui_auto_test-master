'''
权限交接
'''
# 权限交接

transfer_perm = "//button[@data-test-id='myPerm_btn_transferPerm']"
# 用户组权限交接
checkbox_user_g = "//span[contains(.,'test_ui_usermg_name')]/../../..//span[@class='bk-checkbox']"
# 点击交接人
transfer = "//div[@class='user-selector-layout']/div"
# 输入交接人
transfer_span = "//div[@class='user-selector-layout']/div//span"
# 交接理由

transfer_reason = "//div[@class='bk-form-content']//textarea"
# 提交用户组权限交接
commit_transfer = "//div[@class='fixed-action']/button//span"

# 用户组名
test_ui_usermg_name = "//span[contains(.,'test_ui_usermg_name')]"
# PaaS权限
PaaS = "PaaS"
# 自定义权限交接
paas_custom_perm = "//label[contains(.,'自定义权限交接')]/../../div[@class='content']//label[@class='system-list-item-title']"
# paas平台的开发者中心权限
paas_dev_perm = "//div[@class='system-list-item-content']//tr[1]/td[1]//span"

# TESTUI分级管理员权限交接

check_rating_man = "//tr/td/div[contains(.,'TESTUI分级管理员')]/../..//span[@class='bk-checkbox']"

# 系统管理员

check_sys_man = "//tr/td//div[contains(.,'PaaS平台系统管理员')]/../..//span"


# iam右上角的用户名
iam_name = "//p[@data-test-id='header_btn_triggerSwitchRole']"

# 普通用户iam退出登录
iam_login_out = "//section//div[@class='operation right']/div"

# 我的权限导航
nav_myperm = "//div[@data-test-id='nav_menu_switchNav_myPermNav']"

# 申请理由输入框

textarea = "//section//div[@class='bk-textarea-wrapper']/textarea"
resean_text = "TEST UI 申请权限的理由"

# 没有权限的文案,表示交接完了

#no_perm_text = "您还没有任何权限"
no_perm = "//div[@class='empty-wrapper']"
