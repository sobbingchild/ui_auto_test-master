import seldom
import time
from bk_user_manage.page import user_organization
from bk_user_manage.test_dir import test_01_login


class SearchOrg(seldom.TestCase):
    def test_01_switch(self):
        '''搜索切换指定组织'''
        test_01_login.Login.test_login(self)
        #登录
        '''搜索并切换至指定组织'''
        self.type(xpath=user_organization.Department_Search,text=user_organization.Department_Name_Input)
        time.sleep(3)
        self.click(xpath=user_organization.Department_Result)
        time.sleep(5)
        self.click(xpath=user_organization.Department_Result_Switch)
        #切换到第三组织
        if self.get_text(xpath=user_organization.Department_Name) == user_organization.Department_Name_Input:
            print("切换组织成功")
            print("组织名称"+self.get_text(xpath=user_organization.Department_Name))
        else:
            print("切换组织失败")

