# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_01_aply_perm.py
   Description : 完整的申请权限的流程
   Author :       v_adanchen
   date：          2022/4/8
-------------------------------------------------
"""
import seldom
import bk_iam.page.ord_member as page
import time
import bk_iam.settings as settings


class AplyPerm(seldom.TestCase):
    def test_01_aply_perm(self):
        '''申请开发者中心权限'''
        self.click(xpath=page.perm_ply)
        self.click(xpath=page.custom_perm)
        self.click(xpath=page.dev_center_perm)
        self.type(xpath=page.resean_type, text=page.resean_text)
        time.sleep(1)
        self.click(xpath=page.commit_ply)
        time.sleep(2)


    def test_02_login_out_iam(self):
        '''退出iam'''
        self.click(xpath=page.nav_appro)
        self.wait(2)
        # self.Keys.tab()
        new_windows = self.window_handles[1]
        print("新窗口----", new_windows)
        self.switch_to_window(new_windows)
        self.click(xpath=page.itsm_name)
        self.click(xpath=page.loginout_itsm)
        self.wait(3)

    def test_03_login_itsm(self):
        '''登录itsm'''
        self.login(settings.USER_NAME, settings.PASSWORD)

    def test_04_deal_appro(self):
        '''处理审批单据-已通过'''
        self.click(xpath=page.itsm_appro_pass)
        self.wait(1)
        self.click(xpath=page.itsm_appro_confrim, index=1)
        time.sleep(3)
        new_windows = self.window_handles[0]
        print("新窗口----", new_windows)
        self.switch_to_window(new_windows)

    def test_05_assert_perm(self):
        """
        1.先切换到权限中心的窗口
        2.点击导航栏我的权限
        3.右上角切换账号，登录申请权限的这个用户
        4.点击 我的权限-自定义申请权限
        5.检查是否有paas平台的权限
        :return:
        """
        new_windows = self.window_handles[0]
        print("新窗口----", new_windows)
        self.switch_to_window(new_windows)
        self.click(xpath=page.nav_myperm)
        time.sleep(3)
        self.click(xpath=page.iam_name)
        self.click(xpath=page.iam_login_out)
        time.sleep(3)
        self.login(settings.NEW_USER, settings.NEW_PWD)
        self.click(xpath=page.custom_review)
        time.sleep(2)
        self.assertText(page.PaaS)

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



