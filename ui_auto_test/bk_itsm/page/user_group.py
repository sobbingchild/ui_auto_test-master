# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     user_group.py
   Description : 
   Author :       v_adanchen
   date：          2021/10/21
-------------------------------------------------
"""
project = "//a[@data-test-id='navigation-router-navRouter-project']"
nav_user_group = "//a[@data-test-id='navigation-menu-projectRoles']"
add_user_group = "//button[@data-test-id='userGroup_button_create']"

group_name = "//div[@data-test-id='role-input-roleName']//input"

group_menbersc = "//div[@data-test-id='role-input-staffList']//div[@test-posi-id='bk-member-selector']//div[@class='user-selector-layout']"

group_menberk = "//div[@data-test-id='role-input-staffList']//div[@test-posi-id='bk-member-selector']//div[@class='user-selector-layout']//span"
group_menberk2 = "//div[@data-test-id='role-input-staffList']//div[@test-posi-id='bk-member-selector']//div[@class='user-selector-layout']//span[2]"

add_comfirm = "//div[@class='bk-dialog-footer']/div/button[@name='confirm']"

edit_group = ""

TEST_USERS_NAME = "TESTERS"

TEST_USERS_MENBERS_ADMIN = "admin"
TEST_USERS_MENBERS_ADAN = "adan"

# 编辑


# 删除用户组

# del_group = "//span[@title='TESTERS']/../../../td[6]/div/button[2]"
del_group = "//div[4]/div[2]/table/tbody/tr[1]/td[6]/div/button[2]/div/span"

confirm_del = "//div[@class='footer-wrapper']//button[@name='confirm']"
