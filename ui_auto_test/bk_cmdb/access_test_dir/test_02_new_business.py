from time import sleep
import seldom

from bk_cmdb.page import resource
from bk_cmdb import settings
from bk_cmdb.access_test_dir import test_01_login
from public_method.keyboard_operation import MyWebDriver

class BusinessCreate(seldom.TestCase):
    def test_01_new_business(self):
        """创建业务"""
        # 进入首页
        test_01_login.Login.test_login(self)
        # 点击资源
        test_01_login.Login.click_resource(self)
        # 搜索''业务''
        self.type(xpath=resource.business, text=settings.BUSINESS)
        sleep(0.5)
        # 点击业务
        self.click(xpath=resource.click_business)
        # 点击新建
        self.click(xpath=resource.new)
        sleep(0.5)
        # 输入业务信息，业务名
        self.type(xpath=resource.business_name, text=settings.BUSINESS_NAME_CMDB)
        # 输入用户名admin
        self.click(xpath=resource.click_username)
        sleep(1)
        MyWebDriver.Keys(xpath=resource.username).input(settings.USERNAME)
        sleep(2)
        # 确定admin用户
        self.click(xpath=resource.sure_username)
        # 提交
        self.click(xpath=resource.commit)
        self.assertText(resource.asserttext)
