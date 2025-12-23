import seldom
from bk_user_manage.page import user_organization
from bk_user_manage.test_dir import test_01_login
class DeleteUserChild(seldom.TestCase):
    def test_01_switch(self):
        test_01_login.Login.test_login(self)
        #登录
        self.click(xpath=user_organization.DepartmentName2)
        #切换到第三组织
        if self.get_text(xpath=user_organization.Department_Name) == user_organization.Department_Name_Input+"新":
            print("切换组织成功")
            print("组织名称"+self.get_text(xpath=user_organization.Department_Name))
        else:
            print("切换组织失败")
    def test_02_delete(self):
        '''删除副组织用户'''
        self.click(xpath=user_organization.Check_User)
        self.click(xpath=user_organization.User_MoreOption)
        self.click(xpath=user_organization.All_Delete)
        self.click(xpath=user_organization.Delete_Confirm)
        print("用户删除成功")
