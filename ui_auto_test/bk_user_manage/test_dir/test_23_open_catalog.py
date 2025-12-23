import seldom
from bk_user_manage.page import user_organization
from bk_user_manage.page import user_catalog
from bk_user_manage.test_dir import test_01_login
import time

class OpenCatalog(seldom.TestCase):
    def test_01_switch_catalog(self):
        '''切换用户目录'''
        test_01_login.Login.test_login(self)
        #登录
        time.sleep(8)
        self.click(xpath=user_organization.Switch_Catalog)
        time.sleep(8)
        if self.get_text(xpath=user_catalog.New_Catalog) == "新增目录":
            print("切换用户目录成功")
        else:
            print("切换用户目录失败")
    def test_02_open_catalog(self):
        '''开启本地目录'''
        self.click(xpath=user_catalog.SwitcherButton)
        print(self.get_text(xpath=user_organization.Department_Copy_Message))
