from time import sleep
from bk_cmdb.page import business
import seldom
from bk_cmdb.test_dir import test_01_login

class Create_Module_Field(seldom.TestCase):
    def test_01_create_module_group(self):
        # 登陆进入首页，并点击业务
        test_01_login.Login.test_login(self)
        sleep(1)
        # 点击业务
        test_01_login.Login.click_business(self)
        # 点击自定义字段
        self.click(xpath=business.menu_name_custom_field)
        # 点击模块
        self.click(xpath=business.click_module_field)
        # 点击新建分组
        self.click(xpath=business.add_module_group)
        # 输入分组名称
        self.type(xpath=business.group_name,text=business.groupname_new)
        # 点击提交
        self.click(xpath=business.commit)
        # 断言
        self.assertText(business.assert_create_success)

    def test_02_creat_module_field(self):
        # 点击新建字段
        self.click(xpath=business.module_new_field)
        # 输入唯一标识
        self.type(xpath=business.unique_identification,text=business.groupname)
        # 输入名称
        self.type(xpath=business.field_name, text=business.fieldname)
        # 点击字段分组
        self.click(xpath=business.click_field_group)
        # 选择新建的分组
        self.click(xpath=business.new_group)
        # 点击提交
        self.click(xpath=business.commit_field )
        # 断言
        self.assertText(business.assert_create_success)

    def test_03_edit_module_field(self):
        # 点击新建字段 进行编辑
        self.click(xpath=business.new_field_name)
        # 点击编辑
        self.click(xpath=business.click_edit)
        # 编辑输入名称
        self.type(xpath=business.field_name, text=business.fieldname)
        # 点击保存
        self.click(xpath=business.commit_field)
        # 断言
        self.assertText(business.edit_success)

    def test_04_delete_module_group_field(self):
        # 点击删除字段
        self.click(xpath=business.new_delete_field)
        # 确认删除
        self.click(xpath=business.notarize_delete_field)
        # 删除分组，点击3个点iocn
        self.move_to_element(xpath=business.more)
        self.click(xpath=business.more)
        sleep(0.5)
        # 点击删除分组
        self.click(xpath=business.delete_grouping)
        # 断言
        self.assertText(business.assert_delete)
