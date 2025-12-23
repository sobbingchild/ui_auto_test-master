# from public_method.login import LoginBase
# from product_page.bk_monitor import home
# from product_page.bk_monitor import alarm_routing as routing
# from public_method.base_operate import BaseOperate
# from product_page import settings
# BaseOperate = BaseOperate()
#
# class AlertRouting(LoginBase):
#     '''告警分派'''
#     def test_01_create_routing(self):
#         '''创建告警分派'''
#         self.open(settings.MONITOR_URL)
#         self.my_click(home.strategy_config_navigation)
#         self.my_click(element=routing.alert_routing)
#         self.check_page_error()
#         self.my_click(element=routing.alert_create_routing)
#         name = BaseOperate.random_data()
#         settings.routing_name = name
#         self.my_click(element=routing.alert_routing_name)
#         self.my_type(element=routing.alert_routing_name, text=name)
#         self.my_click(element=home.home_del_confirm)
#         self.assertText("创建成功")
#
#     def test_02_config_routing(self):
#         '''配置创建的告警分派'''
#         self.sleep(2)
#         self.my_click(element=routing.alert_routing_team)
#         self.my_click(element=routing.alert_routing_team_search)
#         self.my_type(element=routing.alert_routing_team_search, text="lunck")
#         self.Keys(xpath=routing.alert_routing_team_search['path']).enter()
#         self.my_click(element=routing.alert_routing_match_rule)
#         self.my_click(element=routing.alert_routing_match_rule_search)
#         self.my_type(element=routing.alert_routing_match_rule_search, text="策略")
#         self.sleep(1)
#         self.my_click(element=routing.alert_routing_match_rule_name)
#         self.sleep(1)
#         self.my_click(element=routing.alert_routing_match_rule_condition)
#         self.my_click(element=routing.alert_routing_match_rule_value_search)
#         self.my_type(element=routing.alert_routing_match_rule_value_search, text="edwin测试")
#         self.sleep(2)
#         self.my_click(element=routing.alert_routing_match_rule_value)
#         self.my_click(element=routing.alert_routing_notification_expand)
#         self.my_click(element=routing.alert_routing_notification_search)
#         self.my_click(element=routing.alert_routing_notification_name)
#         self.my_click(element=routing.alert_routing_debug_save)
#         self.assertText("调试结果")
#         self.my_click(element=routing.alert_routing_save)
#         self.assertText("保存成功")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
