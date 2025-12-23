from time import sleep
import seldom
from bk_nodeman import settings,custom_function
from bk_nodeman.page import cloud_area_management, agent_management,business
from bk_nodeman.test_dir import test_01_login
from public_method.keyboard_operation import MyWebDriver

class UinstallAgent(seldom.TestCase):
    def test_01_uninstall_linux_agent(self):
        """执行卸载linux"""
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
        # 进入Agent管理搜索框输入蓝鲸业务下的机器并搜索
        self.type(css=agent_management.data_placeholder, text=BluekingHostIp)
        MyWebDriver.Keys(css=agent_management.data_placeholder).enter()
        # 勾选主机（linux-直连）
        self.click(css=agent_management.linux_host)
        # 点击批量
        self.click(css=agent_management.batch)
        # 点击卸载
        self.click(xpath=agent_management.uninstall_linux)
        sleep(1)
        self.click(css=agent_management.confirm_reinstall)
        self.assertText(settings.STATUS)
        global uninstall_linux_url
        uninstall_linux_url = self.get_url
        print(uninstall_linux_url)

    def test_02_uninstall_proxy(self):
        """执行卸载proxy"""
        # 点击云区域管理
        test_01_login.Login.click_cloud_management(self)
        # 在搜索框输入"节点管理测试用"
        self.type(css=cloud_area_management.searchcloud, text=settings.CLOUD_AREA_NAME)
        # 点击云区域
        self.click(css=cloud_area_management.cloud_area_name)
        sleep(1)
        # 点击更多并卸载
        self.click(xpath=cloud_area_management.more)
        self.click(css=cloud_area_management.uninstall_proxy)
        # 确定卸载
        self.click(css=cloud_area_management.sure_reboot)
        self.assertText(settings.STATUS)
        global uninstall_proxy_url
        uninstall_proxy_url = self.get_url
        print(uninstall_proxy_url)

    def test_03_uninstall_windows_agent(self):
        """执行卸载windows，分别断言卸载widnwos、linux、proxy是否成功"""
        # 点击Agent管理
        test_01_login.Login.click_agent_management(self)
        # 搜索框输入10.0.15.184并搜索
        self.type(css=agent_management.data_placeholder, text=settings.WINDOWS_IP)
        MyWebDriver.Keys(css=agent_management.data_placeholder).enter()
        # 勾选主机10.0.15.184
        self.click(css=agent_management.windows_host)
        # 点击批量
        self.click(css=agent_management.batch)
        # 点击卸载
        self.click(xpath=agent_management.uninstall_linux)
        sleep(1)
        # 卸载
        self.click(css=agent_management.confirm_reinstall)
        self.assertText(settings.STATUS)
        uninstall_windows_url = self.get_url
        print(uninstall_windows_url)
        # 断言卸载widnwos（agent直连区域）是否成功
        custom_function.test_login_assert(self, uninstall_windows_url)
        self.is_visible(180,xpath=agent_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)
        # 断言卸载linux（agent直连区域）是否成功
        custom_function.test_login_assert(self,uninstall_linux_url)
        self.is_visible(180, xpath=agent_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)
        # 断言卸载proxy是否成功
        custom_function.test_login_assert(self, uninstall_proxy_url)
        self.is_visible(180, xpath=agent_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)


