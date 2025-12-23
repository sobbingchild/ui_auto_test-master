import seldom
from bk_user_manage.page import user_organization
from bk_user_manage.test_dir import test_01_login
class CopyName(seldom.TestCase):
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
    def test_02_copy_name(self):
        '''复制名称'''
        self.click(xpath=user_organization.Department_Option)
        self.click(xpath=user_organization.Department_CopyName)
        print(self.get_text(xpath=user_organization.Department_Copy_Message))