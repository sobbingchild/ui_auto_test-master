# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_04_quick_scripts.py
   Description :
   date：          2024/11/11
-------------------------------------------------
"""
from product_page.bk_job import home
from product_page.bk_job import quick_excute_scripts
from public_method.login import LoginBase
from public_method.base_operate import BaseOperate
from product_page import settings
from product_page.bk_job import crons
from product_page.bk_job import navigation
from product_page.public_components import ip_choose

BaseOperate = BaseOperate()

class QuickFileScripts(LoginBase):
    '''分发文件'''
    def test_01_remote_file(self):
        """服务器文件分发"""
        self.open(settings.JOB_URL)
        #self.my_click(element=home.navigation_close)
        self.my_click(element=home.navigation_quick_file_excute)
        self.Keys(xpath=quick_excute_scripts.name_quick_script['path']).select_all()
        self.Keys(xpath=quick_excute_scripts.name_quick_script['path']).delete()
        name = BaseOperate.random_data()
        settings.quickfile = name
        self.my_type(element=quick_excute_scripts.name_quick_script, text=name)
        self.my_click(element=quick_excute_scripts.name_quick_file)
        #self.my_click(element=quick_excute_scripts.input_file_path)
        self.my_type(element=quick_excute_scripts.input_file_path, text="/tmp/*.log")
        self.my_click(element=quick_excute_scripts.add_file_host)
        self.my_click(element=ip_choose.choose_two_agent)
        self.my_click(element=ip_choose.choose_host_confirm)
        self.my_click(element=crons.crons_save)
        self.my_type(element=quick_excute_scripts.input_outgiving_path, text="/tmp/")
        try:
            if self.my_get_elements(element=home.scroll_bar):
                self.my_drag_and_drop_by_offset(element=home.scroll_bar, x=0, y=200)
        except Exception as e:
            pass
        self.my_click(element=quick_excute_scripts.choose_hosts)
        self.sleep(1)
        self.assertText(navigation.PAGE_AGENT_STATE)
        self.my_click(element=quick_excute_scripts.choose_agent)
        self.my_click(element=quick_excute_scripts.choose_host_confirm)
        self.my_click(element=quick_excute_scripts.button_excute_file)
        self.sleep(20)
        self.assertText("执行成功")