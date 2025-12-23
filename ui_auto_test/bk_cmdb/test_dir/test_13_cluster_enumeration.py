from time import sleep
from bk_cmdb.page import business
import seldom
from bk_cmdb.test_dir import test_01_login


class Create_Cluster_Enumeration(seldom.TestCase):
    def test_01_new_group(self):
        # 登陆进入首页，并点击业务
        test_01_login.Login.test_login(self)
        sleep(1)
        # 点击业务
        test_01_login.Login.click_business(self)
        # 点击自定义字段
        self.click(xpath=business.menu_name_custom_field)
        # 点击新建分组（默认在集群下）
        self.click(xpath=business.add_grouping)
        # 输入分组名称
        self.type(xpath=business.group_name, text=business.groupname_new)
        # 提交
        self.click(xpath=business.commit)
        # 断言
        self.assertText(business.assert_create_success)

    #新建业务字段，字段类型为枚举（多选）
    def test_02_create_field(self):
        """新建字段（蓝鲸业务下）"""
        # 新建业务字段
        self.click(xpath=business.new_business_field)
        # 输入唯一标识
        self.type(xpath=business.unique_identification, text=business.groupname)
        # 输入名称
        self.type(xpath=business.field_name, text=business.fieldname)
        # 点击字段类型
        self.click(xpath=business.field_type)
        # 选择枚举（多选字段）
        self.click(xpath=business.type_enumeration)
        # 输入枚举id
        self.type(css=business.iput_id, text=business.groupname_new)
        # 输入枚举值
        self.type(css=business.input_price,text=business.new_price)
        # 点击提交
        self.click(xpath=business.commit_field)
        # 断言
        self.assertText(business.assert_create_success)

    #编辑字段
    def test_03_edit_field(self):
        # 点击业务字段
        self.click(xpath=business.new_field_name)
        # 点击编辑
        self.click(xpath=business.click_edit)
        # 编辑输入名称
        self.type(xpath=business.field_name, text=business.fieldname)
        # 点击保存
        self.click(xpath=business.commit_field)
        self.assertText(business.edit_success)

    #删除分组/字段
    def test_04_delete_group(self):

        # 点击删除字段
        self.click(xpath=business.new_delete_field)
        sleep(1)
        # 确认删除
        self.click(xpath=business.notarize_delete_field)
        # 点击3个点iocn(必须点两次才能识别更多按钮)
        self.click(xpath=business.more)
        sleep(0.5)
        self.click(xpath=business.group_icon)
        # 删除分组
        self.click(xpath=business.delete_grouping)
        # 断言
        self.assertText(business.assert_delete)