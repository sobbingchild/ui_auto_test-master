# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Description :
   date：          2024/10/25
-------------------------------------------------
"""
from public_method.login import LoginBase
from product_page.bk_job import home
from product_page.bk_job import navigation
from product_page.bk_job import operation
from product_page.bk_job import account
from product_page import settings
from product_page.public_components import ip_choose
from public_method.base_operate import BaseOperate
from product_page.bk_job import plandetail
BaseOperate = BaseOperate()

class delData(LoginBase):
    '''删除操作'''
    def test_01_delscript(self):
        ''' 删除脚本'''
        # 进入 资源-脚本 页面
        self.my_click(element=home.navigation_scriptManage)
        self.assertText(navigation.HTML_TITLE)
        self.del_script(settings.script_name, navigation.del_button)
        self.assertText("删除成功")
        self.my_click(element=ip_choose.del_icon_search)
        self.del_script(settings.python_script_name, navigation.del_button)
        self.assertText("删除成功")

    def test_02_del_crontab(self):
        '''删除定时任务'''
        self.my_click(element=home.navigation_cronJob)
        self.del_script(settings.crons_name, navigation.del_button)
        self.assertText("删除定时任务成功")
        self.open(settings.JOB_URL)
        self.my_click(element=home.navigation_cronJob)
        self.del_script(settings.crons_create_name, navigation.del_button)
        self.assertText("删除定时任务成功")

    def test_03_del_plan(self):
        '''删除执行方案'''
        self.open(settings.JOB_URL)
        self.my_click(element=home.navigation_planManage)
        self.del_script(settings.temp_input, plandetail.button_deletePlan, True)
        self.assertText("操作成功")
        self.my_click(element=ip_choose.del_icon_search)
        self.del_script(settings.plan_name, plandetail.button_deletePlan, True)
        self.assertText("操作成功")

    def test_04_del_temp(self):
        '''删除作业'''
        self.open(settings.JOB_URL)
        self.my_click(element=home.jobs)
        self.del_script(settings.temp_input, operation.del_temp, True)
        self.assertText("删除模板成功")

    def test_05_del_linux_account(self):
        '''删除Linux账号'''
        self.open(settings.JOB_URL)
        self.my_click(element=home.navigation_account)
        self.sleep(2)
        self.del_script(settings.account_linux_name, account.del_account)
        self.assertText("删除成功")

    def test_06_del_windows_account(self):
        '''删除windows账号'''
        self.open(settings.JOB_URL)
        self.my_click(element=home.navigation_account)
        self.sleep(2)
        self.del_script(settings.account_windows_name, account.del_account)
        self.assertText("删除成功")

    def test_07_del_mysql_account(self):
        '''删除mysql账号'''
        self.open(settings.JOB_URL)
        self.my_click(element=home.navigation_account)
        self.sleep(2)
        self.del_script(settings.account_mysql_name, account.del_account)
        self.assertText("删除成功")

    def del_script(self, name, xpath, more=False):
        self.sleep(1)
        self.my_type(element=ip_choose.search, text=name)
        self.sleep(1)
        self.Keys(xpath=ip_choose.search['path']).enter()
        self.sleep(1)
        self.my_click(element=ip_choose.search_total)
        if more == True:
            self.my_click(element=operation.temp_more)
        self.my_click(element=xpath)
        self.my_click(element=operation.confirm_button)

