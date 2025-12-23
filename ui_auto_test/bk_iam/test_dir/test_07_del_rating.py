# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_07_del_rating.py
   Description : 
   Author :       v_adanchen
   date：          2022/4/26
-------------------------------------------------
"""
import seldom
from bk_iam.page import rating_manager as page


class DelRating(seldom.TestCase):
    def test_00_swich_id(self):
        '''切换用户身份'''
        self.click(xpath=page.super_admin)
        self.click(xpath=page.search_id)
        self.type(xpath=page.search_id, text=page.rating_admin)
        self.click(xpath=page.search_admin)
        self.wait(2)

    # def test_01_remove_users(self):
    #     '''移除用户'''
    #     self.click(xpath=page.nav_userg)
    #     self.wait(2)
    #     self.click(xpath=page.user_g_name)
    #     self.click(xpath=page.remove_users)
    #     self.click(xpath=page.remove_comfirm)
    #     self.click(xpath=page.come_back)
    #     self.wait(2)

    def test_01_del_userg(self):
        '''移除用户组'''
        self.click(xpath=page.nav_userg)
        self.wait(2)
        self.click(xpath=page.del_user_g)
        self.click(xpath=page.del_userg_confirm)
        self.wait(2)

    def test_02_del_model(self):
        '''删除权限模板'''

        self.click(xpath=page.nav_perm_model)
        self.wait(2)
        self.click(xpath=page.del_model)
        self.click(xpath=page.del_model_confirm)
        self.wait(2)
