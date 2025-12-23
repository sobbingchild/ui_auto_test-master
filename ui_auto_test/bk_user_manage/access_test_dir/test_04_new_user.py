import seldom
from bk_user_manage import settings
from bk_user_manage.page import user_organization
from bk_user_manage.access_test_dir import test_01_login

class NewUser(seldom.TestCase):
    def test_01_switch(self):
        '''切换至主组织'''
        test_01_login.Login.test_login(self)
        # 登录

        self.click(xpath=user_organization.DepartmentName)
        #切换到第三组织
        if self.get_text(xpath=user_organization.Department_Name) == user_organization.Department_Name_Input:
            print("切换组织成功")
            print("组织名称"+self.get_text(xpath=user_organization.Department_Name))
        else:
            print("切换组织失败")
    def test_02_Collapse(self):
        '''折叠目录'''
        self.click(xpath=user_organization.DepartmentName)
    def test_03_new_user(self,UserName=settings.Name_1,AllName='你好测试',Email='123@qq.com',Number='13312312322'):
        '''新增第一个用户'''
        self.click(xpath=user_organization.New_User_Step1)
        self.click(xpath=user_organization.New_User_Step2)
        self.type(xpath=user_organization.User_Name,text=UserName)
        self.type(xpath=user_organization.User_AllName,text=AllName)
        self.type(xpath=user_organization.User_Email,text=Email)
        self.type(xpath=user_organization.User_Number,text=Number)
        # self.click(xpath=user_organization.User_Date)
        # self.click(xpath=user_organization.Date_NextYear)
        # self.click(xpath=user_organization.Date_Select)
        self.click(xpath=user_organization.Button_Save)
        print(settings.Name_1 +"用户创建成功")
    def test_04_second_user(self,UserName=settings.Name_2,AllName='你好测试1',Email='1231@qq.com',Number='13312312322'):
        '''新增第二个用户'''
        self.click(xpath=user_organization.New_User_Step1)
        self.click(xpath=user_organization.New_User_Step2)
        self.type(xpath=user_organization.User_Name,text=UserName)
        self.type(xpath=user_organization.User_AllName,text=AllName)
        self.type(xpath=user_organization.User_Email,text=Email)
        self.type(xpath=user_organization.User_Number,text=Number)
        # self.click(xpath=user_organization.User_Date)
        # self.click(xpath=user_organization.Date_NextYear)
        # self.click(xpath=user_organization.Date_Select)
        self.click(xpath=user_organization.Button_Save)
        print(settings.Name_2 +"用户创建成功")