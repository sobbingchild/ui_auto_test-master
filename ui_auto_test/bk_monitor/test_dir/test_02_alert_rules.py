# -*- coding: utf-8 -*-
from public_method.login import LoginBase
from product_page.bk_monitor import home
from product_page.bk_monitor import alert_rules as alert
from public_method.base_operate import BaseOperate
from product_page import settings
from product_page.public_components import ip_choose
BaseOperate = BaseOperate()

class AlertRulesEvent(LoginBase):
    '''告警策略'''
    def test_01_create_alert_event(self):
        '''新增指标数据告警策略，可产生告警'''
        self.open(settings.MONITOR_URL)
        self.my_click(element=home.strategy_config_navigation)
        if self.my_get_elements(element=alert.alert_rules):
            self.my_click(element=alert.alert_rules)
        else:
            self.my_click(element=home.navigation_packup)
            self.my_click(element=alert.alert_rules)
        self.my_click(element=alert.alert_new)
        name = BaseOperate.random_data()
        settings.alert_name = name
        self.my_type(element=alert.alert_new_name, text=name)
        self.my_type(element=alert.alert_new_priority, text=1)
        self.my_click(element=alert.alert_new_metrics)
        self.my_click(element=alert.alert_new_metrics_add)
        self.my_click(element=alert.alert_new_metrics_search)
        self.my_click(element=alert.alert_new_add_ip)
        self.my_click(element=ip_choose.choose_agent)
        self.my_click(element=ip_choose.choose_host_confirm)
        self.my_click(element=alert.alert_new_submit)
        #self.my_type(element=alert.alert_new_metrics_search, text="磁盘空间使用率")
        #self.Keys(xpath=alert.alert_new_metrics_search['path']).enter()
        self.my_click(element=alert.alert_new_static)
        self.my_click(element=alert.alert_new_submit)
        self.my_click(element=alert.alert_new_handling)
        self.my_click(element=alert.alert_new_handling_triggered)
        self.my_click(element=alert.alert_new_handling)
        self.my_click(element=alert.alert_new_handling_triggered_select)
        self.my_type(element=alert.alert_new_handling_triggered_search, text=settings.solutions_name)
        self.sleep(1)
        self.my_click(element=alert.alert_new_handling_triggered_search_save)
        self.assertText("套餐详情")
        self.my_click(element=home.side_slip_close)
        self.my_click(element=alert.alert_new_submit)
        self.my_click(element=alert.alert_new_alarm_team)
        self.sleep(1)
        self.my_type(element=alert.alert_new_alarm_team_search, text="lunck")
        self.Keys(xpath=alert.alert_new_alarm_team_search['path']).enter()
        self.my_click(element=alert.alert_new_collapse)
        self.assertNotText("数据预览")
        self.my_click(element=alert.alert_new_submit)
        self.assertText("创建策略成功")

    def test_02_check_alert_event(self):
        '''进入创建的告警策略详情'''
        self.sleep(2)
        self.my_click(element=alert.alert_rules_search)
        try:
            element = self.get_element(xpath=alert.alert_rules_search['path'])
            self.execute_script(f"arguments[0].innerText = '{settings.alert_name}';", element)
            # 触发 input 事件，让输入框更新状态
            self.execute_script("""
                        var event = new Event('input', {
                            'bubbles': true,
                            'cancelable': true
                        });
                        arguments[0].dispatchEvent(event);
                    """, element)
            self.my_click(element=alert.alert_rules_search_name)
            self.my_click(element=alert.alert_rules_search_icon)
        except Exception as e:
            print(e)
        self.assertText("共计1条")
        self.my_click(element=alert.alert_search_name)
        self.check_page_error()
        self.assertText("策略详情")
        self.assertText('数据预览')
        self.my_click(element=home.home_back)
        self.assertText("新建")

    def test_03_check_alert_team(self):
        '''告警列表点击告警组查看'''
        self.my_click(alert.alert_rules_team)
        self.check_page_error()
        self.assertText("告警组详情")
        self.assertText("测试告警组，误删")







