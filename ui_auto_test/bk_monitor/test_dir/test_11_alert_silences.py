# # -*- coding: utf-8 -*-
# import seldom
# from public_method.login import LoginBase
# from product_page.bk_monitor import home
# from product_page.bk_monitor import alert_rules as alert
# from product_page.bk_monitor import alert_silences as silences
# from public_method.base_operate import BaseOperate
# from product_page import settings
# BaseOperate = BaseOperate()
#
# class AlertSilences(LoginBase):
#     '''告警屏蔽'''
#     def test_01_check_alert_event(self):
#         '''检验新建的告警测试产生告警'''
#         self.open(settings.MONITOR_URL)
#         self.my_click(element=home.strategy_config_navigation)
#         self.my_click(element=alert.alert_rules)
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
#         element = self.my_get_elements(element=alert.alert_event_icon)
#         self.assertTrue(len(element) > 0, "告警事件未产生告警")
#
#     def test_02_alert_event_mute(self):
#         '''快捷屏蔽'''
#         self.my_click(element=home.list_more)
#         self.my_click(element=alert.alert_event_more_button)
#         self.my_click(element=home.home_del_confirm)
#         self.assertText("创建告警屏蔽成功")
#         element = self.my_get_elements(element=alert.alert_mute_icon)
#         self.assertTrue(len(element) > 0, "告警屏蔽未生效")
#
#     def test_03_alert_silences(self):
#         '''进入告警屏蔽业查看快捷屏蔽告警'''
#         self.my_click(element=silences.alert_silences)
#         self.sleep(4)
#         try:
#             shadow_host_selector = "bk-weweb#alarmShield"
#             alert_silences_click = "div.div-input.input-before"
#             alert_silences_search = "div.search-nextfix span.search-nextfix-icon"
#             alert_silences_unmute = "//span[@class='bk-button-text'][contains(text(), '解除')]"
#             alert_silences_cronfrm = ".bk-modal-footer.bk-dialog-footer. bk-button-primary bk-button "
#             input_value = settings.alert_name
#             js = f"""
#                     var shadowHost = document.querySelector("{shadow_host_selector}");
#                     var shadowRoot = shadowHost.shadowRoot;
#
#                     var targetElement = shadowRoot.querySelector("{alert_silences_click}");
#                     targetElement.click();
#                     //输入
#                     var inputElement = shadowRoot.querySelector("{alert_silences_click}");
#                     if (inputElement) {{
#                         inputElement.focus();
#                         var range = document.createRange();
#                         var sel = window.getSelection();
#                         range.selectNodeContents(inputElement);
#                         sel.removeAllRanges();
#                         sel.addRange(range);
#                         document.execCommand('insertText', false, "{input_value}");
#                     }} else {{
#                         console.log('Div element not found');
#                     }}
#                     //搜索
#                     var divElement = shadowRoot.querySelector("{alert_silences_search}");
#                     divElement.click();
#                     """
#             #   //解除
#             #//var contextNode = shadowRoot.host;
#             #//var spanElement = document.evaluate("{alert_silences_unmute}", contextNode, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
#             #//spanElement.click();
#             self.execute_script(js)
#             self.assertText("lunckliu")
#     #         self.assertText("暂无数据")
#         except Exception as e:
#             print(e)
#     #
#     # def test_04_create_alert_silences(self):
#     #     '''创建告警屏蔽'''
#     #     self.open(settings.MONITOR_URL)
#     #     self.my_click(element=home.strategy_config_navigation)
#     #     self.my_click(element=silences.alert_silences)
#     #     alert_silences_create = "button.bk-button-primary bk-button add-btn"
#     #
#     #     self.my_click(element=silences.alert_silences_create)
#     #     self.my_click(element=silences.silences_create_policy)
#     #     self.my_click(element=silences.silences_search_policy)
#     #     self.my_type(element=silences.silences_search_policy, text=settings.alert_name)
#     #     self.my_click(element=silences.silences_search_policy_confirm)
#     #     self.my_click(element=silences.silences_create_confirm)
#     #     self.my_click(element=silences.silences_severity)
#     #     self.scroll_to_bottom(silences.silences_create_confirm['path'])
#     #     self.my_click(element=silences.silences_time_range)
#     #     self.my_click(element=silences.silences_time_search)
#     #     self.my_click(element=silences.silences_time_search)
#     #     self.my_click(element=silences.silences_create_confirm)
#     #     self.assertText("创建屏蔽成功")
#     #
#     # def test_05_check_alert_silences(self):
#     #     '''检查告警屏蔽是否生效'''
#     #     self.my_click(element=alert.alert_rules)
#     #
#     #     try:
#     #         self.my_click(element=alert.alert_rules_search)
#     #         element = self.get_element(xpath=alert.alert_rules_search['path'])
#     #         self.execute_script(f"arguments[0].innerText = '{settings.alert_name}';", element)
#     #         # 触发 input 事件，让输入框更新状态
#     #         self.execute_script("""
#     #                             var event = new Event('input', {
#     #                                 'bubbles': true,
#     #                                 'cancelable': true
#     #                             });
#     #                             arguments[0].dispatchEvent(event);
#     #                         """, element)
#     #         self.my_click(element=alert.alert_rules_search_name)
#     #         self.my_click(element=alert.alert_rules_search_icon)
#     #     except Exception as e:
#     #         print(e)
#     #     element = self.get_elements(xpath=alert.alert_mute_icon)
#     #     self.assertTrue(len(element) > 0, "告警屏蔽未生效")
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
#
#
#
#
#
#
#
#
#
