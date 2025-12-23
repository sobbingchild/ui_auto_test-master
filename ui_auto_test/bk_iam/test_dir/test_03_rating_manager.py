# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_03_rating_manager.py
   Description : 
   Author :       v_adanchen
   date：          2022/4/22
-------------------------------------------------
"""
import seldom
import bk_iam.page.rating_manager as page

class RatingManager(seldom.TestCase):

    def test_00_swich_admin_user(self):
        '''从超级管理员切换到分级管理员'''
        self.click(xpath=page.super_admin)
        self.click(xpath=page.search_id)
        self.type(xpath=page.search_id, text=page.rating_admin)
        self.click(xpath=page.search_admin)
        self.wait(2)

    def test_01_create_model(self):
        '''创建模板'''
        self.click(xpath=page.nav_perm_model)
        self.click(xpath=page.new_model)
        self.wait(2)
        self.click(xpath=page.model_name_input)
        self.type(xpath=page.model_name_input,text=page.model_name)
        self.click(xpath=page.dev_check)
        self.wait(2)
        self.click(xpath=page.commit_model)


    def test_02_create_useg(self):
        '''创建用户组'''
        self.wait(2)
        self.click(xpath=page.nav_userg)
        self.click(xpath=page.new_user_g)
        self.click(xpath=page.user_g_name_input)
        self.type(xpath=page.user_g_name_input,text=page.user_g_name)
        self.click(xpath=page.user_g_desc)
        self.type(xpath=page.user_g_desc,text=page.user_g_desc)
        self.click(xpath=page.add_g_perm)
        self.click(xpath=page.model_check)
        self.click(xpath=page.model_confirm)
        self.click(xpath=page.user_g_menber)
        self.wait(2)
        self.click(xpath=page.def_fdir)
        self.click(xpath=page.user_g_check)
        self.click(xpath=page.user_g_confirm)
        self.click(xpath=page.user_commit)






