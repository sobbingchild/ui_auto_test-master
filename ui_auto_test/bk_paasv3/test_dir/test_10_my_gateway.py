import seldom

from bk_paasv3.test_dir import test_01_login
import datetime
from public_method.keyboard_operation import MyWebDriver
from bk_paasv3.page import cloud_api


class My_Gateway(seldom.TestCase):
    def test_01_create_gateway(self):
        """创建网关"""
        # 进入首页
        test_01_login.Login.test_login(self)
        # 点击云API
        self.click(xpath=cloud_api.cloud_api)
        # 跳转到界面第二个窗口并获取url跳转
        self.switch_to_window(1)
        global url
        url = self.get_url
        self.open(url)
        # 点击创建网关
        self.click(xpath=cloud_api.create_gateway)
        # 输入网关名称
        self.type(xpath=cloud_api.gateway_name, text='test' + str(
            datetime.datetime.now().day))
        # 输入描述
        self.type(xpath=cloud_api.gateway_describe, text='测试用')
        # 创建
        self.click(xpath=cloud_api.create)
        self.assertText(cloud_api.assert_create)

    def test_02_search_gateway(self):
        """搜索网关"""
        # 点击我的网关
        self.open(url)
        # 搜索框搜索新建的网关
        self.type(xpath=cloud_api.search_gateway, text='test' + str(
            datetime.datetime.now().day))
        # 模拟enter键
        MyWebDriver.Keys(xpath=cloud_api.search_gateway).enter()
        # 点击网关
        self.click(xpath=cloud_api.click_gateway)

    def test_03_new_resource(self):
        """新建资源"""
        # 新建资源
        self.click(xpath=cloud_api.new_resource)
        # 输入资源名称
        self.type(xpath=cloud_api.resource_name, text='test' + str(
            datetime.datetime.now().day))
        # 输入请求路径
        self.type(xpath=cloud_api.request_path, text='/')
        # 输入path路径
        self.type(xpath=cloud_api.path, text='/')
        # 点击校验
        self.click(xpath=cloud_api.check)
        # 断言
        self.assertText(cloud_api.assert_verify)
        # 提交
        self.click(xpath=cloud_api.commit_resource)
        # 断言
        self.assertText(cloud_api.assert_successful_creation)

    def test_04_edit_resource(self):
        """编辑资源"""
        # 编辑
        self.click(xpath=cloud_api.edit_resource)
        # 输入名称
        self.type(xpath=cloud_api.edit_resource_name, text='test')
        # 提交
        self.click(xpath=cloud_api.edit_commit_resource)
        # 断言
        self.assertText(cloud_api.assert_update)

    def test_05_search_resource(self):
        """根据名称搜索资源"""
        # 搜索框根据资源名称搜索资源
        self.type(xpath=cloud_api.search_resource_name, text='test' + str(
            datetime.datetime.now().day) + 'test')
        # 模拟enter键搜索
        MyWebDriver.Keys(xpath=cloud_api.search_resource_name).enter()
        # 断言
        self.assertText(cloud_api.assert_updated)

    def test_06_derived_resource(self):
        """导出资源"""
        # 点击导出
        self.click(xpath=cloud_api.export)
        # 点击全部资源
        self.click(xpath=cloud_api.total_resource)
        # 确定
        self.click(xpath=cloud_api.sure_export_resource)
        # 断言
        self.assertText(cloud_api.assert_export_successful)

    def test_07_set_attributes(self):
        """全选字段显示"""
        # 点击设置
        self.click(xpath=cloud_api.set)
        # 全选属性
        self.click(xpath=cloud_api.attribute)
        # 确认
        self.click(xpath=cloud_api.sure_select_attribute)

    def test_08_creat_document(self):
        """新建中文/英文文档，删除中文/英文文档"""
        # 点击文档下面的+
        self.click(xpath=cloud_api.create_document)
        # 立即创建中文文档
        self.click(xpath=cloud_api.create_Chinese_document)
        # 提交
        self.click(xpath=cloud_api.commit_Chinese_document)
        # 断言
        self.assertText(cloud_api.assert_save_successfully)
        # 删除中文文档
        self.click(xpath=cloud_api.delete_Chinese_document)
        # 确定删除
        self.click(xpath=cloud_api.sure_delete_document)
        # 断言
        self.assertText(cloud_api.assert_delete_successfully)
        # 点击英文文档
        self.click(xpath=cloud_api.click_English_document)
        # 立即创建
        self.click(xpath=cloud_api.create_English_document)
        # 点击提交
        self.click(xpath=cloud_api.commit_Chinese_document)
        # 断言
        self.assertText(cloud_api.assert_save_successfully)
        # 删除英文文档
        self.click(xpath=cloud_api.delete_English_document)
        # 确定
        # self.click(xpath='//body/div[9]/div/div/div/div[4]/div/button[1]/div/span')
        # 确定
        self.click(xpath=cloud_api.sure_delete_document)
        # 断言
        self.assertText(cloud_api.assert_delete_successfully)
        # 返回资源管理界面
        self.click(xpath=cloud_api.return_resource_management)

    # def test_09_edit_delete_resource(self):
    #     """编辑/删除资源"""
    #     # 勾选资源
    #     self.click(xpath=cloud_api.check_resources)
    #     # 点击批量
    #     self.click(xpath=cloud_api.batch)
    #     # 编辑资源
    #     self.click(xpath=cloud_api.edit_resources)
    #     # 确定批量编辑资源
    #     self.click(xpath=cloud_api.sure_edit_resource)
    #     # 断言
    #     self.assertText(cloud_api.assert_batch_edit_successfully)
    #     # 勾选资源
    #     self.click(xpath=cloud_api.check_resources)
    #     # 点击批量
    #     self.click(xpath=cloud_api.batch)
    #     # 删除资源
    #     self.click(xpath=cloud_api.delete_resource)
    #     # 确定删除并断言
    #     self.click(xpath=cloud_api.sure_delete_resource)
    #     # 断言
    #     self.assertText(cloud_api.assert_batch_delete_successfully)
