import seldom
from time import sleep

from bk_nodeman import settings
from bk_nodeman.page import agent_management,business
from bk_nodeman.access_test_dir import test_01_login


class LinuxAgent(seldom.TestCase):
    def test_01_install_linux_agent(self):
        """安装直连（linux）Agent"""
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
        print(BluekingHostIp)
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
        self.type(xpath=agent_management.input_password, text=settings.BLUEKING_PASSWORD)
        sleep(1)
        # 点击安装
        self.click(xpath=agent_management.install)
        self.is_visible(150,xpath=agent_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)
