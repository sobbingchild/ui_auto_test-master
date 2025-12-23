import seldom
from bk_paasv3.test_dir import test_01_login
from bk_paasv3.page import application_development
from public_method.keyboard_operation import MyWebDriver

class Advanced_Filter(seldom.TestCase):
    def test_01_advanced_filter(self):
        """查看更多应用"""
        # 进入首页
        test_01_login.Login.test_login(self)
        # 点击查看更多应用
        self.click(xpath=application_development.more_application)
        # 断言
        self.assertText(application_development.assert_application)
        # 搜索框输入配置平台
        self.type(xpath=application_development.search_application,text=application_development.search_txt)
        # 模拟enter键
        MyWebDriver.Keys(xpath=application_development.search_application).enter()
        self.is_visible(5,xpath=application_development.is_search_success)