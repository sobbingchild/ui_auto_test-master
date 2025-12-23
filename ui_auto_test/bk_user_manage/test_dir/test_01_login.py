import seldom
from bk_user_manage import settings
from bk_user_manage.page import page_login


from bk_user_manage.bk_exception import LoginError

class Login(seldom.TestCase):
    def test_login(self, username=settings.USER_NAME, pwd=settings.PASSWORD):
        ''' 登录态验证'''
        self.open(settings.USER_URL)
        self.set_window(1920, 1080)
        self.wait(3)
        if self.get_title == settings.LOGIN_TITLE_ENGLISH or self.get_title == settings.LOGIN_TITLE:
            if self.get_title == settings.LOGIN_TITLE_ENGLISH:
                # 判断是否社区版
                msg = self.get_attribute(xpath=page_login.Login_photo,attribute="src")
                if 'logo_ce' in msg:
                    self.click(xpath=page_login.switch_language_ce)
                else:
                    self.click(xpath=page_login.switch_language_ee)
                self.sleep(1)
                if self.get_title != settings.LOGIN_TITLE:
                    raise LoginError('英文切换中文失败，登录页面有缺陷')
                self.input_username_password(username=username, pwd=pwd)
            elif self.get_title == settings.LOGIN_TITLE:
                self.input_username_password(username=username, pwd=pwd)
            else:
                raise LoginError('登录页面title不符合规范,测试失败')
        else:
            self.open(settings.USER_URL)
            # self.wait(3)
            self.assertInTitle(settings.INDEX_TITLE)

    def input_username_password(self, username, pwd):
        # 输入账号
        self.type(xpath=page_login.account, text=username)
        # 输入密码
        self.type(xpath=page_login.password, text=pwd)
        self.click(xpath=page_login.login_button)
        # self.wait(1)
        if settings.INDEX_TITLE in self.get_title:
            print("登录成功")
        else:
            raise LoginError('密码账号错误，登录失败')