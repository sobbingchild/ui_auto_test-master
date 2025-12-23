import seldom
from bk_user_manage.page import user_organization
from bk_user_manage.access_test_dir import test_01_login
class RenameChild(seldom.TestCase):
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
    def test_02_rename(self):
        '''重命名下级组织'''
        self.click(xpath=user_organization.Child_Position)
        self.click(xpath=user_organization.Department_Option)
        self.click(xpath=user_organization.Department_Rename)
        self.clear(xpath=user_organization.Department_Rename_Input)
        self.type(xpath=user_organization.Department_Rename_Input,text=user_organization.Child_Name2)
        self.click(xpath=user_organization.Rename_Confirm)
        print(self.get_text(xpath=user_organization.Department_Copy_Message))
        print("下级组织重命名成功,名称为"+user_organization.Child_Name2)




