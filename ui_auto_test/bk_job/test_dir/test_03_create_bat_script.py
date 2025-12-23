# -*- coding: utf-8 -*-
# @Time : 2024/8/3 14:36
# @File : test_03_create_bat_script.py
# @Project : bk_job
import seldom
from public_method.login import LoginBase
from product_page.bk_job import home
from product_page.bk_job import navigation
from product_page import settings
from product_page.public_components import ip_choose
from product_page.bk_job import quick_excute_scripts
from public_method.base_operate import BaseOperate
BaseOperate = BaseOperate()


# 创建bat脚本--无IP依赖
class CreateBatScript(LoginBase):
    '''Bat脚本创建、上线'''
    def test_01_createBat(self):
        '''创建Bat脚本'''
        # self._test_login(target_url=settings.JOB_URL, index_title=settings.INDEX_TITLE)
        # self.max_window()
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
        settings.bat_script_name = name
        # 输入脚本名称,描述,版本,脚本内容
        self.my_type(element=navigation.input_script_name, text=name)
        self.my_type(element=navigation.script_description, text=name)
        self.my_type(element=navigation.script_version, index=1, text=navigation.SCRIPT_VERSION)
        # 选择bat
        self.my_click(element=navigation.bat_click)
        self.my_type(element=navigation.script_content, text=navigation.BAT_SCRIPT_TEXT)


        # 点击提交
        self.my_click(element=navigation.submit_button)
        # 断言是否跳转到版本管理
        self.assertText(navigation.PAGE_TEXT)
        # 断言新建脚本状态
        self.assertText("未上线")

    @seldom.skip_unless(settings.test_model == 'True', "全量用例，跑准入时跳过！")
    def test_02_debugBat(self):
        '''调试脚本'''
        # 断言是否跳转到版本管理
        self.assertText(navigation.PAGE_TEXT)
        # 点击调试脚本
        self.my_click(element=navigation.debug_button)
        self.wait(5)
        self.switch_to_window(1)
        self.assertText(navigation.BAT_SCRIPT_TEXT)
        try:
            if self.my_get_elements(element=home.scroll_bar):
                self.my_drag_and_drop_by_offset(element=home.scroll_bar, x=0, y=200)
        except Exception as e:
            pass
        self.my_click(element=quick_excute_scripts.choose_hosts)
        self.assertText(navigation.PAGE_AGENT_STATE)
        self.my_click(element=ip_choose.choose_agent)
        self.my_click(element=ip_choose.choose_host_confirm)
        self.my_click(element=navigation.debug_run)
        self.sleep(3)
        self.assertText(navigation.RUN_STATE)
        # 关闭跳转的选项卡
        print('调试成功')

    def test_03_onlineShell(self):
        '''上线脚本'''
        self.switch_to_window(0)
        # 断言是否跳转到版本管理
        self.assertText(navigation.PAGE_TEXT)
        # 断言是否进入bat脚本管理页
        self.assertText(navigation.BAT_SCRIPT_TEXT)
        self.my_click(element=navigation.online_alert_button)
        # 断言上线提示文案
        self.sleep(1)
        online_alert_text = self.my_get_text(element=navigation.online_alert_text)
        assert online_alert_text == navigation.ONLINE_ALERT_TEXT
        # 点击确定上线
        self.my_click(element=navigation.online_button)
        # 检查脚本状态
        self.assertText("已上线")
        self.close()