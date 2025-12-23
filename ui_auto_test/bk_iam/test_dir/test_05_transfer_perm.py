# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_05_transfer_perm.py
   Description : 
   Author :       v_adanchen
   date：          2022/5/26
-------------------------------------------------
"""
import seldom
import time
from bk_iam import settings as settings
from bk_iam.page import transfer_perm as page


class TransferPerm(seldom.TestCase):
    def test_01_swich_nomal_user(self):
        '''切换回普通用户'''
        new_windows = self.window_handles[0]
        print("新窗口----", new_windows)
        self.switch_to_window(new_windows)
        self.click(xpath=page.iam_name)
        self.click(xpath=page.iam_login_out)
        time.sleep(2)
        self.login(settings.NEW_USER, settings.NEW_PWD)

    def test_02_transfer_userg_perm(self):
        '''非admin用户组权限交接'''
        self.click(xpath=page.nav_myperm)
        self.click(xpath=page.transfer_perm)
        self.click(xpath=page.checkbox_user_g)
        self.click(xpath=page.transfer)
        self.type(xpath=page.transfer_span, text=settings.B_USER)
        time.sleep(2)
        self.Keys(xpath=page.transfer_span).enter()
        self.type(xpath=page.transfer_reason, text=page.resean_text)
        self.click(xpath=page.commit_transfer)

    def test_03_custom_perm(self):
        '''非admin自定义权限交接'''
        self.click(xpath=page.nav_myperm)
        self.click(xpath=page.transfer_perm)
        self.click(xpath=page.paas_custom_perm)
        time.sleep(1)
        self.click(xpath=page.paas_dev_perm)
        self.click(xpath=page.transfer)
        self.type(xpath=page.transfer_span, text=settings.B_USER)
        time.sleep(2)
        self.Keys(xpath=page.transfer_span).enter()
        self.click(xpath=page.transfer_reason)
        self.type(xpath=page.transfer_reason, text=page.resean_text)
        self.click(xpath=page.commit_transfer)

        '''

            分级管理员没有使用新建的方式，所以交接的时候，也没有用户交接，暂时注释掉
    def test_04_transfer_rating_man(self):
        #admin交接分级管理员
        self.click(xpath=page.nav_myperm)
        self.click(xpath=page.transfer_perm)
        self.click(xpath=page.click_userg_icon)
        self.click(xpath=page.click_custom_icon)
        self.click(xpath=page.check_rating_man)
        self.click(xpath=page.transfer)
        self.type(xpath=page.transfer_span, text=settings.B_USER)
        time.sleep(2)
        self.Keys(xpath=page.transfer_span).enter()
        self.click(xpath=page.transfer_reason)
        self.type(xpath=page.transfer_reason, text=page.resean_text)
        self.click(xpath=page.commit_transfer)

        # 滚动
        # self.drag_and_drop_by_offset(xpath=page.scroll_bar, x=0, y=100)
        '''

    # def test_04_transfer_sys_man(self):
    #     '''交接系统管理员'''
    #     self.click(xpath=page.nav_myperm)
    #     self.click(xpath=page.transfer_perm)
    #     # self.click(xpath=page.click_userg_icon)
    #     # self.click(xpath=page.click_custom_icon)
    #     self.click(xpath=page.check_sys_man)
    #     self.click(xpath=page.transfer)
    #     self.type(xpath=page.transfer_span, text=settings.B_USER)
    #     time.sleep(2)
    #     self.Keys(xpath=page.transfer_span).enter()

    #     self.click(xpath=page.transfer_reason)
    #     self.type(xpath=page.transfer_reason, text=page.resean_text)
    #     self.click(xpath=page.commit_transfer)

    # def test_05_check_perm(self):
    #     '''检查权限交接完成状态'''
    #     no_perm = self.get_text(xpath=page.no_perm)
    #     self.assertText(no_perm)

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
