from time import sleep
import seldom

from bk_nodeman import settings,custom_function
from bk_nodeman.page import agent_management,cloud_area_management,business
from bk_nodeman.test_dir import test_01_login
from public_method.keyboard_operation import MyWebDriver

class ReInstallAgent(seldom.TestCase):
    def test_01_reinstall_linux_agent(self):
        """执行重安装linux"""
        test_01_login.Login.test_login_cmdb(self)
        # 点击资源
        test_01_login.Login.click_business(self)
        # 等待后输入业务名并点击
        sleep(1)
        # 默认进入蓝鲸业务，展开Pass平台，点击apigw
        self.click(xpath=business.pass_platform)
        self.click(xpath=business.apigw)
        # 获取模块apigw的IP值
        global BluekingHostIp
        BluekingHostIp = self.get_text(xpath=business.get_host)
        sleep(3)
        test_01_login.Login.test_login(self)
        # 点击Agent管理
        test_01_login.Login.click_agent_management(self)
        # 搜索框输入蓝鲸主机并搜索
        self.type(css=agent_management.data_placeholder, text=BluekingHostIp)
        MyWebDriver.Keys(css=agent_management.data_placeholder).enter()
        # 勾选蓝鲸主机
        self.click(css=agent_management.linux_host)
        # 点击安装Agent
        self.click(css=agent_management.install_agent)
        sleep(1)
        # 点击重装
        self.click(css=agent_management.confirm_reinstall)
        self.assertText(settings.STATUS)
        global reinstall_linux_url
        reinstall_linux_url = self.get_url
        print(reinstall_linux_url)
    def test_02_reinstall_proxy(self):
        """执行重安装proxy"""
        # 点击云区域管理
        test_01_login.Login.click_cloud_management(self)
        # 在搜索框输入"节点管理测试用"
        self.type(css=cloud_area_management.searchcloud, text=settings.CLOUD_AREA_NAME)
        # 点击云区域
        self.click(css=cloud_area_management.cloud_area_name)
        sleep(1)
        # 点击重装并确定重装
        self.click(xpath=cloud_area_management.reinstall_proxy)
        self.click(css=cloud_area_management.sure)
        self.assertText(settings.STATUS)
        global reinstall_proxy_url
        reinstall_proxy_url = self.get_url
        print(reinstall_proxy_url)

    def test_03_reinstall_windows_agent(self):
        """执行重安装widnwos，分别断言重安装linux、windwos、proxy是否安装成功"""
        # 点击Agent管理
        test_01_login.Login.test_login(self)
        # 搜索框输入10.0.15.184并搜索
        self.type(css=agent_management.data_placeholder, text=settings.WINDOWS_IP)
        MyWebDriver.Keys(css=agent_management.data_placeholder).enter()
        # 勾选主机10.0.15.184
        self.click(css=agent_management.linux_host)
        # 点击安装/重装
        self.click(css=agent_management.install_agent)
        sleep(1)
        self.click(css=agent_management.confirm_reinstall)
        # sleep(600)以前的安装时间600，现设为200
        # 判断是否正在执行
        self.assertText(settings.STATUS)
        reinstall_windows_url = self.get_url
        print(reinstall_windows_url)
        # 断言重安装windows（agent直连区域）是否成功
        custom_function.test_login_assert(self, reinstall_windows_url)
        self.is_visible(600,xpath=agent_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)
        # 断言重安装linux（agent直连区域）是否成功
        custom_function.test_login_assert(self,reinstall_linux_url)
        self.is_visible(600, xpath=agent_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)
        # 断言重安装proxy是否成功
        custom_function.test_login_assert(self, reinstall_proxy_url)
        self.is_visible(600, xpath=agent_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)

