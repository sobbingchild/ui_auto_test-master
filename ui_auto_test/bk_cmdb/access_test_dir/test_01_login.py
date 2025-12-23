import seldom
from bk_cmdb import settings
from bk_cmdb.page import login_page
from bk_cmdb.bk_exception import LoginError


class Login(seldom.TestCase):
    def test_login(self, username=settings.USER_NAME, pwd=settings.PASSWORD):
        ''' 登录态验证'''
        self.open(settings.CMDB_URL)
        self.max_window()
        if self.get_title == settings.LOGIN_TITLE_ENGLISH or self.get_title == settings.LOGIN_TITLE:
            if self.get_title == settings.LOGIN_TITLE_ENGLISH:
                # 判断是否社区版
                msg = self.get_attribute(xpath='//div[@class="logo-title"]/img', attribute="src")
                if 'logo_ce' in msg:
                    self.click(xpath=login_page.switch_language_ce)
                else:
                    self.click(xpath=login_page.switch_language_ee)
                self.sleep(1)
                if self.get_title != settings.LOGIN_TITLE:
                    raise LoginError('英文切换中文失败，登录页面有缺陷')
                # 输入账号
                self.type(xpath=login_page.account, text=username)
                # 输入密码
                self.type(xpath=login_page.password, text=pwd)
                self.click(xpath=login_page.login_button)
                self.sleep(1)
                if settings.INDEX_TITLE in self.get_title:
                    print("登录成功")
                    print(msg)
                else:
                    raise LoginError('密码账号错误，登录失败')
            elif self.get_title == settings.LOGIN_TITLE:
                # 输入账号
                self.type(xpath=login_page.account, text=username)
                # 输入密码
                self.type(xpath=login_page.password, text=pwd)
                self.click(xpath=login_page.login_button)
                self.sleep(1)
                if settings.INDEX_TITLE in self.get_title:
                    print("登录成功")
                else:
                    raise LoginError('密码账号错误，登录失败')
            else:
                raise LoginError('登录页面title不符合规范,测试失败')
        else:
            self.open(settings.CMDB_URL)
            self.assertInTitle(settings.INDEX_TITLE)

    # 点击首页
    def click_homepage(self):
        self.click(css=login_page.homepage)

    # 点击business
    def click_business(self):
        self.click(css=login_page.business)

    # 点击资源
    def click_resource(self):
        self.click(css=login_page.resource)

    # 点击模型
    def click_model(self):
        self.click(css=login_page.model)
