import seldom

from bk_paasv3.test_dir import test_01_login
from bk_paasv3.page import application_development, cloud_api
from public_method.keyboard_operation import MyWebDriver
from time import sleep
import datetime

class Application_Permission(seldom.TestCase):
    def test_01_active_authorization_gateway(self):
        '''主动授权（按网关）'''
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
        # 权限管理
        self.click(xpath=cloud_api.authority_management)
        # 应用权限
        self.click(xpath=cloud_api.application_permission)
        sleep(3)
        # 主动授权
        self.click(xpath=cloud_api.active_authorization)
        # 输入蓝鲸应用ID
        self.type(xpath=cloud_api.Blue_whale_application,text='bk_cmdb')
        # 保存
        self.click(xpath=cloud_api.save_Blue_whale)
        # 断言
        self.assertText(cloud_api.assert_save_Blue_whale)
    def test_02_active_authorization_resource(self):
        '''主动授权（按资源）'''
        # 主动授权
        self.click(xpath=cloud_api.active_authorization)
        # 输入蓝鲸应用ID
        self.type(xpath=cloud_api.Blue_whale_application,text='bk_cmdb')
        # 按资源
        self.click(xpath=cloud_api.per_resource)
        # 选择资源
        self.click(xpath=cloud_api.click_resource)
        # 保存
        self.click(xpath=cloud_api.save_resource)
        # 断言
        self.assertText(cloud_api.assert_save_Blue_whale)
    def test_03_export(self):
        '''导出应用权限'''
        # 导出
        self.click(xpath=cloud_api.export_application_permission)
        # 导出全部应用权限
        self.click(xpath=cloud_api.export_all_application_permission)
        # 断言
        self.assertText(cloud_api.assert_export_successful)
    def test_04_search_permission(self):
        '''搜索应用权限'''
        # 点击搜索框
        self.click(xpath=cloud_api.search_application_permission)
        # 点击蓝鲸应用ID
        self.click(xpath=cloud_api.Blue_Whale_application_ID)
        # 点击搜索框
        self.click(xpath=cloud_api.search_application_permission)
        # 输入bk_cmdb
        self.type(xpath=cloud_api.search_application_permission,text='bk_cmdb')
        # 模拟enter键
        MyWebDriver.Keys(xpath=cloud_api.search_application_permission).enter()
        # 断言
        self.assertText(cloud_api.assert_search_application_permission)
    def test_05_approval_history(self):
        '''审批历史'''
        # 点击审批历史
        self.click(xpath=cloud_api.approval_history)
        # 详情
        self.click(xpath=cloud_api.details)
        # 断言
        self.assertText(cloud_api.assert_details_of_approval)

