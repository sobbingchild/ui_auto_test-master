from time import sleep
import seldom
from bk_nodeman.page import cloud_area_management
from bk_nodeman.test_dir import test_01_login
from bk_cmdb.page import resource, business
from bk_cmdb import settings as cmdb_settings
from bk_cmdb.access_test_dir import test_01_login as cmdb_login
from bk_nodeman.base_operate import BaseOperate
from bk_nodeman.access_test_dir import test_01_login
from bk_nodeman import settings as nodeman_settings
from public_method.keyboard_operation import MyWebDriver

base = BaseOperate()

class DeleteBusinessCloud(seldom.TestCase):
    def test_01_delete_host(self):
        """删除主机"""
        # 进入CMDB
        test_01_login.Login.test_login_cmdb(self)
        # 点击业务
        test_01_login.Login.click_business(self)
        #点击请选择业务
        self.click(xpath=business.businessselector)
        # 等待后输入业务
        sleep(1)
        self.type(css=business.select_search_input, text=nodeman_settings.BUSINESS_NAME_NODEMAN)
        self.click(xpath=business.option_name_nodeman)
        sleep(1)
        self.click(xpath=business.checkbox_blue_whale_host)
        # 点击转移至
        self.click(xpath=business.transfer)
        # 点击主机池
        self.click(xpath=business.host_pool)
        # 归还至目录
        self.click(xpath=business.return_host)
        sleep(0.5)
        # 搜索框搜索空闲机
        self.type(xpath=business.search_idle_pool, text=cmdb_settings.SEARCH_IDLE_HOST)
        # 点击空闲机
        self.click(xpath=business.click_idle_pool)
        # 确定转移主机至空闲机
        self.click(xpath=business.sure_transfer_idle_pool)
        # 断言
        self.assertText(business.assert_transfer)
        sleep(5)
        # 点击资源
        cmdb_login.Login.click_resource(self)
        sleep(5)
        # 搜索框输入'主机'
        self.type(xpath=resource.search_host, text=cmdb_settings.SEARCH_HOST)
        sleep(1)
        # 点击主机
        self.click(xpath=resource.click_host)
        # 点击高级筛选中搜索主机
        self.click(xpath=resource.high_search)
        sleep(0.5)
        #搜索框中搜索IP
        self.type(xpath=resource.input_host,text=nodeman_settings.WINDOWS_IP)
        # 模拟enter键，换行
        MyWebDriver.Keys(xpath=resource.input_host).enter()
        # 再次输入ip
        self.type(xpath=resource.input_host,text=nodeman_settings.WINDOWS_IP_PAGENT)
        # 模拟enter键，换行
        MyWebDriver.Keys(xpath=resource.input_host).enter()
        # 再次输入ip
        self.type(xpath=resource.input_host,text=nodeman_settings.LINUX_IP_PAGENT_FIRST)
        # 模拟enter键，换行
        MyWebDriver.Keys(xpath=resource.input_host).enter()
        # 再次输入ip
        self.type(xpath=resource.input_host,text=nodeman_settings.LINUX_IP_PAGENT_SECOND)
        # 模拟enter键，换行
        MyWebDriver.Keys(xpath=resource.input_host).enter()
        # 再次输入ip
        self.type(xpath=resource.input_host,text=nodeman_settings.PROXY_INTER_IP_FIRST)
        # 模拟enter键，换行
        MyWebDriver.Keys(xpath=resource.input_host).enter()
        # 再次输入ip
        self.type(xpath=resource.input_host,text=nodeman_settings.PROXY_INTER_IP_SECOND)
        # 查询
        self.click(xpath=resource.click_search)
        # 勾选主机
        self.click(xpath=resource.checkbox_blue_whale_host)
        # 点击更多,删除，确认删除
        self.click(xpath=resource.more)
        self.click(xpath=resource.delete)
        self.click(xpath=resource.sure_delete)
        self.assertText(resource.assert_delete)
    def test_02_delete_business(self):
        """删除业务"""
        # 进入首页
        sleep(3)
        test_01_login.Login.test_login_cmdb(self)
        # 点击资源
        test_01_login.Login.click_resource(self)
        # 点击业务
        self.click(xpath=resource.click_business)
        sleep(1)
        # 输入业务名进行enter搜索
        self.type(xpath=resource.search_business_name, text=nodeman_settings.BUSINESS_NAME_NODEMAN)
        MyWebDriver.Keys(xpath=resource.search_business_name).enter()
        sleep(3)
        # 点击归档
        self.click(xpath=resource.pigeonhole)
        # 确定归档
        self.click(xpath=resource.sure_pigeonhole)
        self.assertText(resource.assert_pigeonhole)
        sleep(1)
        # 查看已归档的业务
        self.click(xpath=resource.filed)
        # 输入业务名进行搜索
        self.type(css=resource.inpu_business_name, text=nodeman_settings.BUSINESS_NAME_NODEMAN)
        MyWebDriver.Keys(css=resource.inpu_business_name).enter()
        sleep(1)
        self.click(xpath=resource.completely_cancel)
        # 确定删除
        self.click(xpath=resource.sure_delete_business)
        # 断言
        self.assertText(nodeman_settings.BUSINESS_NAME_NODEMAN + resource.assert_delete_business)
    def test_03_cloud_area_edit(self):
        """编辑云区域"""
        test_01_login.Login.test_login(self)
        test_01_login.Login.click_cloud_management(self)
        #搜索框输入"测试云区域用"
        self.type(css=cloud_area_management.searchcloud,text=nodeman_settings.CLOUD_AREA_NAME)
        #点击编辑按钮
        self.click(css=cloud_area_management.editcloud)
        sleep(1)
        #删除测试云区域用并输入测试
        MyWebDriver.Keys(css=cloud_area_management.cloudname).backspace()
        MyWebDriver.Keys(css=cloud_area_management.cloudname).backspace()
        MyWebDriver.Keys(css=cloud_area_management.cloudname).backspace()
        MyWebDriver.Keys(css=cloud_area_management.cloudname).backspace()
        MyWebDriver.Keys(css=cloud_area_management.cloudname).backspace()
        MyWebDriver.Keys(css=cloud_area_management.cloudname).backspace()
        self.type(css=cloud_area_management.cloudname,text=nodeman_settings.TEST_AREA_NAME)
        #点击保存
        self.click(css=cloud_area_management.savecloud)
        #断言编辑成功
        self.assertText(cloud_area_management.asserttext_edit_cloud)
    def test_04_delete_cloud_area(self):
        test_01_login.Login.test_login(self)
        test_01_login.Login.click_cloud_management(self)
        """删除云区域"""
        sleep(60)
        #搜索框输入
        self.type(css=cloud_area_management.searchcloud,text=nodeman_settings.TEST_AREA_NAME)
        #点击删除
        self.click(css=cloud_area_management.deletecloud)
        #确定删除
        self.click(css=cloud_area_management.sure_delete_cloud)
        #断言，删除成功
        self.assertText(cloud_area_management.asserttext_delete_cloud)




