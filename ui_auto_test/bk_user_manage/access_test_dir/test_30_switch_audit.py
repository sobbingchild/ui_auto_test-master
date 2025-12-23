import seldom
from bk_user_manage.page import user_organization
from bk_user_manage.page import  user_audit
from bk_user_manage.access_test_dir import test_01_login
import time
class SwitchAudit(seldom.TestCase):
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