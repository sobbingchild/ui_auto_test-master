from time import sleep
from bk_cmdb.page import business
import seldom

from bk_cmdb.test_dir import test_01_login
from bk_cmdb import settings

class Host_Automatic_Application(seldom.TestCase):
    def test_01_new_host_automatic_application_business(self):
        """启用主机属性自动应用（按业务拓扑）"""
        # 进入首页点击业务
        test_01_login.Login.test_login(self)
        sleep(1)
        test_01_login.Login.click_business(self)
        self.click(xpath=business.businessselector)
        # 等待后输入业务名并点击
        sleep(1)
        self.type(css=business.select_search_input, text=settings.BUSINESS_NAME_CMDB)
        self.click(xpath=business.option_name)
        # 点击主机自动应用
        # self.is_visible(5,xpath=business.menu_name_host_automatic_application)
        self.click(xpath=business.menu_name_host_automatic_application)
        # 点击立即启用
        self.click(xpath=business.immediately_to_enable)
        # 选择字段
        self.click(xpath=business.select_field)
        # 选择SLA级别
        self.click(xpath=business.sla_level)
        # 勾选确定
        self.click(xpath=business.sure_confirm)
        # 点击SLA级别
        self.click(xpath=business.click_sla)
        # 选择SLA级别L1
        self.click(xpath=business.select_sla)
        # 下一步
        self.click(xpath=business.confirm)
        # 保存并应用
        # self.is_visible(5,xpath=business.confirm)
        sleep(2)
        self.click(xpath=business.confirm)
        # 等待应用成功
        # self.is_visible(30,xpath=business.return_list_host)
        sleep(10)
        # 断言
        self.assertText(business.assert_application_successfully)
        # 返回列表
        self.click(xpath=business.return_list_host)
    def test_02_update_host_automatic_application_business(self):
        """修改主机属性自动应用（按业务拓扑）"""
        # 点击编辑
        self.click(xpath=business.edit_host_automatic_application)
        # 点击SLA级别
        self.click(xpath=business.click_sla)
        # 选择SLA级别L2
        self.click(xpath=business.select_sla_second)
        # 下一步
        self.click(xpath=business.confirm)
        # 保存并应用
        # self.is_visible(5,xpath=business.confirm)
        sleep(3)
        self.click(xpath=business.confirm)
        # 等待应用成功
        # self.is_visible(30,xpath=business.return_list_host)
        sleep(10)
        # 断言
        self.assertText(business.assert_application_successfully)
        # 返回列表
        self.click(xpath=business.return_list_host)

    def test_03_delete_host_automatic_application_business(self):
        """删除主机属性自动应用（按业务拓扑）"""
        # 点击关闭自动应用
        self.click(xpath=business.delete_host_automatic_application)
        # 不保留当前自动应用策略
        self.click(xpath=business.click_save_host_automatic_application)
        # 确定
        self.click(xpath=business.sure_confirm)
        # 断言
        self.assertText(business.assert_close_success)

    def test_04_new_host_automatic_application_service(self):
        """启用主机属性自动应用（按服务模板）"""
        # 点击按服务模板
        self.click(xpath=business.click_service_template)
        # 点击立即启用
        self.click(xpath=business.immediately_to_enable)
        # 选择字段
        self.click(xpath=business.select_field)
        # 选择SLA级别
        self.click(xpath=business.sla_level)
        # 勾选确定
        self.click(xpath=business.sure_confirm)
        # 点击SLA级别
        self.click(xpath=business.click_sla)
        # 选择SLA级别L1
        self.click(xpath=business.select_sla)
        # 下一步
        self.click(xpath=business.confirm)
        # 保存并应用
        # self.is_visible(5,xpath=business.confirm)
        sleep(3)
        self.click(xpath=business.confirm)
        # 等待应用成功
        # self.is_visible(30,xpath=business.return_list_host)
        sleep(10)
        # 断言
        self.assertText(business.assert_application_successfully)
        # 返回列表
        self.click(xpath=business.return_list_host)
    def test_05_update_host_automatic_application_service(self):
        """修改主机属性自动应用（按服务模板）"""
        # 点击编辑
        self.click(xpath=business.edit_host_automatic_application)
        # 点击SLA级别
        self.click(xpath=business.click_sla)
        # 选择SLA级别L2
        self.click(xpath=business.select_sla_second)
        # 下一步
        self.click(xpath=business.confirm)
        # 保存并应用
        # self.is_visible(5,xpath=business.confirm)
        sleep(3)
        self.click(xpath=business.confirm)
        # 等待应用成功
        # self.is_visible(30,xpath=business.return_list_host)
        sleep(10)
        # 断言
        self.assertText(business.assert_application_successfully)
        # 返回列表
        self.click(xpath=business.return_list_host)

    def test_06_delete_host_automatic_application_service(self):
        """删除主机属性自动应用（按服务模板）"""
        # 点击关闭自动应用
        self.click(xpath=business.delete_host_automatic_application)
        # 不保留当前自动应用策略
        self.click(xpath=business.click_save_host_automatic_application)
        # 确定
        self.click(xpath=business.sure_confirm)
        # 断言
        self.assertText(business.assert_close_success)