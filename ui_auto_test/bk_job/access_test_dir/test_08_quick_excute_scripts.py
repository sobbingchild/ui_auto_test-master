# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_02_quick_excute_scripts.py
   Description : 
   Author :       v_adanchen
   date：          2021/7/23
-------------------------------------------------
"""
from bk_job.page import quick_excute_scripts as page
from bk_job import settings
from bk_job.test_dir.test_01_login import LoginBase
import time

# 快速执行shell脚本--不依赖IP
class QuickExecuteScripts(LoginBase):
    def test_01_execute_shell(self):
        '''快速执行shell脚本'''
        # 验证登录
        self._test_login()
        self.click(xpath=page.navigation_quick_script_excute)
        self.click(xpath=page.name_quick_script)
        time.sleep(1)
        self.type(xpath=page.name_quick_script, text=settings.TEST_UI_NAME_QUICK)
        self.type(xpath=page.input_script_content, text=settings.TEST_UI_SHELL_CONTENT)
        time.sleep(1)
        self.click(xpath=page.select_account)
        self.click(xpath=page.select_root)
        time.sleep(2)
        #滚动
        self.drag_and_drop_by_offset(xpath=page.scroll_bar, x=0, y=100)
        #选择服务器
        self.click(xpath=page.execute_target)
        self.type(xpath=page.host_search,text=page.host_search_input)
        time.sleep(3)
        self.click(xpath=page.select_first_agent)
        print("服务器IP为:  " + self.get_text(xpath=page.first_agent_ip))
        self.click(xpath=page.confirm_agent)
        self.click(xpath=page.button_excute_script)
        time.sleep(10)
        if self.get_text(xpath=page.status_excute) == page.excute_suss:
            print(page.excute_suss)
        elif self.get_text(xpath=page.status_excute) == page.excute_fail:
            print(page.excute_fail)
        else:
            print(page.excute_exception)

