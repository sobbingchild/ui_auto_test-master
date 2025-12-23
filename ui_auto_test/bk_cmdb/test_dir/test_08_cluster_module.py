from time import sleep
import seldom

from bk_cmdb.page import business
from bk_cmdb import settings
from bk_cmdb.test_dir import test_01_login
from public_method.keyboard_operation import MyWebDriver
import requests

class Cluster_Module(seldom.TestCase):
    def test_01_new_cluster_module(self):
        """创建集群、模块"""
        # 进入首页，点击业务
        test_01_login.Login.test_login(self)
        test_01_login.Login.click_business(self)
        self.click(xpath=business.businessselector)
        # 等待后输入业务名并点击
        sleep(1)
        self.type(css=business.select_search_input, text=settings.BUSINESS_NAME_CMDB)
        self.click(xpath=business.option_name)
        # self.is_visible(5,xpath=business.business_title)
        # 鼠标悬浮至业务名新建集群
        self.move_to_element(xpath=business.business_title)
        # self.is_visible(5,xpath=business.creat_cluster)
        sleep(2)
        self.click(xpath=business.creat_cluster)
        sleep(1)
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
    def test_02_edit_cluster_module(self):
        """编辑集群、模块"""
        # 点击节点信息
        self.click(xpath=business.node_information)
        # 编辑集群
        self.click(xpath=business.edit_cluster)
        # 输入集群描述
        self.type(xpath=business.cluster_description,text=business.test)
        # 保存
        self.click(xpath=business.save_edit_cluster)
        sleep(1)
        # 点击模块
        self.click(css=business.click_module)
        sleep(1)
        # 编辑模块
        self.click(xpath=business.edit_module)
        # 点击模块类型
        self.click(xpath=business.click_module_type)
        # 模块类型选择数据库
        self.click(xpath=business.click_db)
        # 保存
        self.click(xpath=business.save_edit_cluster)
    def test_03_delete_cluster_module(self):
        """删除集群、模块"""
        # 点击节点信息
        self.click(xpath=business.node_information)
        # 点击模块
        self.click(css=business.click_module)
        # 删除模块
        self.click(xpath=business.delete_module)
        # 确定删除
        self.click(xpath=business.sure_confirm)
        # 断言
        self.assertText(business.assert_delete)
        # 删除集群
        self.click(xpath=business.delete_module)
        # 确定删除
        self.click(xpath=business.sure_confirm)
        # 断言
        self.assertText(business.assert_delete)
    def test_04_edit_host(self):
        """编辑蓝鲸业务下的主机"""
        # 进入首页，点击业务
        test_01_login.Login.test_login(self)
        # 点击资源
        test_01_login.Login.click_business(self)
        self.click(xpath=business.businessselector)
        # 等待后输入业务名并点击
        sleep(1)
        self.type(css=business.select_search_input, text=settings.BLUE_BUSINESS)
        self.click(xpath=business.option_name_blue_business)
        # 默认进入蓝鲸业务，展开Pass平台，点击apigw
        self.click(xpath=business.pass_platform)
        self.click(xpath=business.apigw)
        # 点击主机
        self.click(xpath=business.click_host)
        # 点击铅笔进行编辑
        self.click(xpath=business.click_edit_comment)
        # 输入备注信息
        self.type(xpath=business.comment_message,text=business.test)
        # 确定并断言
        self.click(xpath=business.sure_edit_comment)
        # 断言
        self.assertText(business.edit_success)
        # 清除断言内容
        self.click(xpath=business.click_edit_comment)
        MyWebDriver.Keys(xpath=business.comment_message).backspace()
        MyWebDriver.Keys(xpath=business.comment_message).backspace()
        MyWebDriver.Keys(xpath=business.comment_message).backspace()
        self.click(xpath=business.sure_edit_comment)
        # 点击编辑（SLA级别）
        self.click(xpath=business.click_sla_level)
        # 选择SLA级别
        self.click(xpath=business.select_sla)
        # 确定SLA级别为L1
        self.click(xpath=business.sure_sla_level)


