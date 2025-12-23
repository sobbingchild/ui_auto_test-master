import seldom
from bk_user_manage.page import user_organization
from bk_user_manage.test_dir import test_01_login

class UserClose(seldom.TestCase):
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
    def test_02_select(self):
        '''禁用用户'''
        self.click(xpath=user_organization.User_Select)
        # self.click(xpath=user_organization.User_Edit)
        self.click(xpath=user_organization.User_Close)
        print(self.get_text(xpath=user_organization.User_Close_Assert))
        if self.get_text(xpath=user_organization.User_Close_Assert) == "已禁用":
            print("禁用成功")
        else :
            print("禁用失败")
    