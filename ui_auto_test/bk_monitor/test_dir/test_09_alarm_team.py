# from public_method.login import LoginBase
# from product_page.bk_monitor import home
# from product_page.bk_monitor import alarm_team as alarm
# from public_method.base_operate import BaseOperate
# from product_page import settings
# BaseOperate = BaseOperate()
#
# class AlertTeam(LoginBase):
#     '''告警组'''
#     def test_01_create_group(self):
#         '''查看告警组'''
#         self.open(settings.MONITOR_URL)
#         self.my_click(home.strategy_config_navigation)
#         self.sleep(2)
#         self.my_click(element=alarm.alert_team)
#         self.check_page_error()
#         self.sleep(1)
#         self.my_click(element=alarm.alert_team_check_name)
#         self.assertText("告警组详情")
#         self.sleep(2)
#
#
#
#
#
#
#
