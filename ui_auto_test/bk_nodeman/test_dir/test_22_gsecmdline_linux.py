from time import sleep
import seldom

from bk_nodeman import settings
from bk_nodeman.page import plugin_management
from bk_nodeman.test_dir import test_01_login


class LinuxGsecmdline(seldom.TestCase):
    def test_01_stop_gsecmdline(self):
        """执行停止gsecmdline插件（linux主机）"""
        test_01_login.Login.test_login(self)
        test_01_login.Login.click_plug_in_management(self)
        # 点击搜索框，选择操作系统为linux
        sleep(3)
        self.click(xpath=plugin_management.plugin_select_search)
        self.click(css=plugin_management.click_system)
        self.click(css=plugin_management.select_system_linux)
        # 确认系统为linux
        self.click(css=plugin_management.sure_system)
        # 勾选全部linux主机
        self.click(css=plugin_management.common_checkbox_tableCheckAll)
        # 点击批量插件操作
        self.click(css=plugin_management.plugin_btn_operatePlugin)
        # 停止插件选择gsecmdline，下一步
        self.click(css=plugin_management.plugin_btn_stop)
        self.click(css=plugin_management.plugin_select_pluginName)
        self.click(xpath=plugin_management.select_plugin_gsecmdline)
        self.click(css=plugin_management.common_btn_commit)
        sleep(0.5)
        # 立即执行
        self.click(css=plugin_management.common_btn_commit)
        # 等待并断言
        self.assertText(settings.EXECUTE_SUCCESSFULLY)

    def test_02_start_gsecmdline(self):
        """执行启动gsecmdline插件（linux主机），断言停止启动是否成功"""
        # 进入插件管理
        test_01_login.Login.test_login(self)
        test_01_login.Login.click_plug_in_management(self)
        sleep(1)
        # 点击搜索框，选择操作系统为linux
        self.click(xpath=plugin_management.plugin_select_search)
        self.click(css=plugin_management.click_system)
        self.click(css=plugin_management.select_system_linux)
        # 确认系统为linux
        self.click(css=plugin_management.sure_system)
        # 勾选全部linux主机
        self.click(css=plugin_management.common_checkbox_tableCheckAll)
        # 点击批量插件操作
        self.click(css=plugin_management.plugin_btn_operatePlugin)
        # 启动插件选择gsecmdline，下一步
        self.click(css=plugin_management.plugin_btn_start)
        self.click(css=plugin_management.plugin_select_pluginName)
        self.click(xpath=plugin_management.select_plugin_gsecmdline)
        self.click(css=plugin_management.common_btn_commit)
        sleep(0.5)
        # 立即执行
        self.click(css=plugin_management.common_btn_commit)
        # 等待并断言
        self.assertText(settings.EXECUTE_SUCCESSFULLY)
