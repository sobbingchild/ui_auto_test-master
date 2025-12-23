import seldom
from bk_user_manage import settings
from bk_user_manage.page import user_organization
from bk_user_manage.test_dir import test_01_login


class NewUserChild(seldom.TestCase):
    def test_01_switch(self):
        '''切换副组织'''
        test_01_login.Login.test_login(self)
        #登录
        self.click(xpath=user_organization.DepartmentName2)
        #切换到第三组织
        if self.get_text(xpath=user_organization.Department_Name) == user_organization.Department_Name_2_Input:
            print("切换组织成功")
            print("组织名称"+self.get_text(xpath=user_organization.Department_Name))
        else:
            print("切换组织失败")
    def test_02_new_user(self,UserName=settings.Child_Name,AllName='你好测试',Email='123@qq.com',Number='13312312322'):
        '''新增副组织用户'''
        # self.click(xpath=user_organization.New_User_First)
        self.click(xpath=user_organization.New_User_Step1)
        self.click(xpath=user_organization.New_User_Step2)
        self.type(xpath=user_organization.User_Name,text=UserName)
        self.type(xpath=user_organization.User_AllName,text=AllName)
        self.type(xpath=user_organization.User_Email,text=Email)
        self.type(xpath=user_organization.User_Number,text=Number)
        self.click(xpath=user_organization.User_Date)
        self.click(xpath=user_organization.Date_NextYear)
        self.click(xpath=user_organization.Date_Select)
        self.click(xpath=user_organization.Button_Save)
        print(settings.Child_Name +"用户创建成功")