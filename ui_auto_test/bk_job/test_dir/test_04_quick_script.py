# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_04_quick_scripts.py
   Description :
   date：          2024/10/23
-------------------------------------------------
"""
from product_page.bk_job import home
from product_page.bk_job import quick_excute_scripts as quick_excute_page
from public_method.login import LoginBase
from public_method.base_operate import BaseOperate
from product_page import settings
from product_page.bk_job import navigation
from product_page.public_components import ip_choose
import seldom

BaseOperate = BaseOperate()

# 快速执行python脚本---不依赖IP变量
class QuickExecuteScripts(LoginBase):
    '''快速执行脚本'''
    def test_01_execute_python(self):
        '''快速执行python脚本'''
        # self._test_login(target_url=settings.JOB_URL, index_title=settings.INDEX_TITLE)
        self.switch_to_window(0)
        self.my_click(element=home.navigation_quick_script_excute)
        self.sleep(1)
        self.my_click(element=quick_excute_page.name_quick_script)
        self.Keys(xpath=quick_excute_page.name_quick_script['path']).select_all()
        self.Keys(xpath=quick_excute_page.name_quick_script['path']).backspace()
        name = BaseOperate.random_data()
        settings.NAME_QUICK = name
        # send = self.my_get_elements(element=quick_excute_page.name_quick_script)[0]
        # send.send_keys(Keys.CONTROL + 'a')
        # send.send_keys(Keys.DELETE)
        self.my_type(element=quick_excute_page.name_quick_script, text=name)
        self.my_click(element=navigation.python_click)
        self.my_type(element=navigation.script_content, text=navigation.PYTHON_SCRIPT_TEXT)
        # 滚动
        #self.my_drag_and_drop_by_offset(element=home.scroll_bar, x=0, y=200)
        self.quick_excute_public()
        self.assertText(navigation.RUN_STATE)

    def test_02_execute_shell(self):
        '''快速执行shell脚本'''
        self.open(settings.JOB_URL)
        self.my_click(element=home.navigation_quick_script_excute)
        self.sleep(1)
        self.my_click(element=quick_excute_page.name_quick_script)
        name = BaseOperate.random_data()
        settings.NAME_QUICK = name
        self.Keys(xpath=quick_excute_page.name_quick_script['path']).select_all()
        self.Keys(xpath=quick_excute_page.name_quick_script['path']).backspace()
        self.my_type(element=quick_excute_page.name_quick_script, text=name)
        self.my_type(element=navigation.script_content, text=navigation.SHELL_SCRIPT_TEXT)
        # 滚动
        #self.my_drag_and_drop_by_offset(element=home.scroll_bar, x=0, y=100)
        self.quick_excute_public()
        self.assertText(navigation.RUN_STATE)

    @seldom.skip_unless(settings.test_model == 'True', "全量用例，跑准入时跳过！")
    def test_03_python_timeout(self):
        '''快速执行python脚本超时'''
        self.open(settings.JOB_URL)
        self.my_click(element=home.navigation_quick_script_excute)
        self.sleep(1)
        self.my_click(element=quick_excute_page.name_quick_script)
        name = BaseOperate.random_data()
        settings.NAME_QUICK = name
        self.Keys(xpath=quick_excute_page.name_quick_script['path']).select_all()
        self.Keys(xpath=quick_excute_page.name_quick_script['path']).delete()
        self.my_type(element=quick_excute_page.name_quick_script, text=name)
        self.my_click(element=navigation.python_click)
        self.my_type(element=navigation.script_content, text=navigation.PYTHON_SCRIPT_IMPORT)
        self.sleep(1)
        self.Keys(xpath=navigation.script_content['path']).enter()
        self.my_type(element=navigation.script_content, text=navigation.PYTHON_SCRIPT_SLEEP)
        try:
            if self.my_get_elements(element=home.scroll_bar):
                self.my_drag_and_drop_by_offset(element=home.scroll_bar, x=0, y=200)
        except Exception as e:
            pass
        self.Keys(xpath=quick_excute_page.time_out['path']).backspace()
        self.Keys(xpath=quick_excute_page.time_out['path']).backspace()
        self.Keys(xpath=quick_excute_page.time_out['path']).backspace()
        self.quick_excute_public()
        self.assertText("task is timeout")

    @seldom.skip_unless(settings.test_model == 'True', "全量用例，跑准入时跳过！")
    def test_04_retry_python(self):
        '''执行失败python脚本重试'''
        self.sleep(1)
        self.my_click(element=quick_excute_page.retry_all)
        self.sleep(1)
        self.my_click(element=quick_excute_page.ok_button)
        self.sleep(10)
        self.assertText("task is timeout")

    @seldom.skip_unless(settings.test_model == 'True', "全量用例，跑准入时跳过！")
    def test_05_ignore_error_python(self):
        '''执行失败python忽略错误'''
        self.my_click(element=quick_excute_page.ignore_error)
        self.sleep(1)
        self.my_click(element=quick_excute_page.ok_button)
        self.sleep(10)
        self.assertText("忽略错误")
        self.my_click(element=home.navigation_histories)
        self.my_click(element=home.search)
        self.my_click(element=home.search_name)
        self.my_type(element=home.search, text=settings.NAME_QUICK)
        self.sleep(1)
        self.Keys(xpath=home.search['path']).enter()
        self.assertText("执行成功")


    @seldom.skip_unless(settings.test_model == 'True', "全量用例，跑准入时跳过！")
    def test_06_execute_shell(self):
        '''快速执行shell脚本超时'''
        self.open(settings.JOB_URL)
        self.my_click(element=home.navigation_quick_script_excute)
        self.sleep(1)
        self.my_click(element=quick_excute_page.name_quick_script)
        name = BaseOperate.random_data()
        settings.NAME_QUICK = name
        self.Keys(xpath=quick_excute_page.name_quick_script['path']).select_all()
        self.Keys(xpath=quick_excute_page.name_quick_script['path']).delete()
        self.my_type(element=quick_excute_page.name_quick_script, text=name)
        self.my_type(element=navigation.script_content, text=navigation.SHELL_SCRIPT_TEXT)
        self.sleep(1)
        self.Keys(xpath=navigation.script_content['path']).enter()
        self.my_type(element=navigation.script_content, text=navigation.SHELL_SCRIPT_SLEEP)
        try:
            if self.my_get_elements(element=home.scroll_bar):
                self.my_drag_and_drop_by_offset(element=home.scroll_bar, x=0, y=200)
        except Exception as e:
            pass
        self.Keys(xpath=quick_excute_page.time_out['path']).backspace()
        self.Keys(xpath=quick_excute_page.time_out['path']).backspace()
        self.Keys(xpath=quick_excute_page.time_out['path']).backspace()
        self.quick_excute_public()
        self.assertText("task is timeout")

    @seldom.skip_unless(settings.test_model == 'True', "全量用例，跑准入时跳过！")
    def test_07_relaunch_shell(self):
        '''执行失败shell脚本重做'''
        self.sleep(1)
        self.my_click(element=quick_excute_page.relaunch)
        try:
            if self.my_get_elements(element=home.scroll_bar):
                self.my_drag_and_drop_by_offset(element=home.scroll_bar, x=0, y=200)
        except Exception as e:
            pass
        self.my_type(element=quick_excute_page.time_out, text=0)
        self.my_click(element=quick_excute_page.button_excute_script)
        self.sleep(5)
        self.assertText(navigation.RUN_STATE)


    def quick_excute_public(self):
        try:
            if self.my_get_elements(element=home.scroll_bar):
                self.my_drag_and_drop_by_offset(element=home.scroll_bar, x=0, y=200)
        except Exception as e:
            pass
        #self.my_click(element=quick_excute_page.select_account)
        #self.my_click(element=quick_excute_page.select_root)
        # 选择服务器
        self.my_click(element=quick_excute_page.choose_hosts)
        # self.type(xpath=page.host_search, text=page.host_search_input)
        self.my_click(element=ip_choose.choose_agent)
        self.my_click(element=ip_choose.choose_host_confirm)
        # print("服务器IP为:  " + self.get_text(xpath=page.first_agent_ip))
        self.my_click(element=quick_excute_page.button_excute_script)
        self.sleep(5)

