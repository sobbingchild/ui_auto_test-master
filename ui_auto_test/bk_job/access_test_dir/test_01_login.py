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

from bk_job import settings

from bk_job.page import login_page

from bk_job.bk_exception import LoginError


class LoginBase(seldom.TestCase):
    def _test_login(self, username=settings.USER_NAME, pwd=settings.PASSWORD):
        ''' 登录态验证'''
        self.open(settings.JOB_URL)
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
                try:
                    self.click(xpath=login_page.log_close)
                except Exception as e:
                    print(e)
                try:
                    self.click(xpath=login_page.log_close_2)
                except Exception as e:
                    print(e)
                self.click(xpath=login_page.show_navigation_bar)
                self.input_biz()
            elif self.get_title == settings.LOGIN_TITLE:
                self.input_username_password(username=username, pwd=pwd)
                # version = self.get_text(login_page.version_footer)
                # print(version)
                # if '3.5' in version:
                #     self.click(xpath=login_page.log_close)
                # elif '3.6' in version:
                #     self.click(xpath=login_page.log_close_2)
                try:
                    self.click(xpath=login_page.log_close)
                except Exception as e:
                    print(e)
                try:
                    self.click(xpath=login_page.log_close_2)
                except Exception as e:
                    print(e)
                self.click(xpath=login_page.show_navigation_bar)
                self.input_biz()
            else:
                raise LoginError('登录页面title不符合规范,测试失败')
        else:
            self.open(settings.JOB_URL)
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

    def input_biz(self):
        if settings.ENVIRONMENT == False:
            # 选择业务
            self.click(xpath=login_page.job_app_select)
            self.type(xpath=login_page.app_search, text=settings.BIZ_NAME)
            time.sleep(3)
            self.click(xpath=login_page.app_search_select)
            time.sleep(5)

        if settings.ENVIRONMENT == True:
            # 选择业务
            self.click(xpath=login_page.job_app_select)
            self.type(xpath=login_page.app_search, text=settings.BIZ_NAME)
            time.sleep(3)
            self.click(xpath=login_page.app_search_select)
            time.sleep(5)

class Login(LoginBase):
    def test_login(self):
        self._test_login()