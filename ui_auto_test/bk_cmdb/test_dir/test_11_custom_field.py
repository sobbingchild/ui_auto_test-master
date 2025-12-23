from time import sleep
from bk_cmdb.page import business
import seldom

from bk_cmdb.test_dir import test_01_login
from bk_cmdb import settings


class Custom_Field(seldom.TestCase):
    def test_01_new_grouping(self):
        """新建主机分组（蓝鲸业务下）"""
        # 进入首页点击业务
        test_01_login.Login.test_login(self)
        sleep(2)
        test_01_login.Login.click_business(self)
        # 点击自定义字段
        # self.is_visible(5,xpath=business.menu_name_custom_field)
        self.click(xpath=business.menu_name_custom_field)
        self.click(xpath=business.menu_name_custom_field)
        # 点击主机
        self.click(xpath=business.click_host_grouping)
        # 新建分组
        self.click(xpath=business.add_grouping)
        # 输入分组名称
        self.type(xpath=business.group_name,text=business.groupname)
        # 提交
        self.click(xpath=business.commit)
        # 断言
        self.assertText(business.assert_create_success)

    def test_02_new_field(self):
        """新建字段（蓝鲸业务下）"""
        # 新建业务字段
        self.click(xpath=business.add_field)
        # 输入唯一标识
        self.type(xpath=business.unique_identification,text=business.groupname)
        # 输入名称
        self.type(xpath=business.field_name,text=business.fieldname)
        # 点击 字段 分组
        self.click(xpath=business.click_field_group)
        # 选择新建的分组
        self.click(xpath=business.new_host_group)
        # 点击提交
        self.click(xpath=business.commit_field)
        # 断言
        self.assertText(business.assert_create_success)

    def test_03_edit_field(self):
        """编辑字段（蓝鲸业务下）"""
        # 点击字段
        self.click(css=business.click_field_backlog)
        # 点击编辑
        self.click(xpath=business.return_list_host)
        # 输入名称进行编辑
        self.type(css=business.user_prompts,text=business.test)
        # 保存
        self.click(xpath=business.commit_field)
        # 断言
        self.assertText(business.edit_success)

    def test_04_delete_grouping(self):
        """删除分组（蓝鲸业务下）"""
        # 返回主机
        self.click(xpath=business.return_grouping)
        # 点击字段测试
        self.click(css=business.click_field)
        # 点击字段删除
        self.click(xpath=business.delete_field)
        # 确定删除字段
        self.click(xpath=business.sure_delete_field)
        # 断言
        self.assertText(business.assert_delete)
        # 点击更多三个点,做了模糊匹配，匹配到倒数第一个分组
        # self.is_visible(5,xpath=business.more)
        sleep(2)
        self.move_to_element(xpath=business.more)
        self.click(xpath=business.more)
        # 点击删除分组
        # self.is_visible(5,xpath=business.delete_grouping)
        self.click(xpath=business.delete_grouping)
        # 断言
        self.assertText(business.assert_delete)


