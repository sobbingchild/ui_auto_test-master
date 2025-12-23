from time import sleep
import seldom

from bk_nodeman import settings,custom_function
from bk_nodeman.page import agent_management
from bk_nodeman.test_dir import test_01_login
from public_method.keyboard_operation import MyWebDriver

class UninstallPagent(seldom.TestCase):
    def test_01_uninstall_linux_pagent(self):
        """执行卸载linux主机（云区域）"""
        # 点击云区域管理
        test_01_login.Login.test_login(self)
        #点击搜索框
        self.click(css=agent_management.data_placeholder)
        #输入搜索的IP
        self.type(css=agent_management.data_placeholder,text=settings.LINUX_IP_PAGENT_FIRST)
        #确认
        MyWebDriver.Keys(css=agent_management.data_placeholder).enter()
        #勾选linux主机
        self.click(css=agent_management.linux_host)
        # 点击批量并卸载
        self.click(css=agent_management.batch)
        self.click(xpath=agent_management.uninstall_linux)
        sleep(3)
        self.click(css=agent_management.confirm_reinstall)
        self.assertText(settings.STATUS)
        global uninstall_linuxpagent_url
        uninstall_linuxpagent_url = self.get_url
        print(uninstall_linuxpagent_url)

    def test_02_uninstall_windows_pagent(self):
        """执行卸载windows主机（云区域）,分别断言卸载widnwos、linux（pagent）是否成功"""
        # 点击云区域管理
        test_01_login.Login.test_login(self)
        #点击搜索框
        self.click(css=agent_management.data_placeholder)
        #输入搜索的IP
        self.type(css=agent_management.data_placeholder,text=settings.WINDOWS_IP_PAGENT)
        #确认
        MyWebDriver.Keys(css=agent_management.data_placeholder).enter()
        # 勾选windows主机
        self.click(css=agent_management.linux_host)
        # 点击批量并卸载
        self.click(css=agent_management.batch)
        self.click(xpath=agent_management.uninstall_linux)
        sleep(2)
        self.click(css=agent_management.confirm_reinstall)
        self.assertText(settings.STATUS)
        uninstall_windowspagent_url = self.get_url
        print(uninstall_windowspagent_url)
        # 断言安装widnwos（pagent）是否成功
        custom_function.test_login_assert(self, uninstall_windowspagent_url)
        self.is_visible(180,xpath=agent_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)
        # 断言安装linux（pagent直连区域）是否成功
        custom_function.test_login_assert(self,uninstall_linuxpagent_url)
        self.is_visible(180, xpath=agent_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)



