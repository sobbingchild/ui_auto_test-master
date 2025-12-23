import seldom
from bk_user_manage.page import user_organization
from bk_user_manage.page import  user_audit
from bk_user_manage.test_dir import test_01_login
import time
class LoginAudit(seldom.TestCase):
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
    def test_02_audit_search(self):
        '''操作审计搜索用户'''
        self.type_enter(xpath=user_audit.Search_User,text='admin')
        '''筛选结果'''
        if self.get_text(xpath=user_audit.Search_First_User) == 'admin':
            print("操作审计筛选成功")
        else:
            print("操作审计筛选失败")

    def test_03_switch_login(self):
        '''切换登录审计'''
        self.click(xpath=user_audit.Switch_Login)
        if self.get_text(xpath=user_audit.Login_Table) == '登录用户':
            print("切换登录审计成功")
        else:
            print("切换登录审计失败")
