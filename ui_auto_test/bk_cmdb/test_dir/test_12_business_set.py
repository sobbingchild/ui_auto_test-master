from time import sleep
import seldom

from bk_cmdb import settings
from bk_cmdb.page import resource
from bk_cmdb.access_test_dir import test_01_login
from public_method.keyboard_operation import MyWebDriver

class BusinessSet(seldom.TestCase):
    def test_01_new_business_set(self):
        """新建业务集"""
        # 进入首页
        test_01_login.Login.test_login(self)
        # 点击资源
        test_01_login.Login.click_resource(self)
        # 点击业务集
        self.click(xpath=resource.click_business_set)
        sleep(1)
        # 点击新建
        self.click(xpath=resource.creat_business_set)
        # 输入业务集名
        self.type(xpath=resource.business_set_name,text=resource.businessset_name)
        # 点击提交
        self.click(xpath=resource.commit_businessset_name)
        sleep(2)
        # 断言
        self.assertText(resource.asserttext_creat)
        # 预览(默认预览第一个业务，即新创建的业务)，为接下来查看是否包含测试业务（配置平台自动化测试）
        self.click(xpath=resource.preview)
        # 搜索框搜索业务
        # self.is_visible(5,xpath=resource.search_business)
        self.type(xpath=resource.search_business,text=settings.BUSINESS_NAME_CMDB)
        # 模拟enter键
        MyWebDriver.Keys(xpath=resource.search_business).enter()
        # 断言
        self.assertElement(xpath=resource.business_searchname)

    def test_02_edit_business_set(self):
        """编辑业务集"""
        self.click(xpath=resource.close_windows)
        # 编辑
        self.click(xpath=resource.edit_business_set)
        # 输入业务集描述
        # self.is_visible(5,xpath=resource.business_set_describe)
        self.type(xpath=resource.business_set_describe,text=resource.businessset_name)
        # 保存
        self.click(xpath=resource.commit_businessset_name)
        # 断言
        self.assertText(resource.assert_edit_success)

    def test_03_delete_business_set(self):
        """删除业务集"""
        # 删除
        self.click(xpath=resource.delete_business_set)
        # 确认删除
        self.click(xpath=resource.sure_delete_business_set)
        # 断言
        self.assertText(resource.asserttext_delete)







