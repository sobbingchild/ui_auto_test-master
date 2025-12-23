# from public_method.login import LoginBase
# from product_page.bk_monitor import home
# from product_page.bk_monitor import integrations_collection as integ_home
# from product_page.bk_monitor import integrations_plugins as plugins
# from public_method.base_operate import BaseOperate
# from product_page import settings
# BaseOperate = BaseOperate()
#
# class IntegrationsCollection(LoginBase):
#     '''数据采集'''
#     def test_01_create_collection(self):
#         '''新建数据采集》进程采集'''
#         self.open(settings.MONITOR_URL)
#         self.my_click(element=home.plugin_manager_navigation)
#         self.my_click(element=integ_home.collection_navigation)
#         self.my_click(element=integ_home.create_collection)
#         name = BaseOperate.random_data()
#         settings.collection_name = name
#         self.my_type(element=integ_home.create_collection_name, text=name)
#         self.my_click(element=integ_home.create_collection_plugins)
#         self.my_type(element=integ_home.create_collection_plugins_serach, text="进程采集插件")
#         self.Keys(xpath=integ_home.create_collection_plugins_serach['path']).enter()
#         self.my_click(element=integ_home.create_collection_match)
#         self.my_type(element=integ_home.create_collection_process, text="agent")
#         self.my_click(element=plugins.create_plugin_next)
#         self.my_click(element=integ_home.create_collection_host)
#         self.my_click(element=integ_home.create_collection_deploy)
#         self.sleep(10)
#         for i in range(10):
#             try:
#                 self.my_click(element=integ_home.create_collection_done)
#                 break
#             except:
#                 pass
#         self.assertText("配置已新增")
#         self.my_click(element=integ_home.create_collection_closs)
#         self.assertText("新建")
#
#     def test_02_search_collection(self):
#         """查询新建数据采集进入详情查看采集状态"""
#         self.sleep(3)
#         self.my_click(element=integ_home.collection_search)
#         self.my_type(element=integ_home.collection_search, text=settings.collection_name)
#         self.Keys(xpath=integ_home.collection_search['path']).enter()
#         self.assertText("共计1条")
#         self.my_click(element=integ_home.collection_name_click)
#         self.check_page_error()
#         self.assertText("配置信息")
#         self.my_click(element=integ_home.collection_states)
#         self.assertText("1个成功")
#         self.my_click(home.home_back)
#         self.assertText(settings.collection_name)
#
#
#
#
#
#
#
#
#
