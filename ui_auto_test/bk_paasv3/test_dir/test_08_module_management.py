import seldom

from bk_paasv3.test_dir import test_01_login
from bk_paasv3.page import application_development
from public_method.keyboard_operation import MyWebDriver


class Module_Management(seldom.TestCase):
    def test_01_deployment_restrictions(self):
        '''开启关闭预发布/生产环境限制开关'''
        # 进入首页
        test_01_login.Login.test_login(self)
        # 点击应用开发
        self.click(xpath=application_development.application_development)
        # 搜索框搜索应用
        self.type(xpath=application_development.search_application,text="标准运维")
        # 模拟enter键
        MyWebDriver.Keys(xpath=application_development.search_application).enter()
        # 点击应用
        self.click(xpath=application_development.click_application)
        # 模块管理
        self.click(xpath=application_development.module_management)
        # 开启预发布/生产环境限制开关
        self.click(xpath=application_development.pre_release_environment)
        self.click(xpath=application_development.production_environment)
        self.assertText(application_development.assert_open_success)
        # 关闭预发布/生产环境限制开关
        self.click(xpath=application_development.pre_release_environment)
        self.click(xpath=application_development.production_environment)
        self.assertText(application_development.assert_close_success)
