from time import sleep
import seldom

from bk_nodeman import settings,custom_function
from bk_nodeman.page import agent_management
from bk_nodeman.test_dir import test_01_login
from public_method.keyboard_operation import MyWebDriver

class ReinstallPagent(seldom.TestCase):
    def test_01_reinstall_linux_pagent(self):
        """重安装linux主机（云区域）"""
        # 点击云区域管理
        test_01_login.Login.test_login(self)
        #点击搜索框
        self.click(css=agent_management.data_placeholder)
        #输入搜索的IP
        self.type(css=agent_management.data_placeholder,text=settings.LINUX_IP_PAGENT_FIRST)
        #确认
        MyWebDriver.Keys(css=agent_management.data_placeholder).enter()
        # 勾选linux主机
        self.click(css=agent_management.linux_host)
        # 点击安装Agent
        self.click(css=agent_management.install_agent)
        sleep(1.5)
        self.click(css=agent_management.confirm_reinstall)
        self.assertText(settings.STATUS)
        global reinstall_linuxpagent_url
        reinstall_linuxpagent_url = self.get_url
        print(reinstall_linuxpagent_url)
    def test_02_reinstall_windows_pagent(self):
        """重安装windows主机（云区域）"""
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
        # 点击安装Agent
        self.click(css=agent_management.install_agent)
        sleep(1.5)
        self.click(css=agent_management.confirm_reinstall)
        #断言执行状态
        self.assertText(settings.STATUS)
        reinstall_windowspagent_url = self.get_url
        print(reinstall_windowspagent_url)
        # 断言安装widnwos（pagent）是否成功
        custom_function.test_login_assert(self, reinstall_windowspagent_url)
        self.is_visible(420,xpath=agent_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)
        # 断言安装linux（pagent直连区域）是否成功
        custom_function.test_login_assert(self,reinstall_linuxpagent_url)
        self.is_visible(420, xpath=agent_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)
