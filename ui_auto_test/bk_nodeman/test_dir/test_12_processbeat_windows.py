from time import sleep
import seldom

from bk_nodeman import settings,custom_function
from bk_nodeman.page import plugin_management
from bk_nodeman.test_dir import test_01_login


class WindowsProcessbeat(seldom.TestCase):
    def test_01_stop_processbeat(self):
        """执行停止processbeat插件（windows主机）"""
        test_01_login.Login.test_login(self)
        test_01_login.Login.click_plug_in_management(self)
        # 点击搜索框，选择操作系统为windows
        sleep(3)
        self.click(xpath=plugin_management.plugin_select_search)
        self.click(css=plugin_management.click_system)
        self.click(css=plugin_management.select_system_windows)
        # 确认系统为windows
        self.click(css=plugin_management.sure_system)
        # 勾选全部windows主机
        self.click(css=plugin_management.common_checkbox_tableCheckAll)
        # 点击批量插件操作
        self.click(css=plugin_management.plugin_btn_operatePlugin)
        # 停止插件选择processbeat，下一步
        self.click(css=plugin_management.plugin_btn_stop)
        self.click(css=plugin_management.plugin_select_pluginName)
        self.click(xpath=plugin_management.select_plugin_processbeat)
        self.click(css=plugin_management.common_btn_commit)
        sleep(0.5)
        # 立即执行
        self.click(css=plugin_management.common_btn_commit)
        # 等待并断言
        self.assertText(settings.STATUS)
        global stop_processbeat_url
        stop_processbeat_url = self.get_url
        print(stop_processbeat_url)

    def test_02_start_processbeat(self):
        """执行启动processbeat插件（windows主机），断言停止启动是否成功"""
        # 进入插件管理
        test_01_login.Login.test_login(self)
        test_01_login.Login.click_plug_in_management(self)
        # 点击搜索框，选择操作系统为windows
        sleep(1)
        self.click(xpath=plugin_management.plugin_select_search)
        self.click(css=plugin_management.click_system)
        self.click(css=plugin_management.select_system_windows)
        # 确认系统为windows
        self.click(css=plugin_management.sure_system)
        # 勾选全部windows主机
        self.click(css=plugin_management.common_checkbox_tableCheckAll)
        # 点击批量插件操作
        self.click(css=plugin_management.plugin_btn_operatePlugin)
        # 启动插件选择processbeat，下一步
        self.click(css=plugin_management.plugin_btn_start)
        self.click(css=plugin_management.plugin_select_pluginName)
        self.click(xpath=plugin_management.select_plugin_processbeat)
        self.click(css=plugin_management.common_btn_commit)
        sleep(0.5)
        # 立即执行
        self.click(css=plugin_management.common_btn_commit)
        # 等待并断言
        self.assertText(settings.STATUS)
        start_processbeat_url = self.get_url
        print(start_processbeat_url)
        # 断言停止processbeat是否成功
        custom_function.test_login_assert(self, stop_processbeat_url)
        self.is_visible(30,xpath=plugin_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)
        # 断言启动processbeat是否成功
        custom_function.test_login_assert(self, start_processbeat_url)
        self.is_visible(30, xpath=plugin_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)
