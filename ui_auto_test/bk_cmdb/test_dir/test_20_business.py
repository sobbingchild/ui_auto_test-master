from time import sleep
import seldom

from bk_cmdb import settings
from bk_cmdb.page import resource
from bk_cmdb.access_test_dir import test_01_login
from public_method.keyboard_operation import MyWebDriver

class BusinessDelete(seldom.TestCase):
    def test_01_delete_business(self):
        """编辑业务"""
        # 进入首页
        test_01_login.Login.test_login(self)
        # 点击资源
        test_01_login.Login.click_resource(self)
        # 点击业务
        self.click(xpath=resource.click_business)
        sleep(1)
        # 输入业务名进行enter搜索
        self.type(xpath=resource.search_business_name, text=settings.BUSINESS_NAME_CMDB)
        MyWebDriver.Keys(xpath=resource.search_business_name).enter()
        sleep(1)
        # 点击业务
        self.click(xpath=resource.click_test_business)
        # 编辑生命周期
        self.click(xpath=resource.lifecycle)
        # 选择生命周期，测试中
        self.click(xpath=resource.select_lifecycle)
        # 勾选
        self.click(xpath=resource.check_lifecycle)
        # 断言
        self.assertText(resource.assert_update)
    def test_02_recover_business(self):
        """归档业务、恢复归档业务"""
        # 点击返回
        self.click(xpath=resource.return_business)
        # 点击归档
        self.click(xpath=resource.pigeonhole)
        # 确定归档
        self.click(xpath=resource.sure_pigeonhole)
        self.assertText(resource.assert_pigeonhole)
        sleep(1)
        # 查看已归档的业务
        self.click(xpath=resource.filed)
        # 输入业务名进行搜索
        self.type(css=resource.inpu_business_name, text=settings.BUSINESS_NAME_CMDB)
        MyWebDriver.Keys(css=resource.inpu_business_name).enter()
        # 恢复业务
        self.click(xpath=resource.recover_business)
        # 清除后缀-archived
        MyWebDriver.Keys(xpath=resource.recover_business_name).backspace()
        MyWebDriver.Keys(xpath=resource.recover_business_name).backspace()
        MyWebDriver.Keys(xpath=resource.recover_business_name).backspace()
        MyWebDriver.Keys(xpath=resource.recover_business_name).backspace()
        MyWebDriver.Keys(xpath=resource.recover_business_name).backspace()
        MyWebDriver.Keys(xpath=resource.recover_business_name).backspace()
        MyWebDriver.Keys(xpath=resource.recover_business_name).backspace()
        MyWebDriver.Keys(xpath=resource.recover_business_name).backspace()
        MyWebDriver.Keys(xpath=resource.recover_business_name).backspace()
        # 确定恢复
        self.click(xpath=resource.sure_recover_business)
        # 断言
        self.assertText(resource.assert_recover_business_success)
    def test_03_delete_business(self):
        """删除业务"""
        # 点击返回业务
        self.click(xpath=resource.return_business)
        # 点击归档
        self.click(xpath=resource.pigeonhole)
        # 确定归档
        self.click(xpath=resource.sure_pigeonhole)
        self.assertText(resource.assert_pigeonhole)
        sleep(1)
        # 查看已归档的业务
        self.click(xpath=resource.filed)
        # 输入业务名进行搜索
        self.type(css=resource.inpu_business_name, text=settings.BUSINESS_NAME_CMDB)
        MyWebDriver.Keys(css=resource.inpu_business_name).enter()
        sleep(1)
        self.click(xpath=resource.completely_cancel)
        # 确定删除
        self.click(xpath=resource.sure_delete_business)
        # 断言
        self.assertText(resource.assert_delete_business)
