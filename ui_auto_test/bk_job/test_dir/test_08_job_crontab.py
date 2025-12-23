# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Description :
   date：          2024/10/29
-------------------------------------------------
"""
from public_method.login import LoginBase
from product_page.bk_job import home
from product_page.bk_job import crons
from product_page import settings
from product_page.public_components import ip_choose
from public_method.base_operate import BaseOperate
from product_page.bk_job import plandetail
BaseOperate = BaseOperate()


class ExcuteCrontab(LoginBase):
    '''定时任务'''
    def test_01_new_crontab(self):
        '''新建定时任务'''
        self.open(settings.JOB_URL)
        self.my_click(element=home.navigation_cronJob)
        self.my_click(element=crons.create_button)
        name = BaseOperate.random_data()
        settings.crons_create_name = name
        self.my_type(element=crons.crons_name, text=name)
        self.my_click(element=crons.run_once)
        self.my_click(element=crons.template_crons)
        self.my_click(element=plandetail.search_template)
        self.my_type(element=plandetail.search_template, text=settings.temp_input)
        self.sleep(1)
        self.Keys(xpath=plandetail.search_template['path']).enter()
        self.my_click(element=crons.plan_crons)
        self.my_type(element=plandetail.search_template, text=settings.plan_name)
        self.sleep(1)
        self.Keys(xpath=plandetail.search_template['path']).enter()
        self.my_click(element=crons.crons_submit)
        self.assertText("定时任务创建成功")

    def test_02_edit_crontab(self):
        '''编辑定时任务'''
        self.my_type(element=ip_choose.search, text=settings.crons_create_name)
        self.sleep(1)
        self.Keys(xpath=ip_choose.search['path']).enter()
        self.my_click(element=plandetail.last_modified_by)
        self.my_click(element=crons.edit_crons)
        self.my_click(element=crons.end_time_settings)
        self.my_click(element=crons.notify_to)
        self.my_click(element=crons.notify_to_personnel)
        self.my_click(element=crons.notify_by)
        self.my_click(element=crons.crons_save)
        self.assertText("定时任务编辑成功")

    def test_03_execrecord_crontab(self):
        '''定时任务执行记录 '''
        self.my_click(element=ip_choose.del_icon_search)
        self.my_type(element=ip_choose.search, text=settings.crons_create_name)
        self.sleep(1)
        self.Keys(xpath=ip_choose.search['path']).enter()
        self.my_click(element=ip_choose.search_total)
        self.my_click(element=crons.execrecord_crons)
        self.assertText("任务正常启动")
        self.my_click(element=home.sideslip_close)

    def test_04_start_crontab(self):
        '''开启定时任务'''
        self.my_click(element=home.navigation_cronJob)
        # self.my_type(element=ip_choose.search, text=settings.crons_create_name)
        # self.Keys(xpath=ip_choose.search['path']).enter()
        # self.my_click(element=ip_choose.search_total)
        self.my_click(element=crons.toggle_crontab_status)
        self.assertText("开启成功")
















