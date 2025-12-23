# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_01_login.py
   Description : 
   Author :       v_adanchen
   date：          2021/7/9
-------------------------------------------------
"""
import time

import seldom

from bk_itsm import settings

from bk_itsm.page import login_page

from bk_itsm.bk_exception import LoginError

from bk_itsm.page import login

class LoginBase(seldom.TestCase):
    def _test_login(self, username=settings.USER_NAME, pwd=settings.PASSWORD):
        ''' 登录态验证'''
        self.open(settings.ITSM_URL)
        time.sleep(10)
        self.max_window()
        if self.get_title == settings.LOGIN_TITLE_ENGLISH or self.get_title == settings.LOGIN_TITLE:
            if self.get_title == settings.LOGIN_TITLE_ENGLISH:
                # 判断是否社区版
                msg = self.get_attribute(xpath=login_page.Login_photo,attribute="src")
                if 'logo_ce' in msg:
                    self.click(xpath=login_page.switch_language_ce)
                else:
                    self.click(xpath=login_page.switch_language_ee)
                self.sleep(10)
                if self.get_title != settings.LOGIN_TITLE:
                    raise LoginError('英文切换中文失败，登录页面有缺陷')
                self.input_username_password(username=username, pwd=pwd)
                # version = self.get_text(login_page.version_footer)
                # print(version)
                # if '3.5' in version:
                #     self.click(xpath=login_page.log_close)
                # elif '3.6' in version:
                #     self.click(xpath=login_page.log_close_2)
                self.click(xpath=login.project)
                self.click(xpath=login.select_project)
                self.click(xpath=login.default_project)
            elif self.get_title == settings.LOGIN_TITLE:
                self.input_username_password(username=username, pwd=pwd)
                # version = self.get_text(login_page.version_footer)
                # print(version)
                # if '3.5' in version:
                #     self.click(xpath=login_page.log_close)
                # elif '3.6' in version:
                #     self.click(xpath=login_page.log_close_2)
                self.click(xpath=login.project)
                self.click(xpath=login.select_project)
                self.click(xpath=login.default_project)
            else:
                raise LoginError('登录页面title不符合规范,测试失败')
        else:
            self.open(settings.ITSM_URL)
            self.wait(10)
            self.assertInTitle(settings.INDEX_TITLE)

    def input_username_password(self, username, pwd):
        # 输入账号
        self.type(xpath=login_page.account, text=username)
        # 输入密码
        self.type(xpath=login_page.password, text=pwd)
        self.click(xpath=login_page.login_button)
        time.sleep(10)
        # self.wait(1)
        if settings.INDEX_TITLE in self.get_title:
            print("登录成功")
        else:
            raise LoginError('密码账号错误，登录失败')

class Login(LoginBase):
    def test_login(self):
        self._test_login()