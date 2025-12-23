import seldom
from bk_user_manage.page import user_organization
from bk_user_manage.test_dir import test_01_login


class NewOrg(seldom.TestCase):
    def test_01_new_depart(self):
        '''新增主组织'''
        test_01_login.Login.test_login(self)
        # 登录

        self.click(xpath=user_organization.Main_Option)
        self.click(xpath=user_organization.Main_New_Org)
        self.type_enter(xpath=user_organization.New_Department, text=user_organization.Department_Name_Input)
        if self.get_text(xpath=user_organization.Department_Name) == user_organization.Department_Name_Input:
            print("新建组织成功")
            print("组织名称" + self.get_text(xpath=user_organization.Department_Name))
        else:
            print("新建组织失败")
