from time import sleep
import seldom

from bk_nodeman import settings,custom_function
from bk_nodeman.page import plugin_management
from bk_nodeman.test_dir import test_01_login


class LinuxUpdatePlugin(seldom.TestCase):
    def test_01_update_linux_basereport(self):
        """执行安装/更新插件basereport(linux主机云区域)"""
        test_01_login.Login.test_login(self)
        test_01_login.Login.click_plug_in_management(self)
        # 点击搜索框，选择操作系统为linux
        sleep(1)
        self.click(xpath=plugin_management.plugin_select_search)
        self.click(css=plugin_management.click_system)
        self.click(css=plugin_management.select_system_linux)
        # 确认系统为linux
        self.click(css=plugin_management.sure_system)
        # 勾选全部linux主机
        self.click(css=plugin_management.common_checkbox_tableCheckAll)
        # 点击安装/更新操作
        self.click(css=plugin_management.plugin_btn_install)
        # 安装/更新，选择插件basereport，下一步
        self.click(css=plugin_management.plugin_select_pluginName)
        self.click(xpath=plugin_management.select_plugin_basereport)
        self.click(css=plugin_management.common_btn_commit)
        sleep(2)
        # 下一步,下一步,立即执行
        self.click(css=plugin_management.common_btn_stepNext)
        sleep(1)
        self.click(css=plugin_management.step)
        sleep(1)
        self.click(css=plugin_management.common_btn_commit)
        # 等待安装/更新
        self.assertText(settings.STATUS)
        global update_basereport_url
        update_basereport_url = self.get_url
        print(update_basereport_url)

    def test_02_update_linux_processbeat(self):
        """执行安装/更新插件processbeat(linux主机云区域)"""
        test_01_login.Login.click_plug_in_management(self)
        # 点击搜索框，选择操作系统为linux
        sleep(1)
        self.click(xpath=plugin_management.plugin_select_search)
        self.click(css=plugin_management.click_system)
        self.click(css=plugin_management.select_system_linux)
        # 确认系统为linux
        self.click(css=plugin_management.sure_system)
        # 勾选全部linux主机
        self.click(css=plugin_management.common_checkbox_tableCheckAll)
        # 点击安装/更新操作
        self.click(css=plugin_management.plugin_btn_install)
        # 安装/更新，选择插件processbeat，下一步
        self.click(css=plugin_management.plugin_select_pluginName)
        self.click(xpath=plugin_management.select_plugin_processbeat)
        self.click(css=plugin_management.common_btn_commit)
        sleep(2)
        # 下一步,下一步,立即执行
        self.click(css=plugin_management.common_btn_stepNext)
        sleep(1)
        self.click(css=plugin_management.step)
        sleep(1)
        self.click(css=plugin_management.common_btn_commit)
        # 等待安装/更新
        self.assertText(settings.STATUS)
        global update_processbeat_url
        update_processbeat_url = self.get_url
        print(update_processbeat_url)

    def test_03_update_linux_bkunifylogbeat(self):
        """执行安装/更新插件bkunifylogbeat(linux主机云区域)"""
        test_01_login.Login.click_plug_in_management(self)
        # 点击搜索框，选择操作系统为linux
        sleep(1)
        self.click(xpath=plugin_management.plugin_select_search)
        self.click(css=plugin_management.click_system)
        self.click(css=plugin_management.select_system_linux)
        # 确认系统为linux
        self.click(css=plugin_management.sure_system)
        # 勾选全部linux主机
        self.click(css=plugin_management.common_checkbox_tableCheckAll)
        # 点击安装/更新操作
        self.click(css=plugin_management.plugin_btn_install)
        # 安装/更新，选择插件bkunifylogbeat，下一步
        self.click(css=plugin_management.plugin_select_pluginName)
        self.click(xpath=plugin_management.select_plugin_bkunifylogbeat)
        self.click(css=plugin_management.common_btn_commit)
        sleep(2)
        # 下一步,下一步,立即执行
        self.click(css=plugin_management.common_btn_stepNext)
        sleep(1)
        self.click(css=plugin_management.step)
        sleep(1)
        self.click(css=plugin_management.common_btn_commit)
        # 等待安装/更新
        self.assertText(settings.STATUS)
        global update_bkunifylogbeat_url
        update_bkunifylogbeat_url = self.get_url
        print(update_bkunifylogbeat_url)

    def test_04_update_linux_bkmonitorbeat(self):
        """执行安装/更新插件bkmonitorbeat(linux主机云区域)"""
        test_01_login.Login.click_plug_in_management(self)
        # 点击搜索框，选择操作系统为linux
        sleep(1)
        self.click(xpath=plugin_management.plugin_select_search)
        self.click(css=plugin_management.click_system)
        self.click(css=plugin_management.select_system_linux)
        # 确认系统为linux
        self.click(css=plugin_management.sure_system)
        # 勾选全部linux主机
        self.click(css=plugin_management.common_checkbox_tableCheckAll)
        # 点击安装/更新操作
        self.click(css=plugin_management.plugin_btn_install)
        # 安装/更新，选择插件bkmonitorbeat，下一步
        self.click(css=plugin_management.plugin_select_pluginName)
        self.click(xpath=plugin_management.select_plugin_bkmonitorbeat)
        self.click(css=plugin_management.common_btn_commit)
        sleep(2)
        # 下一步,下一步,立即执行
        self.click(css=plugin_management.common_btn_stepNext)
        sleep(1)
        self.click(css=plugin_management.step)
        sleep(1)
        self.click(css=plugin_management.common_btn_commit)
        # 等待安装/更新
        self.assertText(settings.STATUS)
        global update_bkmonitorbeat_url
        update_bkmonitorbeat_url = self.get_url
        print(update_bkmonitorbeat_url)

    def test_05_update_linux_gsecmdline(self):
        """执行安装/更新插件gsecmdline(linux主机云区域)"""
        test_01_login.Login.click_plug_in_management(self)
        # 点击搜索框，选择操作系统为linux
        sleep(1)
        self.click(xpath=plugin_management.plugin_select_search)
        self.click(css=plugin_management.click_system)
        self.click(css=plugin_management.select_system_linux)
        # 确认系统为linux
        self.click(css=plugin_management.sure_system)
        # 勾选全部linux主机
        self.click(css=plugin_management.common_checkbox_tableCheckAll)
        # 点击安装/更新操作
        self.click(css=plugin_management.plugin_btn_install)
        # 安装/更新，选择插件gsecmdline，下一步
        self.click(css=plugin_management.plugin_select_pluginName)
        self.click(xpath=plugin_management.select_plugin_gsecmdline)
        self.click(css=plugin_management.common_btn_commit)
        sleep(2)
        # 下一步,下一步,立即执行
        self.click(css=plugin_management.common_btn_stepNext)
        sleep(1)
        self.click(css=plugin_management.step)
        sleep(1)
        self.click(css=plugin_management.common_btn_commit)
        # 等待安装/更新
        self.assertText(settings.STATUS)
        global update_gsecmdline_url
        update_gsecmdline_url = self.get_url
        print(update_gsecmdline_url)

    def test_06_update_linux_exceptionbeat(self):
        """安装/更新插件exceptionbeat(linux主机云区域)"""
        test_01_login.Login.click_plug_in_management(self)
        # 点击搜索框，选择操作系统为linux
        sleep(1)
        self.click(xpath=plugin_management.plugin_select_search)
        self.click(css=plugin_management.click_system)
        self.click(css=plugin_management.select_system_linux)
        # 确认系统为linux
        self.click(css=plugin_management.sure_system)
        # 勾选全部linux主机
        self.click(css=plugin_management.common_checkbox_tableCheckAll)
        # 点击安装/更新操作
        self.click(css=plugin_management.plugin_btn_install)
        # 安装/更新，选择插件exceptionbeat，下一步
        self.click(css=plugin_management.plugin_select_pluginName)
        self.click(xpath=plugin_management.select_plugin_exceptionbeat)
        self.click(css=plugin_management.common_btn_commit)
        sleep(2)
        # 下一步,下一步,立即执行
        self.click(css=plugin_management.common_btn_stepNext)
        sleep(1)
        self.click(css=plugin_management.step)
        sleep(1)
        self.click(css=plugin_management.common_btn_commit)
        # 等待安装/更新
        self.assertText(settings.STATUS)
        global update_exceptionbeat_url
        update_exceptionbeat_url = self.get_url
        print(update_exceptionbeat_url)

    def test_07_update_linux_bkmonitorproxy(self):
        """分别断言各插件是否安装成功"""
        test_01_login.Login.click_plug_in_management(self)
        # 点击搜索框，选择操作系统为linux
        sleep(1)
        self.click(xpath=plugin_management.plugin_select_search)
        self.click(css=plugin_management.click_system)
        self.click(css=plugin_management.select_system_linux)
        # 确认系统为linux
        self.click(css=plugin_management.sure_system)
        # 勾选全部linux主机
        self.click(css=plugin_management.common_checkbox_tableCheckAll)
        # 点击安装/更新操作
        self.click(css=plugin_management.plugin_btn_install)
        # 安装/更新，选择插件bkmonitorproxy，下一步
        self.click(css=plugin_management.plugin_select_pluginName)
        self.click(xpath=plugin_management.select_plugin_bkmonitorproxy)
        self.click(css=plugin_management.common_btn_commit)
        sleep(2)
        # 下一步,下一步,立即执行
        self.click(css=plugin_management.common_btn_stepNext)
        sleep(1)
        self.click(css=plugin_management.step)
        sleep(1)
        self.click(css=plugin_management.common_btn_commit)
        # 等待安装/更新
        self.assertText(settings.STATUS)
        update_bkmonitorproxy_url = self.get_url
        print(update_bkmonitorproxy_url)
       # 断言安装bkunifylogbeat是否成功
        custom_function.test_login_assert(self, update_bkunifylogbeat_url)
        self.is_visible(420,xpath=plugin_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)
        # 断言安装bkmonitorproxy是否成功
        custom_function.test_login_assert(self, update_bkmonitorproxy_url)
        self.is_visible(420, xpath=plugin_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)
        # 断言安装exceptionbeat是否成功
        custom_function.test_login_assert(self, update_exceptionbeat_url)
        self.is_visible(420, xpath=plugin_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)
        # 断言安装gsecmdline是否成功
        custom_function.test_login_assert(self, update_gsecmdline_url)
        self.is_visible(420, xpath=plugin_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)
        # 断言安装basereport是否成功
        custom_function.test_login_assert(self, update_basereport_url)
        self.is_visible(420, xpath=plugin_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)
        # 断言安装processbeat是否成功
        custom_function.test_login_assert(self, update_processbeat_url)
        self.is_visible(420, xpath=plugin_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)
        # 断言安装bkmonitorbeat是否成功
        custom_function.test_login_assert(self, update_bkmonitorbeat_url)
        self.is_visible(420, xpath=plugin_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)