# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Description :
   date：          2024/10/29
-------------------------------------------------
"""
from public_method.login import LoginBase
from product_page.bk_job import home
from product_page.bk_job import account
from product_page import settings
from product_page.public_components import ip_choose
from public_method.base_operate import BaseOperate
from product_page.bk_job import plandetail
BaseOperate = BaseOperate()


class ExcuteAccount(LoginBase):
    '''账号'''
    def test_01_create_linux_account(self):
        '''新建linux系统账号'''
        self.open(settings.JOB_URL)
        self.my_click(element=home.navigation_account)
        self.sleep(2)
        self.my_click(element=account.create_account)
        name = BaseOperate.random_data().lower()
        settings.account_linux_name = name
        self.my_type(element=account.account_name, text=name)
        self.my_type(element=account.account_alias, text=name)
        self.my_type(element=account.account_descriptions, text=name)
        self.my_click(element=account.account_submit)
        self.assertText("新建账号成功")

    def test_02_create_windows_account(self):
        '''新建windows系统账号'''
        self.my_click(element=home.navigation_account)
        self.my_click(element=account.create_account)
        name = BaseOperate.random_data()
        settings.account_windows_name = name
        self.my_click(element=account.type_account)
        self.my_type(element=account.account_windows_name, text=name)
        self.my_type(element=account.account_alias, text=name)
        self.my_type(element=account.account_passw, text=name)
        self.my_type(element=account.account_passw_confirm, text=name)
        self.my_type(element=account.account_descriptions, text=name)
        self.my_click(element=account.account_submit)
        self.assertText("新建账号成功")

    def test_03_create_mysql_account(self):
        '''新建mysql系统账号'''
        self.my_click(element=home.navigation_account)
        self.my_click(element=account.create_account)
        name = BaseOperate.random_data()
        settings.account_mysql_name = name
        self.my_click(element=account.usage_account)
        self.my_type(element=account.account_mysql_name, text=name)
        self.my_type(element=account.account_alias, text=name)
        self.my_type(element=account.account_passw, text=name)
        self.my_type(element=account.account_passw_confirm, text=name)
        self.my_type(element=account.account_port, text="abc")
        a = self.my_get_text(element=account.account_port)
        self.assertTrue(a == '')
        self.my_type(element=account.account_port, text=22)
        self.my_type(element=account.account_descriptions, text=name)
        self.my_click(element=account.account_submit)
        self.assertText("新建账号成功")