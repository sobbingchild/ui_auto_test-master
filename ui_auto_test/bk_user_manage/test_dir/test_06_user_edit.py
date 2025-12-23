import time

import seldom
from bk_user_manage.page import user_organization
from bk_user_manage.test_dir import test_01_login

class UserEdit(seldom.TestCase):
    def test_01_switch(self):
        '''切换组织'''
        test_01_login.Login.test_login(self)
        #登录
        self.click(xpath=user_organization.DepartmentName)
        #切换到第2组织
        if self.get_text(xpath=user_organization.Department_Name) == user_organization.Department_Name_Input:
            print("切换组织成功")
            print(self.get_text(xpath=user_organization.Department_Name))
        else:
            print("切换组织失败")
    def test_02_edit(self,AllName='修改全名',Email='66@qq.com'):
        '''编辑一个用户的名称'''
        self.click(xpath=user_organization.User_Select)

        self.click(xpath=user_organization.User_Reset_Password)
        self.type(xpath=user_organization.User_Reset_Input,text='Aa123456')
        self.click(xpath=user_organization.Reset_Confirm)
        print(self.get_text(xpath=user_organization.Department_Copy_Message))
        self.click(xpath=user_organization.User_Edit)
        self.clear(xpath=user_organization.User_AllName)
        self.type(xpath=user_organization.User_AllName,text=AllName)
        self.clear(xpath=user_organization.User_Email)
        self.type(xpath=user_organization.User_Email,text=Email)
        self.click(xpath=user_organization.Button_Save)
        print("编辑成功")