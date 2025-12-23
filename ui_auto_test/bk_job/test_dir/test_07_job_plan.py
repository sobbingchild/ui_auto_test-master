# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Description :
   date：          2024/10/23
-------------------------------------------------
"""
from public_method.login import LoginBase
from product_page.bk_job import home
from product_page.bk_job import operation
from product_page.bk_job import crons
from product_page import settings
from product_page.public_components import ip_choose
from public_method.base_operate import BaseOperate
from product_page.bk_job import plandetail
BaseOperate = BaseOperate()


class ExcutePlan(LoginBase):
    '''执行方案'''
    def test_01_new_plan(self):
        '''新建执行方案'''
        self.open(settings.JOB_URL)
        self.my_click(element=home.navigation_planManage)
        self.my_click(element=plandetail.mine)
        self.my_click(element=plandetail.plan_create)
        self.my_click(element=plandetail.select_template)
        self.my_type(element=plandetail.search_template, text=settings.temp_input)
        self.sleep(1)
        self.Keys(xpath=plandetail.search_template['path']).enter()
        self.my_click(element=plandetail.select_template_submit)
        self.assertText('我的方案')
        self.my_click(element=plandetail.plan_create_name)
        name = BaseOperate.random_data()
        settings.plan_name = name
        self.Keys(xpath=plandetail.plan_create_name['path']).select_all()
        self.Keys(xpath=plandetail.plan_create_name['path']).delete()
        self.my_type(element=plandetail.plan_create_name, text=name)
        self.my_click(element=plandetail.plan_create_submit)
        self.assertText('操作成功')

    def test_02_excute_plan(self):
        '''执行执行方案'''
        self.my_click(element=plandetail.to_execplan)
        self.my_click(element=plandetail.lanunch_button)
        self.sleep(4)
        self.assertText('等待确认')

    def test_03_edit_plan(self):
        '''编辑执行方案'''
        self.open(settings.JOB_URL)
        self.my_click(element=home.navigation_planManage)
        self.my_click(element=plandetail.mine)
        self.my_type(element=ip_choose.search, text=settings.plan_name)
        self.sleep(1)
        self.Keys(xpath=ip_choose.search['path']).enter()
        self.my_click(element=plandetail.last_modified_by)
        self.my_click(element=operation.temp_more)
        self.my_click(element=plandetail.button_editPlan)
        self.my_click(element=plandetail.editPlan_task)
        self.my_click(element=plandetail.button_editPlanSave)
        self.assertText('(1/2)')

    def test_04_createCrontab(self):
        '''执行方案》定时执行'''
        self.open(settings.JOB_URL)
        self.my_click(element=home.navigation_planManage)
        self.my_click(element=plandetail.mine)
        self.my_type(element=ip_choose.search, text=settings.plan_name)
        self.sleep(1)
        self.Keys(xpath=ip_choose.search['path']).enter()
        self.my_click(element=plandetail.last_modified_by)
        self.my_click(element=operation.temp_more)
        self.my_click(element=plandetail.link_createCrontab)
        self.sleep(1)
        self.switch_to_window(1)
        name = BaseOperate.random_data()
        settings.crons_name = name
        self.my_type(element=crons.crons_name, text=name)
        self.my_click(element=crons.time_input)
        self.Keys(xpath=crons.time_input['path']).select_all()
        self.Keys(xpath=crons.time_input['path']).delete()
        self.my_type(element=crons.time_input, text="00 1 * 1 1")
        self.my_click(element=crons.crons_submit)
        self.assertText("定时任务创建成功")

