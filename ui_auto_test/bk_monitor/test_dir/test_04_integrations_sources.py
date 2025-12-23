# from public_method.login import LoginBase
# from product_page.bk_monitor import home
# from product_page.bk_monitor import integrations_collection as integ_home
# from public_method.base_operate import BaseOperate
# from product_page import settings
# BaseOperate = BaseOperate()
#
# class IntegrationsSources(LoginBase):
#     '''告警源'''
#     def test_01_sources_click(self):
#         """进入告警源页面检查"""
#         self.open(settings.MONITOR_URL)
#         self.my_click(element=home.plugin_manager_navigation)
#         self.my_click(element=integ_home.sources_navigation)
#         self.check_page_error()
#         self.assertText("Zabbix")
#         self.assertText("腾讯云告警拉取")
