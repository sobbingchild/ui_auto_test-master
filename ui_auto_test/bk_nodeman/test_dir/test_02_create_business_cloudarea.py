from time import sleep
import seldom

from bk_nodeman.test_dir import test_01_login
from bk_nodeman import settings as nodeman_settings
from bk_nodeman.page import cloud_area_management
from bk_cmdb import settings as cmdb_settings
from bk_cmdb.page import resource
from public_method.keyboard_operation import MyWebDriver

class Create(seldom.TestCase):
    def test_01_create_business(self):
        """创建业务"""
        # 进入首页
        test_01_login.Login.test_login_cmdb(self)
        # 点击资源
        test_01_login.Login.click_resource(self)
        # 搜索''业务''
        self.type(xpath=resource.business, text=cmdb_settings.BUSINESS)
        sleep(0.5)
        # 点击业务
        self.click(xpath=resource.click_business)
        # 点击新建
        self.click(xpath=resource.new)
        sleep(0.5)
        # 输入业务信息，业务名
        self.type(xpath=resource.business_name, text=nodeman_settings.BUSINESS_NAME_NODEMAN)
        # 输入用户名admin
        self.click(xpath=resource.click_username)
        sleep(1)
        MyWebDriver.Keys(xpath=resource.username).input(cmdb_settings.USERNAME)
        sleep(2)
        # 确定admin用户
        self.click(xpath=resource.sure_username)
        # 提交
        self.click(xpath=resource.commit)
        self.assertText(resource.asserttext)

        #新建云区域
    def test_02_cloud_area_creat(self):
        """新建云区域"""
        test_01_login.Login.test_login(self)
        test_01_login.Login.click_cloud_management(self)
        #点击新建
        self.click(css=cloud_area_management.addcloud)
        #等待界面加载完成，输入云区域信息
        sleep(2)
        self.type(css=cloud_area_management.cloudname,text=nodeman_settings.CLOUD_AREA_NAME)
        #选择云服务商腾讯云
        self.click(css=cloud_area_management.select_cloud)
        sleep(2)
        self.click(xpath=cloud_area_management.tencent_cloud)
        #提交并断言
        self.click(css=cloud_area_management.commit_cloud)
        sleep(1)
        self.assertText(cloud_area_management.asserttext_creation_cloud)
