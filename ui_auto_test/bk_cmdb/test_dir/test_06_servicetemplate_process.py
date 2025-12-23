from time import sleep
from bk_cmdb.page import business
import seldom

from bk_cmdb import settings
from bk_cmdb.test_dir import test_01_login


class Servicetemplate_Process(seldom.TestCase):
    def test_01_new_servicetemplate_process(self):
        """新建服务模板、新建进程"""
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

        # 点击服务模板
        self.click(css=business.menu_name_template)
        sleep(1)
        # 点击新建
        self.click(css=business.template_create)
        sleep(0.5)
        # 输入模板名称
        self.type(css=business.templatename, text=settings.TEMPLATE_NAME)
        # 点击添加属性字段
        self.click(xpath=business.add_attribute)
        # 点击模块类型
        self.click(xpath=business.module_type)
        # 点击确定
        self.click(xpath=business.sure_add_attribute)
        # 点击新建进程
        self.click(xpath=business.process_create)
        # 输入进程名称
        self.type(css=business.processname, text=settings.PROCESS_NAME)
        # 提交
        self.click(xpath=business.template_submit)
        sleep(1)
        # 新建进程
        self.click(xpath=business.process_create)
        # 输入进程信息
        self.type(css=business.processname, text=settings.PROCESS_NAME_SECOND)
        self.type(css=business.bk_process_name, text=settings.BK_PROCESS_NAME)
        # 点击进程管理,输入进程信息
        self.click(xpath=business.process_manage)
        self.type(css=business.work_path, text=settings.WORK_PATH)
        # 保存
        self.click(xpath=business.template_submit)
        # 提交
        self.click(xpath=business.operationaltemplate_button_submit)
        self.assertText(business.assert_create_success)

    def test_02_edit_servicetemplate_process(self):
        """编辑服务模板、编辑进程"""
        # 点击关闭
        self.click(xpath=business.close_window_servicetemplate)
        # 点击服务模板
        self.click(css=business.menu_name_template)
        # 点击编辑
        self.click(xpath=business.edit_template)
        sleep(1)
        # 修改模板名称
        self.click(xpath=business.edit_templatename)
        self.type(css=business.templatename, text=settings.EDIT_TEMPLATE_NAME)
        # 编辑第一个进程
        self.click(xpath=business.edit_nginx)
        # 修改进程别名
        self.type(css=business.bk_process_name, text=settings.BK_PROCESS_NAME)
        # 保存进程信息
        self.click(xpath=business.template_submit)
        # 保存
        self.click(xpath=business.save_edit_templatename)
        # 确认修改名称
        self.assertText(business.assert_success)

    def test_03_clone_servicetemplate_process(self):
        """克隆服务模板"""
        # 点击服务模板
        self.click(css=business.menu_name_template)
        # 克隆模板
        self.click(xpath=business.clone_template)
        # 修改模板名称进行克隆模板
        self.type(css=business.templatename, text=business.clone)
        # 提交
        self.click(xpath=business.operationaltemplate_button_submit)
        # 断言
        self.assertText(business.assert_create_success)
