import seldom

from bk_paasv3.test_dir import test_01_login
import datetime
from public_method.keyboard_operation import MyWebDriver
from bk_paasv3.page import cloud_api
from time import sleep


class Version_Management(seldom.TestCase):
    def test_01_deployment_restrictions(self):
        """生成SDK版本号、断言发布历史功能"""
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
        # 点击发布变更
        self.click(xpath=cloud_api.publish_changes)
        # 点击版本管理
        self.click(xpath=cloud_api.version_management)
        sleep(3)
        # 点击编辑
        self.click(xpath=cloud_api.edit_version)
        # 编辑版本标题
        self.type(xpath=cloud_api.version_title, text='test' + str(
            datetime.datetime.now().day))
        # 确认
        self.click(xpath=cloud_api.sure_version_title)
        # 断言
        self.assertText(cloud_api.assert_version_update_succeeded)
        # 点击未生成
        self.click(xpath=cloud_api.not_generate)
        # 输入SDK版本号
        self.type(xpath=cloud_api.input_version_number, text='1.0.0')
        # 确定
        self.click(xpath=cloud_api.sure_version_number)
        # 断言
        self.assertText(cloud_api.assert_generated_successfully)
        # 发布历史
        self.click(xpath=cloud_api.release_history)
        # 断言
        self.assertText(cloud_api.assert_succeed)
