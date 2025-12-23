import seldom

from bk_paasv3.test_dir import test_01_login
import datetime
from public_method.keyboard_operation import MyWebDriver
from bk_paasv3.page import cloud_api
from time import sleep


class Label(seldom.TestCase):
    def test_01_deployment_restrictions(self):
        """新建/删除标签"""
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
        # 点击标签管理,设置等待时间，防止界面不可点击
        self.click(xpath=cloud_api.label_management)
        sleep(3)
        # 新建标签
        self.click(xpath=cloud_api.new_label)
        # 输入标签名
        self.type(xpath=cloud_api.input_tag_name, text='测试标签')
        # 确定
        self.click(xpath=cloud_api.sure_tag_name)
        # 断言
        self.assertText(cloud_api.assert_successful_creation)
        # 点击删除
        self.click(xpath=cloud_api.delete_tag_name)
        # 确定
        self.click(xpath=cloud_api.sure_delete_tag_name)
        # 断言
        self.assertText(cloud_api.assert_delete_successfully)
