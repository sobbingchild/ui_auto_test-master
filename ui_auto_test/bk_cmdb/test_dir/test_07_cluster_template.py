import time
from time import sleep
from bk_cmdb.page import business
import seldom
from bk_cmdb import settings

from bk_cmdb.test_dir import test_01_login


class Business_Cluster_Template(seldom.TestCase):
    def test_01_new_cluster_template(self):
        """新建集群模板"""
        # 进入首页点击业务
        test_01_login.Login.test_login(self)
        sleep(1)
        test_01_login.Login.click_business(self)
        sleep(1)
        self.click(xpath=business.businessselector)
        # 等待后输入业务id并点击
        sleep(1)
        self.type(css=business.select_search_input, text=settings.BUSINESS_NAME_CMDB)
        self.click(xpath=business.option_name)

        # 点击集群模板
        self.click(css=business.menu_name_cluster_template)
        sleep(1)
        # 点击新建
        self.click(css=business.create_cluster_template)
        # 输入模板名称
        self.type(xpath=business.edit_templatename, text=business.cluster_template_name)
        # 添加属性字段
        self.click(xpath=business.add_attribute)
        # 勾选环境类型
        self.click(xpath=business.environmental_type)
        # 确定
        self.click(xpath=business.sure_add_attribute)
        sleep(1)
        # 添加服务模板
        self.click(xpath=business.add_servicetemplate)
        # 勾选单个模板
        self.click(xpath=business.check_service_template)
        # 确定
        self.click(xpath=business.sure_service_template)
        # 提交
        self.click(xpath=business.operationaltemplate_button_submit)
        self.assertText(business.assert_create_success)

    def test_02_edit_cluster_template(self):
        """编辑集群模板"""
        # 返回列表
        self.click(xpath=business.return_list)
        sleep(0.5)
        # 点击编辑
        self.click(xpath=business.edit_cluster_template)
        # 添加服务模板
        self.click(xpath=business.second_add_servicetemplate)
        # 点击服务模板
        self.click(xpath=business.second_check_service_template)
        # 确定
        self.click(xpath=business.sure_service_template)
        # 保存
        self.click(xpath=business.operationaltemplate_button_submit)
        self.assertText(business.edit_success)

    def test_03_delete_servicetemplate_process(self):
        """删除服务模板、删除进程"""
        # 进入首页，点击业务
        self.click(xpath=business.close_window)
        # 点击服务模板
        self.click(css=business.menu_name_template)
        # 编辑模板
        self.click(xpath=business.edit_template)
        # 删除第一个进程
        self.click(css=business.delete_process)
        # 确认删除进程
        self.click(xpath=business.sure_delte_process)
        # 保存
        self.click(xpath=business.confirm)
        # 断言
        self.assertText(business.assert_success)
        # 点击服务模板
        self.click(css=business.menu_name_template)
        # 点击删除（服务模板）
        self.click(xpath=business.delete_template)
        # 确认删除模板
        self.click(xpath=business.sure_delete_template)
        # 断言删除成功
        self.assertText(business.assert_delete)
