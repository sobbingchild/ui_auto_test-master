import seldom
from bk_user_manage.page import user_organization
from bk_user_manage.page import  user_audit
from bk_user_manage.access_test_dir import test_01_login
import time
class AuditTime(seldom.TestCase):
    def test_01_switch_audit(self):
        '''切换审计'''
        test_01_login.Login.test_login(self)
        #登录
        time.sleep(8)
        self.click(xpath=user_organization.Switch_Audit)
        time.sleep(8)
        if self.get_text(xpath=user_audit.Audit_Label) == "操作审计":
            print("切换审计成功")
        else:
            print("切换审计失败")
    def test_02_time_input(self):
        '''选择时间'''
        self.click(xpath=user_audit.Time_Button)
        if self.get_text(xpath=user_audit.Select_Button) == '选择时间':
            print("选择时间界面显示成功")
        else:
            print("选择时间界面显示失败")
    def test_03_select_yesterday(self):
        '''选择昨天'''
        self.click(xpath=user_audit.Time_Button)
        self.click(xpath=user_audit.Select_Yesterday)
        self.click(xpath=user_audit.Select_Confirm)
        print("选择日期范围为昨天")
    def test_04_user_assert(self):
        '''筛选结果'''
        if self.get_text(xpath=user_audit.Search_First_User) == 'admin':
            print("操作审计筛选成功")
        else:
            print("操作审计筛选失败")