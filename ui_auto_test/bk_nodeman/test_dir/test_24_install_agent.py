from time import sleep
import seldom
from bk_nodeman import settings
from bk_nodeman.page import agent_management
from bk_nodeman.test_dir import test_01_login
from public_method.keyboard_operation import MyWebDriver

class PagentInstallLinux(seldom.TestCase):
    def test_01_install_commoa(self):
        """多IP安装，使用逗号（,）分隔IP"""
        test_01_login.Login.test_login(self)
        # 点击安装Agent
        sleep(0.5)
        # 点击安装Agent
        self.click(css=agent_management.install_agent)
        sleep(0.5)
        # 点击普通安装
        self.click(css=agent_management.general_installation)
        sleep(1)
        #点击安装到业务
        self.click(xpath=agent_management.install_business)
        #输入业务并点击节点管理自动化测试
        self.type(css=agent_management.input_business_id, text=settings.BUSINESS_NAME_NODEMAN)
        sleep(1)
        self.click(css=agent_management.business)
        #点击云区域并选择为节点管理UI自动化
        sleep(1)
        self.click(xpath=agent_management.click_cloud_area)
        self.click(css=agent_management.cloud_area)
        #输入IP及密码,使用逗号分隔IP
        self.type(css=agent_management.input_ip, text=settings.INSTALL_IP_COMMOA)
        self.type(css=agent_management.input_password, text=settings.HOST_PASSWORD)
        #点击安装
        self.click(xpath=agent_management.install)
        #断言是否正在执行
        self.is_visible(240,xpath=agent_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)

    def test_02_install_comma(self):
        """多IP安装，使用顿号（、）分隔IP"""
        test_01_login.Login.test_login(self)
        # 点击安装Agent
        sleep(0.5)
        # 点击安装Agent
        self.click(css=agent_management.install_agent)
        sleep(0.5)
        # 点击普通安装
        self.click(css=agent_management.general_installation)
        sleep(1)
        #点击安装到业务
        self.click(xpath=agent_management.install_business)
        #输入业务并点击节点管理测试用
        self.type(css=agent_management.input_business_id, text=settings.BUSINESS_NAME_NODEMAN)
        sleep(1)
        self.click(css=agent_management.business)
        #点击云区域并选择为节点管理测试用勿删
        sleep(1)
        self.click(xpath=agent_management.click_cloud_area)
        self.click(css=agent_management.cloud_area)
        #输入IP及密码,使用顿号分隔IP
        self.type(css=agent_management.input_ip, text=settings.INSTALL_IP_COMMA)
        self.type(css=agent_management.input_password, text=settings.HOST_PASSWORD)
        #点击安装
        self.click(xpath=agent_management.install)
        #断言
        self.is_visible(240,xpath=agent_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)

    def test_03_install_blank(self):
        """多IP安装，使用空格分隔IP"""
        test_01_login.Login.test_login(self)
        # 点击安装Agent
        sleep(0.5)
        # 点击安装Agent
        self.click(css=agent_management.install_agent)
        sleep(0.5)
        # 点击普通安装
        self.click(css=agent_management.general_installation)
        sleep(1)
        #点击安装到业务
        self.click(xpath=agent_management.install_business)
        #输入业务并点击节点管理自动化测试
        self.type(css=agent_management.input_business_id, text=settings.BUSINESS_NAME_NODEMAN)
        sleep(1)
        self.click(css=agent_management.business)
        #点击云区域并选择为节点管理测试用勿删
        sleep(1)
        self.click(xpath=agent_management.click_cloud_area)
        self.click(css=agent_management.cloud_area)
        #输入IP及密码,使用空格分隔IP
        self.type(css=agent_management.input_ip, text=settings.INSTALL_IP_BLANK)
        self.type(css=agent_management.input_password, text=settings.HOST_PASSWORD)
        #点击安装
        self.click(xpath=agent_management.install)
        #断言
        self.is_visible(240,xpath=agent_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)

    def test_04_install_newline(self):
        """多IP安装，使用换行分隔IP"""
        test_01_login.Login.test_login(self)
        # 点击安装Agent
        sleep(0.5)
        # 点击安装Agent
        self.click(css=agent_management.install_agent)
        sleep(0.5)
        # 点击普通安装
        self.click(css=agent_management.general_installation)
        sleep(1)
        #点击安装到业务
        self.click(xpath=agent_management.install_business)
        #输入业务ID并点击节点管理测试用
        self.type(css=agent_management.input_business_id, text=settings.BUSINESS_NAME_NODEMAN)
        sleep(1)
        self.click(css=agent_management.business)
        #点击云区域并选择为节点管理测试用勿删
        sleep(1)
        self.click(xpath=agent_management.click_cloud_area)
        self.click(css=agent_management.cloud_area)
        #输入LINUX_IP_Pagent
        self.type(css=agent_management.input_ip, text=settings.LINUX_IP_PAGENT_FIRST)
        #模拟enter键，换行分隔IP
        MyWebDriver.Keys(css=agent_management.input_ip).enter()
        #再次输入LINUX_IP_Pagent_2
        self.type(css=agent_management.input_ip, text=settings.LINUX_IP_PAGENT_SECOND)
        #输入密码
        self.type(css=agent_management.input_password, text=settings.HOST_PASSWORD)
        #点击安装
        self.click(xpath=agent_management.install)
        #断言是否正在执行
        self.is_visible(240,xpath=agent_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)

    def test_install_linux_pagent_05(self):
        """判断使用逗号顿号空格空行换行分隔IP安装是否成功"""
        test_01_login.Login.test_login(self)
        # 点击安装Agent
        sleep(0.5)
        # 点击安装Agent
        self.click(css=agent_management.install_agent)
        sleep(0.5)
        # 点击普通安装
        self.click(css=agent_management.general_installation)
        #点击安装到业务
        self.click(xpath=agent_management.install_business)
        #输入业务并点击节点管理自动化测试
        self.type(css=agent_management.input_business_id, text=settings.BUSINESS_NAME_NODEMAN)
        sleep(1)
        self.click(css=agent_management.business)
        #点击云区域并选择为节点管理UI自动化
        sleep(1)
        self.click(xpath=agent_management.click_cloud_area)
        self.click(css=agent_management.cloud_area)
        #输入LINUX_IP_Pagent
        self.type(css=agent_management.input_ip, text=settings.LINUX_IP_PAGENT_FIRST)
        #模拟enter键，换行分隔IP
        MyWebDriver.Keys(css=agent_management.input_ip).enter()
        MyWebDriver.Keys(css=agent_management.input_ip).enter()
        #再次输入LINUX_IP_Pagent_2
        self.type(css=agent_management.input_ip, text=settings.LINUX_IP_PAGENT_SECOND)
        #输入密码
        self.type(css=agent_management.input_password, text=settings.HOST_PASSWORD)
        #点击安装
        self.click(xpath=agent_management.install)
        #判断执行状态
        self.is_visible(240,xpath=agent_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)

