# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_06_del_admin.py
   Description : 
   Author :       v_adanchen
   date：          2022/4/26
-------------------------------------------------
"""
import seldom
from bk_iam.page import super_admin as page
import time
from bk_iam import settings as settings
class DelSuper(seldom.TestCase):
    def test_00_swich_user(self):
        '''切换用户，从普通用户切换到admin'''
        time.sleep(1)
        self.click(xpath=page.right_username)
        self.click(xpath=page.iam_login_out)
        time.sleep(2)
        self.login(settings.USER_NAME, settings.PASSWORD)
        #切换身份，admin从普通身份切换到超级管理员身份
        self.click(xpath=page.right_username)
        self.click(xpath=page.search_id)
        self.type(xpath=page.search_id, text=page.super_admin)
        self.click(xpath=page.search_admin)


    def test_01_del_userg(self):
        '''删除用户组'''
        self.click(xpath=page.nav_usermg)
        self.wait(2)
        self.click(xpath=page.del_user_g)
        self.click(xpath=page.del_userg_confirm)
        self.wait(2)

    def test_02_del_model(self):
        '''删除权限模板'''
        self.click(xpath=page.nav_permi_temp)
        self.wait(2)
        self.click(xpath=page.del_model)
        self.click(xpath=page.del_model_confirm)
        self.wait(2)

    def test_03_quit_userg(self):
        '''退出用户组'''
        self.click(xpath=page.nav_user)
        time.sleep(2)
        self.click(xpath=page.quit_usereg)
        self.click(xpath=page.confirm_quit_userg)
        time.sleep(2)

    # def test_04_remove_sys_admin(self):
    #     '''移除系统管理员'''
    #     self.click(xpath=page.nav_admin)
    #     self.click(xpath=page.sys_man)
    #     self.move_to_element(xpath=page.paas_menber)
    #     self.click(xpath=page.paas_menber_hover)
    #     self.Keys(xpath=page.paas_menber_selector_span3).backspace()
    #     time.sleep(2)
    #     self.Keys(xpath=page.paas_menber_selector_span2).enter()


    def login(self, username, pwd):
        self.delete_all_cookies()
        self.refresh()
        self.sleep(0.5)
        try:
            # 输入账号
            self.type(xpath=page.account, text=username)
            # 输入密码
            self.type(xpath=page.password, text=pwd)
            self.click(xpath=page.login_btn)
            time.sleep(3)
        except BaseException as e:
            print("登录失败", e)