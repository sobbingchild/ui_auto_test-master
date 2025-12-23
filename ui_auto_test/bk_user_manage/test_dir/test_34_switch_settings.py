import seldom
from bk_user_manage.page import user_organization
from bk_user_manage.page import user_settings
from bk_user_manage.test_dir import test_01_login
import time
class SwitchSettings(seldom.TestCase):
    def test_01_switch_audit(self):
        '''切换设置'''
        test_01_login.Login.test_login(self)
        #登录
        time.sleep(8)
        self.click(xpath=user_organization.Switch_Setting)
        time.sleep(8)
        if self.get_text(xpath=user_settings.Settings_Label) == "添加字段":
            print("切换设置成功")
        else:
            print("切换设置失败")