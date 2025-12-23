from time import sleep
from bk_cmdb.page import model
import seldom

from bk_cmdb.access_test_dir import test_01_login


class ModelCreat(seldom.TestCase):
    def test_01_new_model(self):
        """创建模型"""
        # 进入首页，点击模型
        test_01_login.Login.test_login(self)
        test_01_login.Login.click_model(self)
        # 点击网络
        self.click(xpath=model.network)
        # 点击新建模型
        self.click(xpath=model.creat_model)
        # 输入新建模型的唯一标识及名称并提交
        self.type(xpath=model.unique, text=model.model_unique_text)
        self.type(xpath=model.model_name, text=model.model_name_text)
        self.click(xpath=model.commit_model_message)
        self.assertText(model.asserttext)
