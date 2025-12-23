from time import sleep
import seldom

from bk_nodeman import settings
from bk_nodeman.page import plugin_management,login_page
from bk_nodeman.access_test_dir import test_01_login
from bk_nodeman.page import business
from public_method.keyboard_operation import MyWebDriver

class LinuxUpdatePlugin(seldom.TestCase):
    def test_01_update_linux_basereport(self):
        """更新插件"""
        test_01_login.Login.test_login_cmdb(self)
        # 点击资源
        test_01_login.Login.click_business(self)
        # 等待后输入业务名并点击
        sleep(1)
        #默认进入蓝鲸业务，展开Pass平台，点击apigw
        self.click(xpath=business.pass_platform)
        self.click(xpath=business.apigw)
        #获取模块apigw的IP值
        BluekingHostIp = self.get_text(xpath=business.get_host)
        print(BluekingHostIp)
        test_01_login.Login.test_login(self)
        # 点击插件状态
        self.click(xpath=login_page.click_plug_in)
        sleep(1)
        # 点击并选择业务
        self.click(css=plugin_management.click_business)
        sleep(0.5)
        # 搜索框输入"蓝鲸"
        self.type(css=plugin_management.search_business, text=settings.BLUE_BUSINESS)
        sleep(1)
        # 点击"节点管理测试用 ",必须加sleep,否则report报错stale element reference: element is not attached to the page document
        self.click(xpath=plugin_management.plugin_business)
        # 点击搜索框，输入IP
        self.click(xpath=plugin_management.plugin_select_search)
        self.type(xpath=plugin_management.search_host,text=BluekingHostIp)
        MyWebDriver.Keys(xpath=plugin_management.search_host).enter()
        # 勾选全部linux主机
        self.click(css=plugin_management.common_checkbox_tableCheckAll)
        #点击安装/更新操作
        self.click(css=plugin_management.plugin_btn_install)
        #选择插件basereport，下一步
        self.click(css=plugin_management.plugin_select_pluginName)
        self.click(xpath=plugin_management.select_plugin_basereport)
        self.click(css=plugin_management.common_btn_commit)
        # 下一步,下一步,立即执行
        self.click(css=plugin_management.common_btn_stepNext)
        sleep(1)
        self.click(css=plugin_management.step)
        sleep(0.5)
        self.click(css=plugin_management.common_btn_commit)
        # 等待安装/更新成功并断言
        self.is_visible(120,xpath=plugin_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)
