
from bk_nodeman import settings
from bk_nodeman.page import login_page
from bk_nodeman.bk_exception import LoginError
from bk_nodeman.base_operate import BaseOperate

base = BaseOperate()

def test_login_assert(self, NODEMAN_URL):
    ''' 登录态验证'''
    self.open(NODEMAN_URL)
    self.max_window()
    if self.get_title == settings.LOGIN_TITLE_ENGLISH or self.get_title == settings.LOGIN_TITLE:
        if self.get_title == settings.LOGIN_TITLE_ENGLISH:
            # 判断是否社区版
            msg = self.get_attribute(xpath='//div[@class="logo-title"]/img', attribute="src")
            print(msg)
            if 'logo_ce' in msg:
                self.click(xpath=login_page.switch_language_ce)
            else:
                self.click(xpath=login_page.switch_language_ee)
            self.sleep(1)
            if self.get_title != settings.LOGIN_TITLE:
                raise LoginError('英文切换中文失败，登录页面有缺陷')
            # 输入账号
            self.type(xpath=login_page.account, text=settings.USER_NAME)
            # 输入密码
            self.type(xpath=login_page.password, text=settings.PASSWORD)
            self.click(xpath=login_page.login_button)
            self.sleep(1)
            if settings.INDEX_TITLE in self.get_title:
                pass
            else:
                raise LoginError('密码账号错误，登录失败')
        elif self.get_title == settings.LOGIN_TITLE:
            # 输入账号
            self.type(xpath=login_page.account, text=settings.USER_NAME)
            # 输入密码
            self.type(xpath=login_page.password, text=settings.PASSWORD)
            self.click(xpath=login_page.login_button)
            self.sleep(1)
            if settings.INDEX_TITLE in self.get_title:
                pass
            else:
                raise LoginError('密码账号错误，登录失败')
        else:
            raise LoginError('登录页面title不符合规范,测试失败')
    else:
        self.open(NODEMAN_URL)
        self.assertInTitle(settings.INDEX_TITLE)
        self.sleep(1)