import seldom
from bk_user_manage import settings
from bk_user_manage.page import user_organization
from bk_user_manage.page import user_catalog
from bk_user_manage.test_dir import test_01_login
import time
class NewMicrosoft(seldom.TestCase):
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
    def test_02_new_catalog(self):
        '''新增Microsoft Active Directory'''
        self.click(xpath=user_catalog.New_Catalog)
        self.click(xpath=user_catalog.Microsoft_Catalog)
        self.click(xpath=user_catalog.NewCatalogConfirm)
        self.type(xpath=user_catalog.LocalCatalog_Name,text=user_catalog.LocalCatalogName)
        self.type(xpath=user_catalog.LocalCatalog_Domain,text=settings.Name_4)
        print("目录名称为:"+user_catalog.LocalCatalogName)
        print("登录域为:"+settings.Name_4)
        print("基础设置填写完成")
        self.click(xpath=user_catalog.LocalCatalog_Confirm)
    def test_03_username(self):
        print("跳转至连接设置成功")
        time.sleep(5)
        self.click(xpath=user_catalog.M_King_Input)
        self.clear(xpath=user_catalog.M_King_Input)
        time.sleep(5)
        self.type(xpath=user_catalog.M_King_Input,text=user_catalog.M_King_Url)
        self.type(xpath=user_catalog.M_BaseDN,text=user_catalog.M_BaseDN_Input)
        self.type(xpath=user_catalog.M_Username,text=user_catalog.M_Username_Input)
        self.type(xpath=user_catalog.M_Password,text=user_catalog.M_Password_Input)
        self.click(xpath=user_catalog.M_Nextstep)
    def test_04_commit(self):
        '''提交'''
        print("跳转至字段配置成功")
        self.type(xpath=user_catalog.M_Agent,text=user_catalog.M_Agent_Name)
        self.click(xpath=user_catalog.M_Commit)
        print("新建Microsoft类型目录成功")
        print(self.get_text(xpath=user_organization.Department_Copy_Message))