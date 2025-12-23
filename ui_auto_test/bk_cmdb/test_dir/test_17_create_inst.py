from time import sleep
import seldom

from bk_cmdb.page import resource
from bk_cmdb.test_dir import test_01_login

from bk_cmdb.page import model

class InstCreat(seldom.TestCase):
    def test_01_creat_inst(self):
        """创建实例、删除实例"""
        # 进入首页，点击模型
        test_01_login.Login.test_login(self)
        # 点击资源
        test_01_login.Login.click_resource(self)
        # 搜索框输入新建的模型(跟准入用例模型名一致)
        self.type(xpath=resource.search, text=model.model_name_text)
        sleep(1)
        # 点击测试模型
        self.click(xpath=resource.click_model)
        # 新建实例
        self.click(xpath=resource.creat_inst)
        # 输入实例名并提交
        self.type(xpath=resource.inst_name, text=resource.inst_name_text)
        self.click(xpath=resource.commit_inst)
        self.assertText(resource.asserttext_creat)
        sleep(1)
        # 删除实例
        self.click(xpath=resource.delete_inst)
        # 确定删除实例
        self.click(xpath=resource.sure_delete_inst)
        self.assertText(resource.asserttext_delete)
