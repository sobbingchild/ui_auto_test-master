from time import sleep
import seldom

from bk_cmdb import settings
from bk_cmdb.page import resource
from bk_cmdb.access_test_dir import test_01_login
from public_method.keyboard_operation import MyWebDriver

class BusinessDelete(seldom.TestCase):
    def test_01_delete_business(self):
        """删除业务"""
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
        self.assertText(settings.BUSINESS_NAME_CMDB + "-archived" + resource.assert_delete_business)
