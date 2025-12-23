from bk_cmdb.page import login_page, model
import seldom
from bk_cmdb.page import resource
from bk_cmdb.access_test_dir import test_01_login


class ModelDelete(seldom.TestCase):
    def test_01_delete_model(self):
        """删除模型"""
        # 进入首页，点击模型
        test_01_login.Login.test_login(self)
        # 点击模型
        self.click(css=login_page.model)
        # 搜索框输入模型名称
        self.type(xpath=model.search_model, text=model.search_model_text)
        # 点击模型
        self.click(xpath=model.click_model)
        # 点击模型旁的3个点删除
        self.click(xpath=model.click_delete_model)
        # 点击删除
        self.click(xpath=model.click_delete_mo)
        # 确定删除
        self.click(xpath=model.sure_delete_model)
        self.assertText(resource.asserttext_delete_mod)