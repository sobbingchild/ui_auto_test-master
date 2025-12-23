import seldom

from bk_paasv3.test_dir import test_01_login
from bk_paasv3.page import application_development, cloud_api
from public_method.keyboard_operation import MyWebDriver
from time import sleep
import datetime


class Au_Audi_Bnt_Pass(seldom.TestCase):
    def test_01_cloud_api_permissions(self):
        '''云API权限申请权限'''
        # 进入首页
        test_01_login.Login.test_login(self)
        # 点击应用开发
        self.click(xpath=application_development.application_development)
        # 搜索框搜索应用
        self.type(xpath=application_development.search_application, text="节点管理")
        sleep(3)
        # 模拟enter键
        MyWebDriver.Keys(xpath=application_development.search_application).enter()
        # 点击应用
        self.click(xpath=application_development.click_application)
        # 云API管理
        self.click(xpath=application_development.Cloud_API_management)
        # 云API权限
        self.click(xpath=application_development.Cloud_API_permissions)
        sleep(3)
        # 网关列表搜索网关
        self.type(xpath=application_development.search_gateway, text='test' + str(
            datetime.datetime.now().day))
        # 点击网关
        self.click(xpath=cloud_api.click_gateway_test)
        sleep(3)
        # 申请网关权限
        self.click(xpath=cloud_api.applying_for_gateway_permission)
        # 填写申请权限
        self.type(xpath=cloud_api.permission_information, text='测试')
        # 确定
        self.click(xpath=cloud_api.sure_permission_information)
        # 断言
        self.assertText(cloud_api.assert_applying)

    def test_02_au_audi_bnt_pass(self):
        '''通过全部申请权限'''
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
        # 权限管理
        self.click(xpath=cloud_api.authority_management)
        # 权限审批
        self.click(xpath=cloud_api.apigwPermissionApply)
        # 全部通过
        self.click(xpath=cloud_api.all_pass)
        # 确定
        self.click(xpath=cloud_api.sure_all_pass)
        # 断言
        self.assertText(cloud_api.assert_operate_successfully)

