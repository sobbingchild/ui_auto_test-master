# -*- coding: utf-8 -*-
# @Time : 2024/8/3 14:36
# @File : test_03_create_python_script.py
# @Project : bk_job
import seldom
from public_method.login import LoginBase
from product_page.bk_job import home
from product_page.bk_job import navigation
from product_page import settings
from product_page.public_components import ip_choose
from product_page.bk_job import quick_excute_scripts
from public_method.base_operate import BaseOperate
from ..page.job_public_method import JobMethod

BaseOperate = BaseOperate()


# 创建python脚本--无IP依赖
class CreateScript(JobMethod):
    '''python脚本创建、上线'''
    def test_01_createScript(self):
        '''创建python脚本'''
        self._test_login(target_url=settings.JOB_URL, index_title=settings.INDEX_TITLE)
        self.max_window()
        # 登录态验证
        self.switch_to_window(0)
        self.my_click(element=home.navigation_scriptManage)
        self.assertText(navigation.HTML_TITLE)
        self.sleep(2)
        # 点击新建脚本
        try:
            if self.my_get_text(element=navigation.scriptPage_title, index=1) == '当前业务暂无脚本，请先创建':
                self.my_click(element=navigation.scriptPage_button)
        except Exception:
            self.my_click(element=navigation.append_button)
        self.wait(5)
        name = BaseOperate.random_data()
        settings.python_script_name = name
        # 输入脚本名称,描述,版本,脚本内容
        self.my_type(element=navigation.input_script_name, text=name)
        self.my_type(element=navigation.script_description, text=name)
        self.my_type(element=navigation.script_version, index=1, text=navigation.SCRIPT_VERSION)
        self.CreateScript(Script_Type='python',Script_Usage_Scope='business')
        # 此处输入"python"执行python脚本创建,目前支持python/perl/powershell
        # 此处输入'business'执行业务脚本相关创建

    @seldom.skip_unless(settings.test_model == 'True', "全量用例，跑准入时跳过！")
    def test_02_debugScript(self):
        '''调试脚本'''
        # 断言是否跳转到版本管理
        self.assertText(navigation.PAGE_TEXT)
        # 点击调试脚本
        self.my_click(element=navigation.debug_button)
        self.wait(5)
        self.switch_to_window(1)
        self.AssertScriptText(Script_Type='python')
        # 此处输入"python"执行python脚本创建,目前支持python/perl/powershell

        self.ScriptDebug(self)


    def test_03_onlineScript(self):
        '''上线脚本'''
        self.switch_to_window(0)
        # 断言是否跳转到版本管理
        self.assertText(navigation.PAGE_TEXT)
        # 断言是否进入python脚本管理页
        self.AssertScriptOnline(Script_Type='python')
        # 此处输入"python"执行python脚本创建,目前支持python/perl/powershell