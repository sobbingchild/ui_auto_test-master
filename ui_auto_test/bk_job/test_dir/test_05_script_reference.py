# -*- coding: utf-8 -*-
# @Time : 2024/8/4 17:17
# @File : test_04_script_reference.py
# @Project : bk_job
import seldom
from product_page import settings
from public_method.login import LoginBase
from product_page.bk_job import home
from public_method.base_operate import BaseOperate
from product_page.bk_job import quick_excute_scripts as quick_excute_page
from product_page.public_components import ip_choose
from product_page.bk_job import navigation

BaseOperate = BaseOperate()

class ScriptReference(LoginBase):
    '''快速执行脚本》引用脚本'''
    @seldom.skip_unless(settings.test_model == 'True', "全量用例，跑准入时跳过！")
    def test_01_shellReference(self):
        '''引用shell脚本'''
        self.open(settings.JOB_URL)
        self.scriptReference(settings.script_name)
        print('shell脚本引用成功')

    @seldom.skip_unless(settings.test_model == 'True', "全量用例，跑准入时跳过！")
    def test_02_pythonReference(self):
        '''引用python脚本'''
        self.open(settings.JOB_URL)
        self.scriptReference(settings.python_script_name)
        print('python脚本引用成功')

    def scriptReference(self, script_name):
        self.my_click(element=home.navigation_quick_script_excute)
        self.my_click(element=quick_excute_page.name_quick_script)
        name = BaseOperate.random_data()
        settings.NAME_QUICK = name
        self.Keys(xpath=quick_excute_page.name_quick_script['path']).select_all()
        self.Keys(xpath=quick_excute_page.name_quick_script['path']).backspace()
        self.my_type(element=quick_excute_page.name_quick_script, text=name)
        # 切换脚本来源为脚本引用
        self.my_click(element=quick_excute_page.script_reference)
        # 断言页面跳转为脚本引用
        self.assertText('脚本引用')
        # 点击脚本引用
        self.my_click(element=quick_excute_page.script_select)
        # 选择脚本
        self.my_click(element=quick_excute_page.choice_script(script_name))
        self.sleep(1)
        # 拖动滚动条，显示页面元素
        try:
            if self.my_get_elements(element=home.scroll_bar):
                self.my_drag_and_drop_by_offset(element=home.scroll_bar, x=0, y=200)
        except Exception as e:
            pass
        self.my_click(element=quick_excute_page.select_account)
        self.my_click(element=quick_excute_page.select_root)
        self.my_click(element=quick_excute_page.choose_hosts)
        self.my_click(element=ip_choose.choose_agent)
        self.my_click(element=ip_choose.choose_host_confirm)
        self.my_click(element=quick_excute_page.button_excute_script)
        self.sleep(5)
        self.assertText(navigation.RUN_STATE)
