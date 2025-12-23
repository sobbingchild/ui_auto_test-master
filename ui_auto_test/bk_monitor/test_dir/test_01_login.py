import seldom
from product_page import settings
from public_method.login import LoginBase


class Login(LoginBase):
    '''登录'''
    def test_login(self):
        ''' 登录态验证'''
        if 'woa' not in settings.MONITOR_URL:
            self._test_login(target_url=settings.MONITOR_URL, index_title=settings.INDEX_TITLE)
        else:
            self._test_woa_login(target_url=settings.MONITOR_URL, index_title=settings.MONITOR_TITLE)