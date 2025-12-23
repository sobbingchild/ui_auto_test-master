# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ord_member.py
   Description : 普通用户
   Author :       v_adanchen
   date：          2022/4/8
-------------------------------------------------
"""

# 权限申请

perm_ply = "//div[@data-test-id='nav_menu_switchNav_permApplyNav']"

custom_perm = "//div[@class='info']//span"

select_system = '//div[@class="bk-tooltip bk-select-dropdown"]'

select_sops = '//li[@displayname="标准运维(bk_sops)"]'

create_project = '//span[text()="创建项目"]'

resean_type = "//div[@class='content']//textarea[@type='textarea']"
# 提交
commit_ply = "//button[@class='bk-primary bk-button-normal bk-button']"
resean_text = "TEST UI 申请权限的理由"

# itsm右上角的用户名
itsm_name = "//div[@data-test-id='navigation-popover-user']"

loginout_itsm = "//ul[@class='nav-operate-list']/li[2]"

# iam右上角的用户名
iam_name = "//p[@data-test-id='header_btn_triggerSwitchRole']"

# 普通用户iam退出登录
iam_login_out = '//div[@title="退出登录"]'

# 我的审批
nav_appro = "//div[@data-test-id='nav_menu_switchNav_approvalNav']/span"

# ITSM的通过文本

itsm_appro_pass = "//tr[1]/td//span[contains(.,'通过')]"
# 确定通过
itsm_appro_confrim = "//div[@class='bk-dialog-footer']//button[@name='confirm']"

# 我的权限导航
nav_myperm = "//div[@data-test-id='nav_menu_switchNav_myPermNav']"

# 我的权限-自定义权限点击
#custom_review = '//span[text()="自定义权限"]'
custom_review = '//span[text()="自定义权限"]/../../../div'

# PaaS权限
Sops = "创建项目"

Sops_permission = '//div[@class="iam-perm-item myPerm-perm-item iam-perm-ext-reset-cls"]'
# 定位paas模块

paas_perm = "//div[@class='sub-title']/..//label[contains(.,'PaaS')]"


'''
普通用户的其他权限申请
'''

# test_ui_usermg_name 勾选用户组名称

user_g_name = "//span[@title='test_ui_usermg_name']/../../..//label/span"

# 申请理由输入框

textarea = "//section//div[@class='bk-textarea-wrapper']/textarea"

# 提交
button_commit = "//div[@role='dynamic-position']//button"

# 撤销按钮，用于判断审批中状态

revoke = "//div[@class='action']//button//span"

revoke_text = "撤销"
