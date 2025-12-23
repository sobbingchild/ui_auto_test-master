# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_12_del_usergroup.py
   Description : 
   Author :       v_adanchen
   date：          2021/12/27
-------------------------------------------------
"""
import seldom
from bk_itsm.page import user_group as page
import time
from bk_itsm.test_dir import test_01_login as login


class DelUserG(seldom.TestCase):
    def test_del_user_g(self):
        """"删除用户组"""
        login.Login.test_login(self)
        self.click(xpath=page.project)
        self.click(xpath=page.nav_user_group)
        time.sleep(10)
        self.click(xpath=page.del_group)
        # self.execute_script("arguments[0].click();", page.del_group)
        time.sleep(3)
        self.click(xpath=page.confirm_del)
        time.sleep(1)

