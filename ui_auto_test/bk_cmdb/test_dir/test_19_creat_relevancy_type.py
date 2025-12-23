from time import sleep
import seldom
from bk_cmdb.page import model
from bk_cmdb.test_dir import test_01_login
from public_method.keyboard_operation import MyWebDriver


class Relevancy_Type(seldom.TestCase):
    # 创建关联类型
    def test_01_creat_relevancy_type(self):
        #  进入首页- 点击模型
        test_01_login.Login.test_login(self)
        test_01_login.Login.click_model(self)
        sleep(1)
        #点击关联类型
        self.click(xpath=model.click_relevancy_type)
        # 点击新建按钮
        self.click(xpath=model.click_create_type)
        # 输入唯一标识
        self.type(css=model.relevancy_type_unique,text=model.unique_name)
        # 输入名称
        self.type(css=model.relevancy_type_name , text=model.type_name)
        # 输入源->目标描述
        self.type(css=model.target_describe,text=model.input_target_describe)
        # 输入目标->源描述
        self.type(css=model.target_source_describe,text=model.input_describe)
        # 点击提交
        self.click(xpath=model.submit)
        # 断言
        self.assertText(model.type_name)


    # 搜索不存在的关联类型
    def test_02_search_nonexistent_relevancy(self):
        # 输入不存在的关联类型名称
        self.type(css=model.relevancy_type_search,text=model.search_no_name)
        # 模拟enter键
        MyWebDriver.Keys(css=model.relevancy_type_search).enter()
        # 断言
        self.assertText(model.assert_search)

    # 搜索存在的关联类型
    def test_03_search_exist_relevancy(self):
        # 清空搜索条件
        self.click(xpath=model.clear_search_condition)
        # 输入刚新建的关系类型名称
        self.type(css=model.relevancy_type_search, text=model.type_name)
        # 模拟enter键
        MyWebDriver.Keys(css=model.relevancy_type_search).enter()
        # 断言
        self.assertText(model.type_name)

    # 编辑关联类型信息
    def test_04_edit_relevancy(self):
        # 点击编辑按钮
        self.click(xpath=model.click_edit)
        # 输入名称
        self.type(css=model.relevancy_type_name, text=model.edit_name)
        # 输入源->目标描述
        self.type(css=model.target_describe, text=model.edit_name)
        # 输入目标->源描述
        self.type(css=model.target_source_describe, text=model.edit_name)
        # 点击保存
        self.click(xpath=model.click_save)
        # 断言
        self.assertText(model.assert_search_save)

    # 删除关联类型
    def test_05_delete_relevancy(self):
        # 点击删除按钮
        self.click(xpath=model.click_delete)
        # 二次确认点击删除
        self.click(xpath=model.reconfirm_delete)
        # 断言删除成功
        self.assertNotText(model.assert_search_save)
        sleep(1)
        # 清空搜索条件
        self.click(xpath=model.clear_search_condition)
