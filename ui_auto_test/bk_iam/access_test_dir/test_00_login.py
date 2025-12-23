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
import bk_iam.page.login as login
from bk_iam.bk_exception import LoginError
from bk_iam import settings
from bk_iam.base_operate import BaseOperate
# import os
#
# PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
# base = BaseOperate()
# base.path = PATH('../../../config.ini')
from public_method.login import LoginBase
# 已完成
# class Login(seldom.TestCase):
#     def test_login(self):
#         ''' 登录态验证'''
#         # userApi = UserApi()
#         # # 提前创建用户
#         # username = userApi.add_user()
#         # self.wait(1)
#         # print("username", username)
#         # # 重置密码
#         # pwd = userApi.user_passw()
#         # print("pwd", pwd)
#         # settings.NEW_USER = username
#         # settings.NEW_PWD = pwd
#         self.open(settings.IAM_URL)
#         self.set_window(1920, 1080)
#         self.wait(3)
#         base.write_data(key='original_flow', value='lFALSE')
#         if self.get_title == settings.LOGIN_TITLE_ENGLISH or self.get_title == settings.LOGIN_TITLE:
#             if self.get_title == settings.LOGIN_TITLE_ENGLISH:
#                 # 判断是否社区版
#                 msg = self.get_attribute(xpath=login.Login_photo, attribute="src")
#                 if 'logo_ce' in msg:
#                     self.click(xpath=login.switch_language_ce)
#                 else:
#                     self.click(xpath=login.switch_language_ee)
#                 self.sleep(1)
#                 if self.get_title != settings.LOGIN_TITLE:
#                     raise LoginError('英文切换中文失败，登录页面有缺陷')
#                 #self.input_uername_password(username=username, pwd=pwd)
#                 self.input_uername_password(username=settings.USER_NAME, pwd=settings.PASSWORD)
#             elif self.get_title == settings.LOGIN_TITLE:
#                 #self.input_uername_password(username=username, pwd=pwd)
#                 self.input_uername_password(username=settings.USER_NAME, pwd=settings.PASSWORD)
#             else:
#                 raise LoginError('登录页面title不符合规范,测试失败')
#         else:
#             self.open(settings.IAM_URL)
#             # self.wait(3)
#
#     def input_uername_password(self, username, pwd):
#         # 输入账号
#         self.type(xpath=login.account, text=username)
#         # 输入密码
#         self.type(xpath=login.password, text=pwd)
#         self.click(xpath=login.login_btn)
#         self.sleep(3)
#         if settings.INDEX_TITLE in self.get_title:
#
#             print("登录成功")
#
#             self.wait(10)
#         else:
#             raise LoginError('密码账号错误，登录失败')

class Login(LoginBase):
    def test_login(self):
        ''' 登录态验证'''
        self._test_login(target_url=settings.IAM_URL, index_title=settings.INDEX_TITLE)
