from time import sleep
import seldom

from bk_nodeman import settings,custom_function
from bk_nodeman.page import agent_management
from bk_nodeman.test_dir import test_01_login


class InstallPagent(seldom.TestCase):
    def test_01_install_linux_pagent(self):
        """执行安装linux(pagent)"""
        test_01_login.Login.test_login(self)
        # 点击安装Agent
        sleep(0.5)
        # 点击安装Agent
        self.click(css=agent_management.install_agent)
        sleep(0.5)
        # 点击普通安装
        self.click(css=agent_management.general_installation)
        sleep(1)
        # 点击安装到业务
        self.click(xpath=agent_management.install_business)
        # 输入业务名并点击节点管理自动化测试
        self.type(css=agent_management.input_business_id, text=settings.BUSINESS_NAME_NODEMAN)
        sleep(1)
        self.click(css=agent_management.business)
        # 点击云区域并选择为节点管理测试用勿删
        sleep(1)
        self.click(xpath=agent_management.click_cloud_area)
        self.click(css=agent_management.cloud_area)
        # 输入IP及密码
        self.type(css=agent_management.input_ip, text=settings.LINUX_IP_PAGENT_FIRST)
        self.type(css=agent_management.input_password, text=settings.HOST_PASSWORD)
        # 点击安装
        self.click(xpath=agent_management.install)
        self.assertText(settings.STATUS)
        global install_linuxpagent_url
        install_linuxpagent_url = self.get_url
        print(install_linuxpagent_url)


    def test_02_install_windows_pagent(self):
        """执行安装windows（pagent）,分别断言安装widnwos、linux（pagent）是否成功"""
        test_01_login.Login.test_login(self)
        # 点击安装Agent
        self.click(css=agent_management.install_agent)
        sleep(5)
        # 点击普通安装
        self.click(css=agent_management.general_installation)
        #等待界面加载完成，防止无法选择系统
        sleep(5)
        # 点击安装到业务
        self.click(xpath=agent_management.install_business)
        # 输入业务名并点击节点管理自动化测试
        self.type(css=agent_management.input_business_id, text=settings.BUSINESS_NAME_NODEMAN)
        sleep(1)
        self.click(css=agent_management.business)
        # 点击云区域并选择为节点管理测试用
        sleep(1)
        self.click(xpath=agent_management.click_cloud_area)
        self.click(css=agent_management.cloud_area)
        # 输入IP、密码
        self.type(css=agent_management.input_ip, text=settings.WINDOWS_IP_PAGENT)
        self.type(css=agent_management.input_password, text=settings.HOST_PASSWORD)
        # 选择操作系统为windows
        self.click(css=agent_management.operating_system)
        self.click(xpath=agent_management.system)
        # 点击安装
        self.click(xpath=agent_management.install)
        self.assertText(settings.STATUS)
        install_windowspagent_url = self.get_url
        print(install_windowspagent_url)
        # 断言安装widnwos（pagent）是否成功
        custom_function.test_login_assert(self, install_windowspagent_url)
        self.is_visible(420,xpath=agent_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)
        # 断言安装linux（pagent直连区域）是否成功
        custom_function.test_login_assert(self,install_linuxpagent_url)
        self.is_visible(420, xpath=agent_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)




