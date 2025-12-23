import seldom
from bk_user_manage.page import user_organization
from bk_user_manage.test_dir import test_01_login
import time
from bk_user_manage import settings
class PullUser(seldom.TestCase):
    def test_01_switch(self):
        test_01_login.Login.test_login(self)
        #登录
        self.click(xpath=user_organization.DepartmentName)
        #切换到第三组织
        if self.get_text(xpath=user_organization.Department_Name) == user_organization.Department_Name_Input:
            print("切换组织成功")
            print("组织名称"+self.get_text(xpath=user_organization.Department_Name))
        else:
            print("切换组织失败")
    def test_02_pull(self):
        '''从副组织拉取副组织用户'''
        self.click(xpath=user_organization.New_User_Step1)
        self.click(xpath=user_organization.New_User_Step3)
        #从其他组织拉取
        time.sleep(1)
        self.click(xpath=user_organization.Pull_User_Name)
        self.type_enter(xpath=user_organization.Pull_User_Name_Search,text=settings.Child_Name)
        time.sleep(3)
        self.click(xpath=user_organization.Pull_User_Name)
        time.sleep(3)
        self.click(xpath=user_organization.Pull_User_Name)
        self.type_enter(xpath=user_organization.Pull_User_Name_Search,text=settings.Child_Name)
        time.sleep(10)
        if self.get_text(xpath=user_organization.Pull_User_Name_Select) == settings.Child_Name:
            self.click(xpath=user_organization.Pull_User_Name_Select)
            self.click(xpath=user_organization.Pull_Close_Down)
            self.click(xpath=user_organization.Pull_Confirm)
            print("从其它组织拉取用户成功")
        else:
            print("搜索失败")
    def test_03_remove(self):
        '''从主组织移除副组织用户'''
        time.sleep(1)
        self.click(xpath=user_organization.Search_User)
        self.click(xpath=user_organization.Search_User_List)
        self.type_enter(xpath=user_organization.Search_User, text=settings.Child_Name)
        self.click(xpath=user_organization.Check_User)
        print("搜索用户成功")
        self.click(xpath=user_organization.User_MoreOption)
        self.click(xpath=user_organization.User_Org)
        time.sleep(3)
        self.click(xpath=user_organization.User_RemoveOrg)
        time.sleep(3)
        self.click(xpath=user_organization.Pull_Confirm)
        time.sleep(3)
        print("设置用户组织且移除成功")
