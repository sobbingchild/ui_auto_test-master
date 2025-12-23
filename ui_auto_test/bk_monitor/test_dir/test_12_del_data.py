# from public_method.login import LoginBase
# from product_page.bk_monitor import home
# from product_page.bk_monitor import alert_rules as alert
# from public_method.base_operate import BaseOperate
# from product_page import settings
# from product_page.bk_monitor import integrations_collection as integ_home
# BaseOperate = BaseOperate()
#
# class DelData(LoginBase):
#     '''检查告警及数据采集，删除新建数据'''
#     def test_01_del_alert(self):
#         '''删除新建的告警策略'''
#         self.open(settings.MONITOR_URL)
#         self.my_click(element=home.strategy_config_navigation)
#         self.my_click(element=alert.alert_rules)
#         self.sleep(2)
#         self.my_click(element=alert.alert_rules_search)
#         try:
#             element = self.get_element(xpath=alert.alert_rules_search['path'])
#             self.execute_script(f"arguments[0].innerText = '{settings.alert_name}';", element)
#             # 触发 input 事件，让输入框更新状态
#             self.execute_script("""
#                                 var event = new Event('input', {
#                                     'bubbles': true,
#                                     'cancelable': true
#                                 });
#                                 arguments[0].dispatchEvent(event);
#                             """, element)
#             self.my_click(element=alert.alert_rules_search_name)
#             self.my_click(element=alert.alert_rules_search_icon)
#         except Exception as e:
#             print(e)
#         self.assertText("共计1条")
#         self.my_click(element=home.list_more)
#         self.my_click(element=alert.alert_event_more_button_del)
#         self.my_click(element=alert.alert_event_del_confirm)
#         self.assertText("删除成功")
#         self.assertText("搜索结果为空")
#
#     def test_02_check_collection(self):
#         '''查看新建数据采集是否有上报数据'''
#         self.open(settings.MONITOR_URL)
#         self.my_click(element=home.plugin_manager_navigation)
#         self.my_click(element=integ_home.collection_navigation)
#         self.my_click(element=integ_home.collection_search)
#         self.my_type(element=integ_home.collection_search, text=settings.collection_name)
#         self.Keys(xpath=integ_home.collection_search['path']).enter()
#         self.my_click(element=integ_home.collection_name_click)
#         self.my_click(element=integ_home.collection_link_state)
#         self.assertText("查看上报数据")
#         self.my_click(home.home_back)
#
#
#     def test_03_del_collection(self):
#         '''删除数据采集'''
#         self.my_click(element=integ_home.collection_navigation)
#         self.my_click(element=integ_home.collection_search)
#         self.my_type(element=integ_home.collection_search, text=settings.collection_name)
#         self.Keys(xpath=integ_home.collection_search['path']).enter()
#         self.my_click(element=home.list_more)
#         self.my_click(element=integ_home.collection_more_del)
#         self.my_click(element=integ_home.collection_more_del_confirm)
#         self.sleep(5)
#         self.assertText("删除完成")
#
#
