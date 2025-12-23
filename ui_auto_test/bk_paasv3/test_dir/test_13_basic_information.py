import seldom

from bk_paasv3.test_dir import test_01_login
import datetime
from public_method.keyboard_operation import MyWebDriver
from bk_paasv3.page import cloud_api


class Basic_Information(seldom.TestCase):
    def test_01_deployment_restrictions(self):
        """编辑网关基本信息"""
        # 进入首页
        test_01_login.Login.test_login(self)
        # 点击云API
        self.click(xpath=cloud_api.cloud_api)
        # 跳转到界面第二个窗口并获取url跳转
        self.switch_to_window(1)
        global url
        url = self.get_url
        self.open(url)
        # 搜索框搜索新建的网关
        self.type(xpath=cloud_api.search_gateway, text='test' + str(
            datetime.datetime.now().day))
        # 模拟enter键
        MyWebDriver.Keys(xpath=cloud_api.search_gateway).enter()
        # 点击网关
        self.click(xpath=cloud_api.click_gateway)
        # 点击基本信息,设置等待时间，防止界面不可点击
        self.click(xpath=cloud_api.basic_information)
        # 编辑
        self.click(xpath=cloud_api.edit_gateway)
        # 编辑描述信息
        self.type(xpath=cloud_api.edit_descriptor, text='test' + str(
            datetime.datetime.now().day))
        # 保存
        self.click(xpath=cloud_api.save_descriptor)
        # 断言
        self.assertText(cloud_api.assert_update)
