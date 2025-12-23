# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_15_ip_select.py
   Description : 
   Author :       v_adanchen
   date：          2021/9/6
-------------------------------------------------
"""
from bk_job import settings
from bk_job.test_dir.test_01_login import LoginBase
from bk_job.page import quick_excute_scripts as page
from pre_data.job_api_demo import JobApi
from bk_job.bk_exception import ApiError
import time

api = JobApi()

# test_3 依赖IP
class IpList(LoginBase):
    def test_01_static_ip(self):
        '''静态IP选择执行脚本'''
        # 验证登录
        self._test_login()
        self.click(xpath=page.navigation_quick_script_excute)
        self.click(xpath=page.name_quick_script)
        time.sleep(1)
        self.type(xpath=page.name_quick_script, text=settings.TEST_UI_NAME_QUICK)
        self.type(xpath=page.input_script_content, text=settings.TEST_UI_SHELL_CONTENT)
        # 拖动滚动条，显示页面元素
        self.drag_and_drop_by_offset(xpath=page.scroll_bar, x=0, y=200)
        time.sleep(1)
        self.click(xpath=page.select_account)
        self.click(xpath=page.select_root)
        time.sleep(1)
        self.click(xpath=page.button_add_ip)
        self.click(xpath=page.checkbox_choose_ip)
        self.click(xpath=page.button_confirm_ip)
        self.click(xpath=page.button_excute_script)
        time.sleep(2)
        if self.get_text(xpath=page.status_excute) == page.excute_suss:
            print(page.excute_suss)
        elif self.get_text(xpath=page.status_excute) == page.excute_fail:
            print(page.excute_fail)
        else:
            print(page.excute_exception)


    def test_02_dynamic_topo(self):
        '''动态拓扑选择执行脚本'''
        self.click(xpath=page.navigation_quick_script_excute)
        self.click(xpath=page.name_quick_script)
        time.sleep(1)
        self.type(xpath=page.name_quick_script, text=settings.TEST_UI_NAME_QUICK)
        self.type(xpath=page.input_script_content, text=settings.TEST_UI_SHELL_CONTENT)
        # 拖动滚动条，显示页面元素
        self.drag_and_drop_by_offset(xpath=page.scroll_bar, x=0, y=200)
        time.sleep(1)
        self.click(xpath=page.select_account)
        self.click(xpath=page.select_root)
        time.sleep(2)
        self.click(xpath=page.button_add_ip)
        self.click(xpath=page.button_dynamic_top)
        self.click(xpath=page.select_bussiss)
        self.click(xpath=page.confirm_ip_dy)
        self.click(xpath=page.button_excute_script)
        time.sleep(2)
        if self.get_text(xpath=page.status_excute) == page.excute_suss:
            print(page.excute_suss)
        elif self.get_text(xpath=page.status_excute) == page.excute_fail:
            print(page.excute_fail)
        else:
            print(page.excute_exception)

    def test_03_manual_input(self):
        '''手动输入IP选择执行脚本'''
        self.click(xpath=page.navigation_quick_script_excute)
        self.click(xpath=page.name_quick_script)
        time.sleep(1)
        self.type(xpath=page.name_quick_script, text=settings.TEST_UI_NAME_QUICK)
        self.type(xpath=page.input_script_content, text=settings.TEST_UI_SHELL_CONTENT)
        # 拖动滚动条，显示页面元素
        self.drag_and_drop_by_offset(xpath=page.scroll_bar, x=0, y=200)
        time.sleep(1)
        self.click(xpath=page.select_account)
        self.click(xpath=page.select_root)
        time.sleep(2)
        self.click(xpath=page.button_add_ip)
        self.click(xpath=page.button_manmul_input)
        # 发起APi请求获取当前环境蓝鲸业务下的linux_ip列表
        ip_list = api.get_hosts_ip()
        if ip_list:
            self.type(xpath=page.input_ip, text=ip_list[0])
        else:
            raise ApiError("API请求错误")
        self.click(xpath=page.add_ip)
        time.sleep(1)
        self.click(xpath=page.confirm_ip_input)
        self.click(xpath=page.button_excute_script)
        time.sleep(2)
        if self.get_text(xpath=page.status_excute) == page.excute_suss:
            print(page.excute_suss)
        elif self.get_text(xpath=page.status_excute) == page.excute_fail:
            print(page.excute_fail)
        else:
            print(page.excute_exception)