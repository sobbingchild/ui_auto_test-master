# from time import sleep
# import seldom
# from bk_cmdb import settings
# from bk_cmdb.page import homepage, business
# from bk_cmdb.test_dir import test_01_login
# from public_method.keyboard_operation import MyWebDriver
#
#
# class TextSearch(seldom.TestCase):
#     def test_01_business_textsearch(self):
#         """根据业务关键字搜索业务（全文检索）"""
#         test_01_login.Login.test_login(self)
#         # 点击资源
#         test_01_login.Login.click_business(self)
#         # 等待后输入业务名并点击
#         sleep(1)
#         # 默认进入蓝鲸业务，点击公共组件
#         self.click(xpath=business.common_components)
#         # 获取公共组件的IP值
#         global BluekingHostIp
#         BluekingHostIp = self.get_text(xpath=business.get_host)
#         print(BluekingHostIp)
#         test_01_login.Login.click_homepage(self)
#         # 点击全文检索
#         self.click(css=homepage.textsearch)
#         sleep(1)
#         # 输入BUSINESS进行搜索（业务关键字），搜索
#         self.type(css=homepage.index_text_search, text=settings.BUSINESS_KEY)
#         self.click(css=homepage.index_button_search)
#         self.assertText(settings.BUSINESS_KEY_ASSERT)
#
#     def test_02_model_textsearch(self):
#         """根据模型关键字搜索模型（全文检索）"""
#         # 清除关键字
#         MyWebDriver.Keys(css=homepage.index_text_search).backspace()
#         MyWebDriver.Keys(css=homepage.index_text_search).backspace()
#         # 输入模型进行搜索（模型关键字），搜索
#         self.type(css=homepage.index_text_search, text=settings.MODEL_KEY)
#         self.click(css=homepage.index_button_search)
#         self.assertText(settings.MODEL_KEY_ASSERT)
#
#     def test_03_host_textsearch(self):
#         """根据存在的主机IP搜索主机（全文检索）"""
#         # 清除关键字
#         MyWebDriver.Keys(css=homepage.index_text_search).backspace()
#         MyWebDriver.Keys(css=homepage.index_text_search).backspace()
#         # 输入模型实例进行搜索（模型实例关键字）及根据主机IP搜索主机（主机关键字）
#         self.type(css=homepage.index_text_search, text=BluekingHostIp)
#         sleep(1)
#         # 搜索
#         self.click(css=homepage.index_button_search)
#         self.assertText(settings.HOST_ASSERT + BluekingHostIp)
