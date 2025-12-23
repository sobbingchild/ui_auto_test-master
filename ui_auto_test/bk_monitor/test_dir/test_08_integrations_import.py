# import re
#
# from public_method.login import LoginBase
# from product_page.bk_monitor import home
# from product_page.bk_monitor import integrations_collection as integ_home
# from product_page.bk_monitor import observations_k8s as kub
# from public_method.base_operate import BaseOperate
# from product_page import settings
# BaseOperate = BaseOperate()
#
# class IntegrationsImport(LoginBase):
#     '''导入导出'''
#     def test_01_metrics_event(self):
#         '''导入导出页面检查'''
#         self.open(settings.MONITOR_URL)
#         self.my_click(element=home.plugin_manager_navigation)
#         self.my_click(element=integ_home.import_navigation)
#         self.check_page_error()
#         self.assertText("导入历史")
#         self.sleep(2)
#
#     # def test_01_metrics_event(self):
#     #     '''导入导出页面检查'''
#     #     self.open(settings.MONITOR_URL)
#     #     self.my_click(element=home.performance_navigation)
#     #     self.my_click(element=kub.kub_kubernetes)
#     #     self.check_page_error()
#     #     self.assertText("导入历史")
#     #     self.sleep(2)
#
#
#
#
#
#
#
#
