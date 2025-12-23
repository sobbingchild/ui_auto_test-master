# import re
#
# from public_method.login import LoginBase
# from product_page.bk_monitor import home
# from product_page.bk_monitor import integrations_collection as integ_home
# from product_page.bk_monitor import integrations_custom as custom
# from public_method.base_operate import BaseOperate
# from product_page import settings
# BaseOperate = BaseOperate()
#
# class IntegrationsEvent(LoginBase):
#     '''自定义事件'''
#     # def test_01_metrics_event(self):
#     #     '''自定义事件检查'''
#     #     self.open(settings.MONITOR_URL)
#     #     self.my_click(element=home.plugin_manager_navigation)
#     #     self.my_click(element=integ_home.events_navigation)
#     #     self.my_click(element=custom.check_metrics)
#     #     self.check_page_error()
#     #     self.assertText("事件列表")
#     #     self.sleep(2)
#     #     data_id = self.my_get_text(element=custom.metrics_data_id)
#     #     pattern = re.compile(r'^\d+$')
#     #     self.assertTrue(pattern.match(data_id) is not None, "数据ID的值不正确")
#     #     self.assertText("自定义事件帮助")
#     #     self.sleep(2)
#
#     def test_01_create_Metrics(self):
#         '''新建自定义事件'''
#         self.open(settings.MONITOR_URL)
#         self.my_click(element=home.plugin_manager_navigation)
#         self.my_click(element=integ_home.events_navigation)
#         self.my_click(element=custom.create_metrics)
#         name = BaseOperate.random_data()
#         settings.events_name = name
#         self.my_type(element=custom.create_event_en_name, text=name)
#         self.my_type(element=custom.create_event_data_name, text=name)
#         self.my_click(element=custom.create_monitor_layer)
#         self.my_click(element=custom.create_monitor_layer_name)
#         self.my_click(element=custom.create_submit)
#         for i in range(10):
#             try:
#                 self.assertText("创建成功")
#                 break
#             except:
#                 pass
#         self.sleep(1)
#         data_id = self.my_get_text(element=custom.metrics_data_id)
#         pattern = re.compile(r'^\d+$')
#         self.assertTrue(pattern.match(data_id) is not None, "数据ID的值不正确")
#         self.my_click(element=home.home_back)
#
#     def test_02_check_Metrics(self):
#         '''查看自定义事件'''
#         self.my_click(element=integ_home.events_navigation)
#         self.my_click(element=custom.check_metrics)
#         self.check_page_error()
#         self.assertText("事件列表")
#         self.sleep(2)
#         data_id = self.my_get_text(element=custom.metrics_data_id)
#         pattern = re.compile(r'^\d+$')
#         self.assertTrue(pattern.match(data_id) is not None, "数据ID的值不正确")
#         self.assertText("自定义事件帮助")
#         self.sleep(2)
#
#     def test_03_del_metrics(self):
#         '''删除新建的自定义事件'''
#         self.my_click(element=integ_home.events_navigation)
#         self.my_click(element=custom.metrics_search)
#         self.my_type(element=custom.metrics_search, text=settings.events_name)
#         self.Keys(xpath=custom.metrics_search['path']).enter()
#         self.my_click(element=custom.metrics_del)
#         self.my_click(element=custom.metrics_del_confirm)
#         self.assertText("删除成功")
#         self.assertText("搜索结果为空")
#         self.sleep(2)
#
#
#
#
#
#
#
#
#
