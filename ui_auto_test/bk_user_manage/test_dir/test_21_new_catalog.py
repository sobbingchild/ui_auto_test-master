import seldom
from bk_user_manage import settings
from bk_user_manage.page import user_organization
from bk_user_manage.page import user_catalog
from bk_user_manage.test_dir import test_01_login
import time
class NewCatalog(seldom.TestCase):
    def test_01_switch_catalog(self):
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
        """新增本地目录"""
        self.click(xpath=user_catalog.New_Catalog)
        self.click(xpath=user_catalog.Local_Catalog)
        self.click(xpath=user_catalog.NewCatalogConfirm)
        self.type(xpath=user_catalog.LocalCatalog_Name,text=user_catalog.LocalCatalogName)
        self.type(xpath=user_catalog.LocalCatalog_Domain,text=settings.Name_3)
        print("目录名称为:"+user_catalog.LocalCatalogName)
        print("登录域为:"+settings.Name_3)
        print("基础设置填写完成")
        self.click(xpath=user_catalog.LocalCatalog_Confirm)
        time.sleep(3)
        self.click(xpath=user_catalog.Account_Confirm)
    def test_03_input_Password(self):
        '''填入本地目录信息'''
        print("设置密码最短长度为8")
        self.click(xpath=user_catalog.Password_Special)
        print("密码支持小写字母,大写字母,数字,特殊字符")
        self.click(xpath=user_catalog.Date_6Month)
        print("密码有效期为:"+self.get_text(xpath=user_catalog.Date_6Month))
        self.click(xpath=user_catalog.Error_5Times)
        print("密码错误次数:"+self.get_text(xpath=user_catalog.Error_5Times))
        print("自动解锁时间:600")
        # self.click(xpath=user_catalog.Email_Password)
        # self.click(xpath=user_catalog.Random_Password)
        print("邮箱发送密码")
        self.click(xpath=user_catalog.Password_Submit)
        print(self.get_text(xpath=user_organization.Department_Copy_Message))

    def test_04_renew_catalog(self):
        """登录域重名新增本地目录"""
        self.click(xpath=user_catalog.New_Catalog)
        self.click(xpath=user_catalog.Local_Catalog)
        self.click(xpath=user_catalog.NewCatalogConfirm)
        self.type(xpath=user_catalog.LocalCatalog_Name,text=user_catalog.LocalCatalogName+"2")
        self.type(xpath=user_catalog.LocalCatalog_Domain,text=settings.Name_3)
        print("目录名称为:"+user_catalog.LocalCatalogName)
        print("登录域为:"+settings.Name_3)
        print("基础设置填写完成")
        self.click(xpath=user_catalog.LocalCatalog_Confirm)
        print(self.get_text(xpath=user_organization.Department_Copy_Message))