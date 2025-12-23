import seldom
from time import sleep
from bk_nodeman import settings,custom_function
from bk_nodeman.page import agent_management, cloud_area_management,business
from bk_nodeman.test_dir import test_01_login



class InstallAgent(seldom.TestCase):
    def test_01_install_linux_agent(self):
        """执行安装直连linux（直连区域）"""
        test_01_login.Login.test_login_cmdb(self)
        # 点击资源
        test_01_login.Login.click_business(self)
        # 等待后输入业务名并点击
        sleep(1)
        #默认进入蓝鲸业务，展开Pass平台，点击apigw
        self.click(xpath=business.pass_platform)
        self.click(xpath=business.apigw)
        #获取模块apigw的IP值
        global BluekingHostIp
        BluekingHostIp = self.get_text(xpath=business.get_host)
        sleep(3)
        test_01_login.Login.test_login(self)
        # 点击安装Agent
        self.click(css=agent_management.install_agent)
        sleep(0.5)
        # 点击普通安装
        self.click(css=agent_management.general_installation)
        sleep(1)
        # 点击安装到业务
        self.click(xpath=agent_management.install_business)
        # 输入业务名并点击蓝鲸
        self.type(css=agent_management.input_business_id, text=settings.BLUE_BUSINESS)
        sleep(1)
        self.click(css=agent_management.business)
        # 点击云区域并选择为直连区域
        self.click(xpath=agent_management.click_cloud_area)
        self.click(css=agent_management.directly_connected_area)
        # 输入IP地址及密码
        self.type(css=agent_management.input_ip, text=BluekingHostIp)
        self.type(css=agent_management.input_password, text=settings.BLUEKING_PASSWORD)
        # 点击安装
        self.click(xpath=agent_management.install)
        self.assertText(settings.STATUS)
        global install_linux_url
        install_linux_url = self.get_url
        print(install_linux_url)

    def test_02_install_proxy(self):
        """执行安装proxy"""
        # 点击云区域管理
        test_01_login.Login.click_cloud_management(self)
        sleep(1)
        # 在搜索框输入"节点管理动UI自动化"
        self.type(css=cloud_area_management.searchcloud, text=settings.CLOUD_AREA_NAME)
        sleep(1)
        # 点击安装proxy
        self.click(xpath=cloud_area_management.install_proxy)
        sleep(0.5)
        # 输入第一台prxoy的主机信息
        self.type(css=cloud_area_management.input_proxy_inter_ip_first, text=settings.PROXY_INTER_IP_FIRST)
        self.type(css=cloud_area_management.input_proxy_internet_first, text=settings.PROXY_INTERNET_FIRST)
        self.type(css=cloud_area_management.input_proxy_internet_login_first, text=settings.PROXY_INTERNET_FIRST)
        self.type(css=cloud_area_management.proxy_password_first, text=settings.HOST_PASSWORD)
        # 输入第二台proxy的主机信息
        self.type(css=cloud_area_management.input_proxy_inter_ip_second, text=settings.PROXY_INTER_IP_SECOND)
        self.type(css=cloud_area_management.input_proxy_internet_second, text=settings.PROXY_INTERNET_SECOND)
        self.type(css=cloud_area_management.input_proxy_internet_login_second, text=settings.PROXY_INTERNET_SECOND)
        self.type(css=cloud_area_management.proxy_password_second, text=settings.HOST_PASSWORD)
        # 点击归属业务并输入业务ID,确定
        self.click(css=cloud_area_management.business)
        self.type(css=cloud_area_management.input_business_id, text=settings.BUSINESS_NAME_NODEMAN)
        sleep(0.5)
        self.click(css=cloud_area_management.sure_business)
        sleep(0.5)
        # 点击安装
        self.click(css=cloud_area_management.install)
        self.assertText(settings.STATUS)
        global install_proxy_url
        install_proxy_url = self.get_url
        print(install_proxy_url)

    def test_03_install_windows_agent(self):
        """执行安装windows（直连区域），分别断言安装windwos、linux、proxy是否成功"""
        test_01_login.Login.click_agent_management(self)
        # 点击安装Agent
        self.click(css=agent_management.install_agent)
        sleep(0.5)
        # 点击普通安装
        self.click(css=agent_management.general_installation)
        #防止界面不可选择windows系统，等待界面加载完成
        sleep(5)
        # 点击安装到业务
        self.click(xpath=agent_management.install_business)
        # 输入业务ID并点击节点管理测试用
        self.type(css=agent_management.input_business_id, text=settings.BUSINESS_NAME_NODEMAN)
        sleep(1)
        self.click(css=agent_management.business)
        # 点击云区域并选择为直连区域
        sleep(1)
        self.click(xpath=agent_management.click_cloud_area)
        self.click(css=agent_management.directly_connected_area)
        # 输入IP地址及密码
        self.type(css=agent_management.input_ip, text=settings.WINDOWS_IP)
        self.type(css=agent_management.input_password, text=settings.HOST_PASSWORD)
        # 选择操作系统windows
        self.click(css=agent_management.operating_system)
        self.click(xpath=agent_management.system)
        # 点击安装
        self.click(xpath=agent_management.install)
        # 判断是否正在执行
        self.assertText(settings.STATUS)
        install_windows_url = self.get_url
        print(install_windows_url)
        # 断言安装widnwos（agent直连区域）是否成功
        custom_function.test_login_assert(self, install_windows_url)
        self.is_visible(600,xpath=agent_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)
        # 断言安装proxy是否成功,存在windows安装时间较短的情况，增加判断
        custom_function.test_login_assert(self, install_proxy_url)
        self.is_visible(600,xpath=agent_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)
        # 断言安装linux（agent直连区域）是否成功
        custom_function.test_login_assert(self,install_linux_url)
        self.is_visible(300,xpath=agent_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)
