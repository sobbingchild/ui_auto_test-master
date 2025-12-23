# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_00_login.py
   Description : 
   Author :       v_adanchen
   date：          2021/1/19
-------------------------------------------------
"""
import seldom
import bk_itsm.settings as settings
import time
import bk_itsm.page.login as page

#已完成
class Login(seldom.TestCase):
    def test_login(self,username=settings.USER_NAME,pwd=settings.PASSWORD):
        """登录"""
        try:
            self.open(settings.ITSM_URL)
            self.set_window(1920, 1080)
            self.wait(3)
            if self.get_title == settings.LOGIN_TITLE_ENGLISH:
                self.click(xpath=page.language)
                time.sleep(1)
            if self.get_title == settings.LOGIN_TITLE:
                # 输入账号
                self.type(xpath=page.account, text=username)
                # 输入密码
                self.type(xpath=page.password, text=pwd)
                self.click(xpath=page.login_btn)
                self.wait(1)
                self.assertTitle(settings.INDEX_TITLE)
            else:
                self.open(settings.ITSM_URL)
                self.wait(3)
                self.assertTitle(settings.INDEX_TITLE)
                print("登录成功")
            self.wait(5)
        except BaseException as e:
            print("登录失败")


