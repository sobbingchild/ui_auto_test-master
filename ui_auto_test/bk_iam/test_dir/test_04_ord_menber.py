import seldom
from bk_iam.page import ord_member as page
from bk_iam import settings as settings
import time


class OrdMenber(seldom.TestCase):
    def test_00_swich_adminuser(self):
        '''切换用户，admin切换为普通用户'''
        self.click(xpath=page.iam_name)
        self.click(xpath=page.iam_login_out)
        self.login(settings.NEW_USER, settings.NEW_PWD)

    def test_01_aply_user_g(self):
        '''非admin申请加入用户组'''
        self.click(xpath=page.perm_ply)
        self.click(xpath=page.user_g_name)
        self.click(xpath=page.textarea)
        self.type(xpath=page.textarea, text=page.resean_text)
        self.click(xpath=page.button_commit)

    def test_02_asset_status_review(self):
        '''检验审核中状态'''
        text = self.get_text(xpath=page.revoke)
        print("test_04_ord_menber.py--获取文本", text)
        if text == page.revoke_text:
            self.assertText(text)
        else:
            print("状态有误")

    def test_03_appro_userg_perm(self):
        '''切换admin审批用户组权限'''
        self.click(xpath=page.nav_appro)
        time.sleep(2)
        new_windows = self.window_handles[1]
        print("新窗口----", new_windows)
        self.switch_to_window(new_windows)
        self.click(xpath=page.itsm_name)
        time.sleep(2)
        self.move_to_element(xpath=page.loginout_itsm)
        self.click(xpath=page.loginout_itsm)
        time.sleep(2)
        self.login(settings.USER_NAME, settings.PASSWORD)
        time.sleep(2)
        self.click(xpath=page.itsm_appro_pass)
        time.sleep(1)
        self.click(xpath=page.itsm_appro_confrim, index=1)
        time.sleep(1)

    def login(self, username, pwd):
        self.delete_all_cookies()
        self.refresh()
        self.sleep(0.5)
        try:
            # 输入账号
            self.type(xpath=page.account, text=username)
            # 输入密码
            self.type(xpath=page.password, text=pwd)
            self.click(xpath=page.login_btn)
            time.sleep(3)
        except BaseException as e:
            print("登录失败", e)
