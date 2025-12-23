import seldom
from bk_user_manage.page import user_organization
from bk_user_manage.page import user_catalog
from bk_user_manage.test_dir import test_01_login
import time
class EditLDAP(seldom.TestCase):
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
    def test_02_select_catalog(self):
        '''选择目录'''
        self.click(xpath=user_catalog.EditButton)
        print("进入目录编辑界面成功")
    def test_03_edit_catalog(self):
        '''编辑LDAP目录'''
        self.type(xpath=user_catalog.LocalCatalog_Name,text="修改目录名称")
        self.click(xpath=user_catalog.Base_Settings)
        self.type(xpath=user_catalog.M_BaseDN,text="修改根目录")
        self.click(xpath=user_catalog.Index_Settings)
        self.click(xpath=user_catalog.SaveButton3)
        print(self.get_text(xpath=user_organization.Department_Copy_Message))
        print("修改成功")
