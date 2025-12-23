from time import sleep
import seldom

from bk_cmdb.page import business
from bk_cmdb import settings
from bk_cmdb.access_test_dir import test_01_login


class Cluster_Module(seldom.TestCase):
    def test_01_new_cluster_module(self):
        """创建集群模块"""
        # 进入首页，点击业务
        test_01_login.Login.test_login(self)
        # 点击资源
        test_01_login.Login.click_business(self)
        self.click(xpath=business.businessselector)
        # 等待后输入业务名并点击
        sleep(1)
        self.type(css=business.select_search_input, text=settings.BUSINESS_NAME_CMDB)
        self.click(xpath=business.option_name)
        # self.is_visible(5,xpath=business.business_title)
        # 鼠标悬浮至业务名新建集群
        self.move_to_element(xpath=business.business_title)
        sleep(2)
        # self.is_visible(5,xpath=business.creat_cluster)
        self.click(xpath=business.creat_cluster)
        # 点击直接新建并输入集群名
        self.click(xpath=business.new_direct)
        self.type(css=business.cluster_name, text=business.cluster_name_text)
        # 提交新建的集群
        self.click(xpath=business.commit_cluster)
        sleep(1)
        self.assertText(business.asserttext)
        # 点击集群,点击立即创建(创建模块)
        self.click(css=business.click_cluster)
        sleep(1)
        self.click(xpath=business.immediately_the_new)
        # 点击直接新建并输入模块名
        self.click(xpath=business.new_direct_second)
        self.type(css=business.module_name, text=business.module_name_text)
        # 提交新建的模块
        self.click(css=business.commit_module)
        sleep(1)
        self.assertText(business.asserttext)
