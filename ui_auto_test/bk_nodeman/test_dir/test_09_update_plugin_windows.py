from time import sleep
import seldom

from bk_nodeman import settings,custom_function
from bk_nodeman.page import plugin_management
from bk_nodeman.test_dir import test_01_login

class WindowsUpdatePlugin(seldom.TestCase):
    def test_01_update_windows_basereport(self):
        """执行安装/更新插件basereport(windows主机直连区域)"""
        test_01_login.Login.test_login(self)
        test_01_login.Login.click_plug_in_management(self)
        sleep(3)
        #点击并选择业务
        self.click(css=plugin_management.click_business)
        sleep(1)
        #搜索框输入"节点管理自动测试"
        self.type(css=plugin_management.search_business,text=settings.BUSINESS_NAME_NODEMAN)
        sleep(1)
        #点击"节点管理自动化测试",必须加sleep,否则report报错stale element reference: element is not attached to the page document
        self.click(xpath=plugin_management.plugin_business)
        #点击搜索框，现在操作系统为windows
        sleep(1)
        self.click(xpath=plugin_management.plugin_select_search)
        self.click(css=plugin_management.click_system)
        self.click(css=plugin_management.select_system_windows)
        #确认系统为windows
        self.click(css=plugin_management.sure_system)
        #勾选全部windows主机
        self.click(css=plugin_management.common_checkbox_tableCheckAll)
        #点击安装/更新操作
        self.click(css=plugin_management.plugin_btn_install)
        #安装/更新，选择插件basereport，下一步
        self.click(css=plugin_management.plugin_select_pluginName)
        self.click(xpath=plugin_management.select_plugin_basereport)
        self.click(css=plugin_management.common_btn_commit)
        sleep(2)
        #下一步,下一步,立即执行
        self.click(css=plugin_management.common_btn_stepNext)
        sleep(1)
        self.click(css=plugin_management.step)
        sleep(1)
        self.click(css=plugin_management.common_btn_commit)
        #等待安装/更新
        self.assertText(settings.STATUS)
        global update_basereport_url
        update_basereport_url = self.get_url
        print(update_basereport_url)
    def test_02_update_windows_processbeat(self):
        """执行安装/更新插件processbeat(windows主机直连区域)"""
        test_01_login.Login.click_plug_in_management(self)
        #点击搜索框，选择操作系统为windows
        sleep(1)
        self.click(xpath=plugin_management.plugin_select_search)
        self.click(css=plugin_management.click_system)
        self.click(css=plugin_management.select_system_windows)
        #确认系统为windows
        self.click(css=plugin_management.sure_system)
        #勾选全部windows主机
        self.click(css=plugin_management.common_checkbox_tableCheckAll)
        #点击安装/更新操作
        self.click(css=plugin_management.plugin_btn_install)
        #安装/更新，选择插件processbeat，下一步
        self.click(css=plugin_management.plugin_select_pluginName)
        self.click(xpath=plugin_management.select_plugin_processbeat)
        self.click(css=plugin_management.common_btn_commit)
        sleep(2)
        #下一步,下一步,立即执行
        self.click(css=plugin_management.common_btn_stepNext)
        sleep(1)
        self.click(css=plugin_management.step)
        sleep(1)
        self.click(css=plugin_management.common_btn_commit)
        #等待安装/更新
        self.assertText(settings.STATUS)
        global update_processbeat_url
        update_processbeat_url = self.get_url
        print(update_processbeat_url)
    def test_03_update_windows_bkunifylogbeat(self):
        """执行安装/更新插件bkunifylogbeat(windows主机直连区域)"""
        test_01_login.Login.click_plug_in_management(self)
        #点击搜索框，选择操作系统为windows
        sleep(1)
        self.click(xpath=plugin_management.plugin_select_search)
        self.click(css=plugin_management.click_system)
        self.click(css=plugin_management.select_system_windows)
        #确认系统为windows
        self.click(css=plugin_management.sure_system)
        #勾选全部windows主机
        self.click(css=plugin_management.common_checkbox_tableCheckAll)
        #点击安装/更新操作
        self.click(css=plugin_management.plugin_btn_install)
        #安装/更新，选择插件bkunifylogbeat，下一步
        self.click(css=plugin_management.plugin_select_pluginName)
        self.click(xpath=plugin_management.select_plugin_bkunifylogbeat)
        self.click(css=plugin_management.common_btn_commit)
        sleep(2)
        #下一步,下一步,立即执行
        self.click(css=plugin_management.common_btn_stepNext)
        sleep(1)
        self.click(css=plugin_management.step)
        sleep(1)
        self.click(css=plugin_management.common_btn_commit)
        #等待安装/更新
        self.assertText(settings.STATUS)
        global update_bkunifylogbeat_url
        update_bkunifylogbeat_url = self.get_url
        print(update_bkunifylogbeat_url)
    def test_04_update_windows_bkmonitorbeat(self):
        """执行安装/更新插件bkmonitorbeat(windows主机直连区域)"""
        test_01_login.Login.click_plug_in_management(self)
        #点击搜索框，选择操作系统为windows
        sleep(1)
        self.click(xpath=plugin_management.plugin_select_search)
        self.click(css=plugin_management.click_system)
        self.click(css=plugin_management.select_system_windows)
        #确认系统为windows
        self.click(css=plugin_management.sure_system)
        #勾选全部windows主机
        self.click(css=plugin_management.common_checkbox_tableCheckAll)
        #点击安装/更新操作
        self.click(css=plugin_management.plugin_btn_install)
        #安装/更新，选择插件bkmonitorbeat，下一步
        self.click(css=plugin_management.plugin_select_pluginName)
        self.click(xpath=plugin_management.select_plugin_bkmonitorbeat)
        self.click(css=plugin_management.common_btn_commit)
        sleep(2)
        #下一步,下一步,立即执行
        self.click(css=plugin_management.common_btn_stepNext)
        sleep(1)
        self.click(css=plugin_management.step)
        sleep(1)
        self.click(css=plugin_management.common_btn_commit)
        #等待安装/更新
        self.assertText(settings.STATUS)
        global update_bkmonitorbeat_url
        update_bkmonitorbeat_url = self.get_url
        print(update_bkmonitorbeat_url)
    def test_05_update_windows_gsecmdline(self):
        """分别断言各插件是否安装成功"""
        test_01_login.Login.click_plug_in_management(self)
        #点击搜索框，选择操作系统为windows
        sleep(1)
        self.click(xpath=plugin_management.plugin_select_search)
        self.click(css=plugin_management.click_system)
        self.click(css=plugin_management.select_system_windows)
        #确认系统为windows
        self.click(css=plugin_management.sure_system)
        #勾选全部windows主机
        self.click(css=plugin_management.common_checkbox_tableCheckAll)
        #点击安装/更新操作
        self.click(css=plugin_management.plugin_btn_install)
        #安装/更新，选择插件gsecmdline，下一步
        self.click(css=plugin_management.plugin_select_pluginName)
        self.click(xpath=plugin_management.select_plugin_gsecmdline)
        self.click(css=plugin_management.common_btn_commit)
        sleep(2)
        #下一步,下一步,立即执行
        self.click(css=plugin_management.common_btn_stepNext)
        sleep(1)
        self.click(css=plugin_management.step)
        sleep(1)
        self.click(css=plugin_management.common_btn_commit)
        #等待安装/更新
        self.assertText(settings.STATUS)
        update_gsecmdline_url = self.get_url
        print(update_gsecmdline_url)
        # 断言安装gsecmdline是否成功
        custom_function.test_login_assert(self, update_gsecmdline_url)
        self.is_visible(90,xpath=plugin_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)
        # 断言安装basereport是否成功
        custom_function.test_login_assert(self,update_basereport_url)
        self.is_visible(90, xpath=plugin_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)
        # 断言安装processbeat是否成功
        custom_function.test_login_assert(self, update_processbeat_url)
        self.is_visible(90, xpath=plugin_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)
        # 断言安装bkunifylogbeat是否成功
        custom_function.test_login_assert(self,update_bkunifylogbeat_url)
        self.is_visible(90, xpath=plugin_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)
        # 断言安装bkmonitorbeat是否成功
        custom_function.test_login_assert(self, update_bkmonitorbeat_url)
        self.is_visible(90, xpath=plugin_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)