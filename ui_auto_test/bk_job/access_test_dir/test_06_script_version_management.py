# -*- coding: utf-8 -*-
# @Time : 2021/7/24 16:48
# @File : test_05_script_version_management.py
# @Project : bk_job


from bk_job.test_dir.test_01_login import LoginBase

from bk_job.page import create_shell_script_page

from bk_job.page import script_version_page as page


# 创建shell脚本
class ScriptVersionManagement(LoginBase):
    def test_01_create_shell_version(self):
        '''创建脚本版本'''
        # 登录态验证
        self._test_login()
        # 跳转到 脚本管理页面
        self.click(xpath=page.script_page)
        # 断言shell脚本是否创建成功
        self.assertText(create_shell_script_page.SCRIPT_NAME)
        # 点击脚本管理
        self.click(xpath=page.version_button(create_shell_script_page.SCRIPT_NAME), index=1)
        self.wait(5)
        # 断言是否进入版本管理
        self.assertText(create_shell_script_page.PAGE_TEXT)
        # 断言脚本状态
        self.assertText('已上线')
        # 点击复用并新建
        self.click(xpath=page.create_new_version(create_shell_script_page.SCRIPT_VERSION), index=2)
        # 断言进入新建脚本
        self.assertText('新建脚本')
        # 断言脚本版本为admin.xxx
        version = self.get_text(xpath=page.version)
        self.assertIn('admin', container=version)
        # 点击提交
        self.click(xpath=page.submit_button)
        self.wait(3)
        print('提交成功')

    def test_02_onlineScript(self):
        '''上线脚本'''
        # 断言是否进入版本管理页面
        self.assertText(create_shell_script_page.PAGE_TEXT)
        # 断言新提交的脚本状态
        status = self.get_text(xpath=create_shell_script_page.script_status)
        assert status == '未上线'
        # 点击上线
        self.click(xpath=create_shell_script_page.online_button)
        online_alert_text = self.get_text(xpath=create_shell_script_page.online_alert_text)
        assert online_alert_text == create_shell_script_page.ONLINE_ALERT_TEXT
        # 点击确定上线
        self.click(xpath=create_shell_script_page.online_alert_button)
        # #检查脚本状态
        script_status = self.get_text(xpath=create_shell_script_page.script_status)
        assert script_status == '已上线'
        print('脚本上线成功')
