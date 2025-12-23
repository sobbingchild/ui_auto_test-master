# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_16_dangerous_rule_manage.py
   Description :
   Author :       v_jingdhe
   date：          2021/9/14
-------------------------------------------------
"""

from bk_job.test_dir.test_01_login import LoginBase
from bk_job.page import public_ScriptList
import time

class DangerousRules(LoginBase):
    def test_01_new_rules(self):
        '''进入高危语句规则页面'''
        # 验证登录
        self._test_login()
        #跳转至平台管理
        self.click(xpath=public_ScriptList.navigation_publicScriptList)
        #跳转至高危语句规则
        self.click(xpath=public_ScriptList.navigation_dangerousRuleManage)
    def test_02_create_rules(self):
        '''新增高危语句规则'''
        self.click(xpath=public_ScriptList.new_dangerousRuleManage)
        time.sleep(2)
        self.type(xpath=public_ScriptList.Syntax_expression,text="nihao")
        self.type(xpath=public_ScriptList.Rules_specification,text="testtext")
        self.click(xpath=public_ScriptList.Script_type)
        self.click(xpath=public_ScriptList.Type_all)
        time.sleep(2)
        self.click(xpath=public_ScriptList.Rules_action)
        self.click(xpath=public_ScriptList.Action_scan)
        self.click(xpath=public_ScriptList.Rules_save)
        time.sleep(2)
    def test_03_assert_rules(self):
        '''断言是否新增成功'''
        #断言是否新建成功
        Syntax_expression_name = "nihao"
        if self.get_text(xpath=public_ScriptList.Syntax_expression_text) == Syntax_expression_name:
            print("新建成功")
        else:
            print("新建失败")
        time.sleep(2)
    def test_04_delete_rules(self):
        '''删除规则'''
        self.click(xpath=public_ScriptList.Rules_delete)
        self.click(xpath=public_ScriptList.Delete_confirm)
        print("删除成功")


