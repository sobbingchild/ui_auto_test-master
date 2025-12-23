# -*- coding: utf-8 -*-
# @Time : 2024/10/15 15:56
# @Project : JOB_327
from product_page import settings
from public_method.login import LoginBase
from product_page.bk_job import home
from product_page.bk_job import navigation
from product_page.bk_job import quick_excute_scripts
from product_page.public_components import ip_choose
from public_method.base_operate import BaseOperate
BaseOperate = BaseOperate()
# 创建shell脚本--无IP依赖
class CreateShellScript(LoginBase):
    '''shell脚本创建、上线'''
    def test_01_createShell(self):
        ''' 创建shell脚本'''
        # 进入 资源-脚本 页面
        #self.max_window()
        self.my_click(element=home.navigation_close)
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
        settings.script_name = name
        # 输入脚本名称,描述,版本,脚本内容
        self.my_type(element=navigation.input_script_name, text=name)
        self.my_type(element=navigation.script_description, text=name)
        self.my_type(element=navigation.script_version, index=1, text=navigation.SCRIPT_VERSION)
        self.my_type(element=navigation.script_content, text=navigation.SCRIPT_TEXT)
        # 点击提交
        self.sleep(1)
        self.my_click(element=navigation.submit_button)
        # 断言是否跳转到版本管理
        self.assertText(navigation.PAGE_TEXT)
        # 断言新建脚本状态
        self.sleep(1)
        script_status = self.my_get_text(element=navigation.script_status)
        assert script_status == '未上线'
        print('新建shell脚本成功')

    def test_02_debugShell(self):
        ''' 调试脚本'''
        # 断言是否跳转到版本管理
        self.assertText(navigation.PAGE_TEXT)
        # 断言是否进入shell脚本管理页
        #self.assertText(navigation.SCRIPT_NAME)
        # 点击调试脚本
        self.my_click(element=navigation.debug_button)
        self.sleep(2)
        # 跳转到调试脚本页面
        self.switch_to_window(1)
        # 断言跳转url是否正确
        self.assertInUrl('debugScript')
        # 断言脚本内容是否覆盖
        self.assertText(navigation.SCRIPT_TEXT)
        # 滚动
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
        self.sleep(2)
        self.assertText(navigation.RUN_STATE)
        # 关闭跳转的选项卡

    def test_03_onlineShell(self):
        '''上线脚本'''
        self.switch_to_window(0)
        # 断言是否跳转到版本管理
        self.assertText(navigation.PAGE_TEXT)
        # 断言是否进入shell脚本管理页
        #self.assertText(navigation.SCRIPT_NAME)
        # 点击上线
        self.my_click(element=navigation.online_alert_button)
        # 断言上线提示文案
        online_alert_text = self.my_get_text(element=navigation.online_alert_text)
        assert online_alert_text == navigation.ONLINE_ALERT_TEXT
        # 点击确定上线
        self.my_click(element=navigation.online_button)
        # 检查脚本状态
        self.assertText("已上线")
        self.close()
