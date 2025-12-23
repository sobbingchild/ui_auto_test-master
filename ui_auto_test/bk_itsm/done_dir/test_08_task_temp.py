# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_05_task_temp.py
   Description : 
   Author :       v_adanchen
   date：          2021/10/25
-------------------------------------------------
"""
import seldom
import bk_itsm.page.tash_temp as page
import bk_itsm.settings as settings


# 已完成
class TaskTemp(seldom.TestCase):

    def test_01_new_task_temp(self):
        """"添加任务模板"""
        self.click(xpath=page.platform_man)
        self.click(xpath=page.nav_task_temp)
        self.click(xpath=page.add_task_temp)
        self.type(xpath=page.temp_name, text=settings.TEST_TICKETS_TASK_NAME)
        self.click(xpath=page.into_setings)
        self.click(xpath=page.task_temp_next)
        self.click(xpath=page.task_temp_next)
        self.click(xpath=page.task_complet)

    def test_02_search_temp(self):
        """"搜索任务模板"""
        self.click(xpath=page.search)
        self.type_enter(xpath=page.search, text=settings.TEST_TICKETS_TASK_NAME)
        assert self.get_text(xpath=page.search_text) == settings.TEST_TICKETS_TASK_NAME
