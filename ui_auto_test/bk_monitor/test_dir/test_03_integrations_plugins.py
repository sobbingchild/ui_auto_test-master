# from public_method.login import LoginBase
# from product_page.bk_monitor import home
# from product_page.bk_monitor import integrations_collection as integ_home
# from product_page.bk_monitor import integrations_plugins as plugins
# from public_method.base_operate import BaseOperate
# from product_page import settings
# BaseOperate = BaseOperate()
#
# class IntegrationsPlugins(LoginBase):
#     '''插件'''
#     def test_01_create_plugins(self):
#         """新建插件"""
#         self.open(settings.MONITOR_URL)
#         self.my_click(element=home.plugin_manager_navigation)
#         self.my_click(element=integ_home.plugins_navigation)
#         self.my_click(element=plugins.create_plugins)
#         name = BaseOperate.random_data()
#         settings.plugins_id_name = name
#         self.my_type(element=plugins.plugins_id, text=name)
#         self.scroll_to_bottom(plugins.create_plugin_next['path'])
#         self.my_click(element=plugins.create_plugin_next)
#         self.sleep(10)
#         self.my_click(element=plugins.plugin_test_probe)
#         self.my_click(element=plugins.plugin_test_probe_ip)
#         self.my_click(element=plugins.plugin_dubug)
#         self.sleep(10)
#         self.my_click(element=plugins.plugin_save)
#         self.sleep(3)
#         self.assertText("创建插件完成")
#         self.my_click(element=plugins.plugin_create_closs)
#
#
#     def test_02_search_plugins(self):
#         """查询新建插件进入详情"""
#         self.my_click(element=plugins.plugin_search)
#         self.my_type(element=plugins.plugin_search, text=settings.plugins_id_name)
#         self.Keys(xpath=plugins.plugin_search['path']).enter()
#         self.assertText("共计1条")
#         self.my_click(element=plugins.plugin_name_click)
#         self.check_page_error()
#         self.assertText("插件详情")
#         self.assertText("指标维度")
#         self.my_click(home.home_back)
#         self.assertText(settings.plugins_id_name)
#
#     def test_03_del_plugins(self):
#         """删除新建插件"""
#         self.my_click(element=plugins.plugin_more)
#         self.my_click(element=plugins.plugin_more_del)
#         self.my_click(element=plugins.plugin_more_del_comfirm)
#         self.assertText("删除插件成功")
#
#
