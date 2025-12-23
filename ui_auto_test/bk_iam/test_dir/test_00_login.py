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
import bk_iam.settings as settings
import time
import bk_iam.page.login as login
from bk_iam.bk_exception import LoginError
from pre_data.user_api import UserApi

userApi = UserApi()


# 已完成
class Login(seldom.TestCase):

    def test_01_new_user(self):
        '''新建用户'''
        # 提前创建用户
        username = userApi.add_user()
        self.wait(1)
        print("username", username)
        # 重置密码
        pwd = userApi.user_passw()
        print("pwd", pwd)
        settings.NEW_USER = username
        settings.NEW_PWD = pwd
        '''
        创建交接用户
        '''
        usernameB = userApi.add_user()
        self.wait(1)
        print("usernameB", usernameB)
        # 重置密码
        pwdB = userApi.user_passw()
        print("pwdB", pwdB)
        settings.B_USER = usernameB
        settings.B_PWD = pwdB
        time.sleep(2)
        self.test_login(username,pwd)

    def test_login(self, username=settings.USER_NAME, pwd=settings.PASSWORD):
        ''' 登录态验证'''
        self.open(settings.IAM_URL)
        time.sleep(2)
        self.set_window(1920, 1080)
        time.sleep(4)
        if self.get_title == settings.LOGIN_TITLE_ENGLISH or self.get_title == settings.LOGIN_TITLE:
            if self.get_title == settings.LOGIN_TITLE_ENGLISH:
                # 判断是否社区版
                msg = self.get_attribute(xpath=login.Login_photo, attribute="src")
                if 'logo_ce' in msg:
                    self.click(xpath=login.switch_language_ce)
                else:
                    self.click(xpath=login.switch_language_ee)
                self.sleep(1)
                if self.get_title != settings.LOGIN_TITLE:
                    raise LoginError('英文切换中文失败，登录页面有缺陷')
                self.input_uername_password(username=username, pwd=pwd)
            elif self.get_title == settings.LOGIN_TITLE:
                self.input_uername_password(username=username, pwd=pwd)
            else:
                raise LoginError('登录页面title不符合规范,测试失败')
        else:
            self.get(settings.IAM_URL)
            # self.wait(3)
            self.assertInTitle(settings.INDEX_TITLE)

    def input_uername_password(self, username, pwd):
        # 输入账号
        self.type(xpath=login.account, text=username)
        # 输入密码
        self.type(xpath=login.password, text=pwd)
        self.click(xpath=login.login_btn)
        self.sleep(3)
        if settings.INDEX_TITLE in self.get_title:
            print("登录成功")
        else:
            raise LoginError('密码账号错误，登录失败')
