# -*- coding: utf-8 -*-
# @Time : 2021/9/16 20:21
# @File : test_19_create_public_shell_scripts.py
# @Project : bk_job


from bk_job.test_dir.test_01_login import LoginBase
from bk_job.page import public_script as page
from bk_job.page import create_shell_script_page as create_page


# 创建shell脚本
class CreateShellScript(LoginBase):
    def test_01_createShell(self):
        '''创建公共shell脚本'''
        # 登录态验证
        self._test_login()
        # 进入平台管理页面
        self.click(xpath=page.public_script_list)
        self.sleep(1)
        self.click(xpath=page.public_script_page)
        # 点击新建脚本
        self.click(xpath=page.create_script_button)
        self.sleep(1)
        # 输入脚本名称,描述,版本,脚本内容
        self.type(xpath=create_page.input_script_name, text=page.PUBLIC_SHELL_SCRIPT_NAME)
        self.type(xpath=create_page.script_description, text=create_page.SCRIPT_NAME)
        self.type(xpath=create_page.script_version, index=1, text=create_page.SCRIPT_VERSION)
        self.type(xpath=create_page.script_content, text=create_page.SCRIPT_TEXT)
        # 点击提交
        self.click(xpath=create_page.submit_button)
        self.wait(5)
        # 断言是否跳转到版本管理
        self.assertText(create_page.PAGE_TEXT)
        # 断言新建脚本状态
        script_status = self.get_text(xpath=create_page.script_status)
        assert script_status == '未上线'
        print('新建shell公共脚本成功')

    def test_02_debugShell(self):
        '''调试脚本'''
        # 断言是否跳转到版本管理
        self.assertText(create_page.PAGE_TEXT)
        # 断言是否进入shell脚本管理页
        self.assertText(create_page.SCRIPT_NAME)
        # 点击调试脚本
        self.click(xpath=create_page.debug_button)
        self.wait(5)
        # 跳转到调试脚本页面
        self.switch_to_window(self.window_handles[1])
        # 断言跳转url是否正确
        self.assertInUrl('debugScript')
        # 断言脚本内容是否覆盖
        self.assertText(create_page.SCRIPT_TEXT)
        # 关闭跳转的选项卡
        self.close()
        print('调试成功')

    def test_03_onlineShell(self):
        '''上线脚本'''
        self.switch_to_window(self.window_handles[0])
        # 断言是否跳转到版本管理
        self.assertText(create_page.PAGE_TEXT)
        # 断言是否进入shell脚本管理页
        self.assertText(create_page.SCRIPT_NAME)
        # 点击上线
        self.click(xpath=create_page.online_button)
        # 断言上线提示文案
        online_alert_text = self.get_text(xpath=create_page.online_alert_text)
        assert online_alert_text == create_page.ONLINE_ALERT_TEXT
        # 点击确定上线
        self.click(xpath=create_page.online_alert_button)
        # 检查脚本状态
        script_status = self.get_text(xpath=create_page.script_status)
        assert script_status == '已上线'
        print('上线成功')
