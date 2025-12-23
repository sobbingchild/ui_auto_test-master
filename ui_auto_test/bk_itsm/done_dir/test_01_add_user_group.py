# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_02_add_user_group.py
   Description : 
   Author :       v_adanchen
   date：          2021/10/21
-------------------------------------------------
"""
import seldom
import bk_itsm.page.user_group as page
from bk_itsm.access_test_dir import test_01_login as login
from public_method.keyboard_operation import MyWebDriver
from time import sleep


# 已完成
class AddUserGroup(seldom.TestCase):
    def test_01_add_user_group(self):
        '''新增用户组'''
        login.Login.test_login(self)
        self.click(xpath=page.project)
        self.click(xpath=page.nav_user_group)
        self.click(xpath=page.add_user_group)
        self.type(xpath=page.group_name, text=page.TEST_USERS_NAME)
        self.click(xpath=page.group_menbersc)
        self.type(xpath=page.group_menberk, text=page.TEST_USERS_MENBERS_ADMIN)
        sleep(2)
        MyWebDriver.Keys(xpath=page.group_menberk).enter()
        self.click(xpath=page.add_comfirm)

