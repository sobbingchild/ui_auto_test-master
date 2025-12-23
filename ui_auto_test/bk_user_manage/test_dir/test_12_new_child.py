import seldom
from bk_user_manage.page import user_organization
from bk_user_manage.test_dir import test_01_login
class NewChild(seldom.TestCase):
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
    def test_02_new_depart(self):
        '''新增下级组织'''
        self.click(xpath=user_organization.Department_Option)
        self.click(xpath=user_organization.Department_New_Child)
        self.type(xpath=user_organization.Child_Name_Input,text=user_organization.Child_Name)
        self.click(xpath=user_organization.Child_Confirm)
        print("创建下级组织成功,下级组织名称为:"+user_organization.Child_Name)

    def test_03_new_depart(self):
        '''新增重名下级组织'''
        self.click(xpath=user_organization.Department_Option)
        self.click(xpath=user_organization.Department_New_Child)
        self.type(xpath=user_organization.Child_Name_Input,text=user_organization.Child_Name)
        self.click(xpath=user_organization.Child_Confirm)
        # print(self.get_text(xpath=user_organization.Department_Copy_Message))
        print("新增一个名称重复的下级组织,新增失败")

    def test_04_new_depart(self):
        '''新增名称为空的下级组织'''
        self.click(xpath=user_organization.Department_Option)
        self.click(xpath=user_organization.Department_New_Child)
        self.type(xpath=user_organization.Child_Name_Input,text="")
        self.click(xpath=user_organization.Child_Confirm)
        print("新增一个名称为空的下级组织,新增失败")
        # print(self.get_text(xpath=user_organization.Department_Copy_Message))

