import seldom
from time import sleep
from bk_nodeman import settings,custom_function
from bk_nodeman.page import business,plugin_management
from bk_nodeman.test_dir import test_01_login
from public_method.keyboard_operation import MyWebDriver

class LinuxAgent(seldom.TestCase):
    def test_01_update_linux_plugin(self):
        """更新linux插件"""
        test_01_login.Login.test_login_cmdb(self)
        # 点击资源
        test_01_login.Login.click_business(self)
        # 等待后输入业务名并点击
        sleep(1)
        #默认进入蓝鲸业务，展开Pass平台，点击apigw
        self.click(xpath=business.pass_platform)
        self.click(xpath=business.apigw)
        #获取模块apigw的值
        global BluekingHostIp
        BluekingHostIp = self.get_text(xpath=business.get_host)
        print(BluekingHostIp)
        test_01_login.Login.test_login(self)
        #点击插件状态
        test_01_login.Login.click_plug_in_management(self)
        #点击并选择业务
        self.click(css=plugin_management.click_business)
        sleep(1)
        #搜索框输入"蓝鲸"
        self.type(css=plugin_management.search_business,text=settings.BLUE_BUSINESS)
        sleep(1)
        #点击"蓝鲸",必须加sleep,否则report报错stale element reference: element is not attached to the page document
        self.click(xpath=plugin_management.plugin_business)
        self.is_visible(10,xpath=plugin_management.search_hostip)
        #点击搜索框，输入IP
        self.type(xpath=plugin_management.search_hostip,text=BluekingHostIp)
        #模拟enter键
        MyWebDriver.Keys(xpath=plugin_management.search_hostip).enter()
        #勾选主机
        self.click(css=plugin_management.common_checkbox_tableCheckAll)
        #点击安装/更新
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
    def test_02_update_linux_processbeat(self):
        """执行安装/更新插件processbeat(linux主机直连区域)"""
        test_01_login.Login.click_plug_in_management(self)
        self.is_visible(10,xpath=plugin_management.search_hostip)
        #点击搜索框，输入IP
        self.type(xpath=plugin_management.search_hostip,text=BluekingHostIp)
        #模拟enter键
        MyWebDriver.Keys(xpath=plugin_management.search_hostip).enter()
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
        """执行安装/更新插件bkunifylogbeat(linux主机直连区域)"""
        test_01_login.Login.click_plug_in_management(self)
        self.is_visible(10,xpath=plugin_management.search_hostip)
        #点击搜索框，输入IP
        self.type(xpath=plugin_management.search_hostip,text=BluekingHostIp)
        #模拟enter键
        MyWebDriver.Keys(xpath=plugin_management.search_hostip).enter()
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
        """执行安装/更新插件bkmonitorbeat(linux主机直连区域)"""
        test_01_login.Login.click_plug_in_management(self)
        self.is_visible(10, xpath=plugin_management.search_hostip)
        # 点击搜索框，输入IP
        self.type(xpath=plugin_management.search_hostip, text=BluekingHostIp)
        # 模拟enter键
        MyWebDriver.Keys(xpath=plugin_management.search_hostip).enter()
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
        """执行安装/更新插件gsecmdline(linux主机直连区域)"""
        test_01_login.Login.click_plug_in_management(self)
        self.is_visible(10, xpath=plugin_management.search_hostip)
        # 点击搜索框，输入IP
        self.type(xpath=plugin_management.search_hostip, text=BluekingHostIp)
        # 模拟enter键
        MyWebDriver.Keys(xpath=plugin_management.search_hostip).enter()
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
        """安装/更新插件exceptionbeat(linux主机直连区域)"""
        test_01_login.Login.click_plug_in_management(self)
        self.is_visible(10,xpath=plugin_management.search_hostip)
        #点击搜索框，输入IP
        self.type(xpath=plugin_management.search_hostip,text=BluekingHostIp)
        #模拟enter键
        MyWebDriver.Keys(xpath=plugin_management.search_hostip).enter()
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
        self.is_visible(10, xpath=plugin_management.search_hostip)
        # 点击搜索框，输入IP
        self.type(xpath=plugin_management.search_hostip, text=BluekingHostIp)
        # 模拟enter键
        MyWebDriver.Keys(xpath=plugin_management.search_hostip).enter()
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

    def test_08_stop_basereport(self):
        """执行停止basereport插件（linux主机）"""
        test_01_login.Login.test_login(self)
        test_01_login.Login.click_plug_in_management(self)
        self.is_visible(10, xpath=plugin_management.search_hostip)
        # 点击搜索框，输入IP
        self.type(xpath=plugin_management.search_hostip, text=BluekingHostIp)
        # 模拟enter键
        MyWebDriver.Keys(xpath=plugin_management.search_hostip).enter()
        # 勾选全部linux主机
        self.click(css=plugin_management.common_checkbox_tableCheckAll)
        # 点击批量插件操作
        self.click(css=plugin_management.plugin_btn_operatePlugin)
        # 停止插件选择basereport，下一步
        self.click(css=plugin_management.plugin_btn_stop)
        self.click(css=plugin_management.plugin_select_pluginName)
        self.click(xpath=plugin_management.select_plugin_basereport)
        self.click(css=plugin_management.common_btn_commit)
        sleep(0.5)
        # 立即执行
        self.click(css=plugin_management.common_btn_commit)
        # 等待并断言
        self.assertText(settings.STATUS)
        global stop_basereport_url
        stop_basereport_url = self.get_url
        print(stop_basereport_url)

    def test_09_start_basereport(self):
        """执行启动basereport插件（linux主机），断言停止启动是否成功"""
        # 进入插件管理
        test_01_login.Login.test_login(self)
        test_01_login.Login.click_plug_in_management(self)
        sleep(1)
        self.is_visible(10, xpath=plugin_management.search_hostip)
        # 点击搜索框，输入IP
        self.type(xpath=plugin_management.search_hostip, text=BluekingHostIp)
        # 模拟enter键
        MyWebDriver.Keys(xpath=plugin_management.search_hostip).enter()
        # 勾选全部linux主机
        self.click(css=plugin_management.common_checkbox_tableCheckAll)
        # 点击批量插件操作
        self.click(css=plugin_management.plugin_btn_operatePlugin)
        # 启动插件选择basereport，下一步
        self.click(css=plugin_management.plugin_btn_start)
        self.click(css=plugin_management.plugin_select_pluginName)
        self.click(xpath=plugin_management.select_plugin_basereport)
        self.click(css=plugin_management.common_btn_commit)
        sleep(0.5)
        # 立即执行
        self.click(css=plugin_management.common_btn_commit)
        # 等待并断言
        self.assertText(settings.STATUS)
        start_basereport_url = self.get_url
        print(start_basereport_url)
        # 断言停止basereport是否成功
        custom_function.test_login_assert(self, stop_basereport_url)
        self.is_visible(30,xpath=plugin_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)
        # 断言启动basereport是否成功
        custom_function.test_login_assert(self, start_basereport_url)
        self.is_visible(30, xpath=plugin_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)

    def test_10_stop_processbeat(self):
        """执行停止processbeat插件（linux主机）"""
        test_01_login.Login.test_login(self)
        test_01_login.Login.click_plug_in_management(self)
        self.is_visible(10, xpath=plugin_management.search_hostip)
        # 点击搜索框，输入IP
        self.type(xpath=plugin_management.search_hostip, text=BluekingHostIp)
        # 模拟enter键
        MyWebDriver.Keys(xpath=plugin_management.search_hostip).enter()
        # 勾选全部linux主机
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

    def test_11_start_processbeat(self):
        """执行启动processbeat插件（linux主机），断言停止启动是否成功"""
        # 进入插件管理
        test_01_login.Login.test_login(self)
        test_01_login.Login.click_plug_in_management(self)
        self.is_visible(10, xpath=plugin_management.search_hostip)
        # 点击搜索框，输入IP
        self.type(xpath=plugin_management.search_hostip, text=BluekingHostIp)
        # 模拟enter键
        MyWebDriver.Keys(xpath=plugin_management.search_hostip).enter()
        # 勾选全部linux主机
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
    def test_12_stop_exceptionbeat(self):
        """执行停止exceptionbeat插件（linux主机）"""
        test_01_login.Login.test_login(self)
        test_01_login.Login.click_plug_in_management(self)
        self.is_visible(10, xpath=plugin_management.search_hostip)
        # 点击搜索框，输入IP
        self.type(xpath=plugin_management.search_hostip, text=BluekingHostIp)
        # 模拟enter键
        MyWebDriver.Keys(xpath=plugin_management.search_hostip).enter()
        # 勾选全部linux主机
        self.click(css=plugin_management.common_checkbox_tableCheckAll)
        # 点击批量插件操作
        self.click(css=plugin_management.plugin_btn_operatePlugin)
        # 停止插件选择exceptionbeat，下一步
        self.click(css=plugin_management.plugin_btn_stop)
        self.click(css=plugin_management.plugin_select_pluginName)
        self.click(xpath=plugin_management.select_plugin_exceptionbeat)
        self.click(css=plugin_management.common_btn_commit)
        sleep(0.5)
        # 立即执行
        self.click(css=plugin_management.common_btn_commit)
        # 等待并断言
        self.assertText(settings.STATUS)
        global stop_exceptionbeat_url
        stop_exceptionbeat_url = self.get_url
        print(stop_exceptionbeat_url)

    def test_13_start_exceptionbeat(self):
        """执行启动exceptionbeat插件（linux主机），断言停止启动是否成功"""
        # 进入插件管理
        test_01_login.Login.test_login(self)
        test_01_login.Login.click_plug_in_management(self)
        self.is_visible(10, xpath=plugin_management.search_hostip)
        # 点击搜索框，输入IP
        self.type(xpath=plugin_management.search_hostip, text=BluekingHostIp)
        # 模拟enter键
        MyWebDriver.Keys(xpath=plugin_management.search_hostip).enter()
        # 勾选全部linux主机
        self.click(css=plugin_management.common_checkbox_tableCheckAll)
        # 点击批量插件操作
        self.click(css=plugin_management.plugin_btn_operatePlugin)
        # 启动插件选择exceptionbeat，下一步
        self.click(css=plugin_management.plugin_btn_start)
        self.click(css=plugin_management.plugin_select_pluginName)
        self.click(xpath=plugin_management.select_plugin_exceptionbeat)
        self.click(css=plugin_management.common_btn_commit)
        sleep(0.5)
        # 立即执行
        self.click(css=plugin_management.common_btn_commit)
        # 等待并断言
        self.assertText(settings.STATUS)
        start_exceptionbeat_url = self.get_url
        print(start_exceptionbeat_url)
        # 断言停止exceptionbeat是否成功
        custom_function.test_login_assert(self, stop_exceptionbeat_url)
        self.is_visible(30, xpath=plugin_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)
        # 断言启动exceptionbeat是否成功
        custom_function.test_login_assert(self, start_exceptionbeat_url)
        self.is_visible(30, xpath=plugin_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)

    def test_14_stop_bkunifylogbeat(self):
        """执行停止bkunifylogbeat插件（linux主机）"""
        test_01_login.Login.test_login(self)
        test_01_login.Login.click_plug_in_management(self)
        self.is_visible(10, xpath=plugin_management.search_hostip)
        # 点击搜索框，输入IP
        self.type(xpath=plugin_management.search_hostip, text=BluekingHostIp)
        # 模拟enter键
        MyWebDriver.Keys(xpath=plugin_management.search_hostip).enter()
        # 勾选全部linux主机
        self.click(css=plugin_management.common_checkbox_tableCheckAll)
        # 点击批量插件操作
        self.click(css=plugin_management.plugin_btn_operatePlugin)
        # 停止插件选择bkunifylogbeat，下一步
        self.click(css=plugin_management.plugin_btn_stop)
        self.click(css=plugin_management.plugin_select_pluginName)
        self.click(xpath=plugin_management.select_plugin_bkunifylogbeat)
        self.click(css=plugin_management.common_btn_commit)
        sleep(0.5)
        # 立即执行
        self.click(css=plugin_management.common_btn_commit)
        # 等待并断言
        self.assertText(settings.STATUS)
        global stop_bkunifylogbeat_url
        stop_bkunifylogbeat_url = self.get_url
        print(stop_bkunifylogbeat_url)

    def test_15_start_bkunifylogbeat(self):
        """执行启动bkunifylogbeat插件（linux主机），断言停止启动是否成功"""
        # 进入插件管理
        test_01_login.Login.test_login(self)
        test_01_login.Login.click_plug_in_management(self)
        self.is_visible(10, xpath=plugin_management.search_hostip)
        # 点击搜索框，输入IP
        self.type(xpath=plugin_management.search_hostip, text=BluekingHostIp)
        # 模拟enter键
        MyWebDriver.Keys(xpath=plugin_management.search_hostip).enter()
        # 勾选全部linux主机
        self.click(css=plugin_management.common_checkbox_tableCheckAll)
        # 点击批量插件操作
        self.click(css=plugin_management.plugin_btn_operatePlugin)
        # 启动插件选择bkunifylogbeat，下一步
        self.click(css=plugin_management.plugin_btn_start)
        self.click(css=plugin_management.plugin_select_pluginName)
        self.click(xpath=plugin_management.select_plugin_bkunifylogbeat)
        self.click(css=plugin_management.common_btn_commit)
        sleep(0.5)
        # 立即执行
        self.click(css=plugin_management.common_btn_commit)
        # 等待并断言
        self.assertText(settings.STATUS)
        start_bkunifylogbeat_url = self.get_url
        print(start_bkunifylogbeat_url)
        # 断言停止bkunifylogbeat是否成功
        custom_function.test_login_assert(self, stop_bkunifylogbeat_url)
        self.is_visible(30, xpath=plugin_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)
        # 断言启动bkunifylogbeat是否成功
        custom_function.test_login_assert(self, start_bkunifylogbeat_url)
        self.is_visible(30, xpath=plugin_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)

    def test_16_stop_bkmonitorbeat(self):
        """执行停止bkmonitorbeat插件（linux主机）"""
        test_01_login.Login.test_login(self)
        test_01_login.Login.click_plug_in_management(self)
        self.is_visible(10, xpath=plugin_management.search_hostip)
        # 点击搜索框，输入IP
        self.type(xpath=plugin_management.search_hostip, text=BluekingHostIp)
        # 模拟enter键
        MyWebDriver.Keys(xpath=plugin_management.search_hostip).enter()
        # 勾选全部linux主机
        self.click(css=plugin_management.common_checkbox_tableCheckAll)
        # 点击批量插件操作
        self.click(css=plugin_management.plugin_btn_operatePlugin)
        # 停止插件选择bkmonitorbeat，下一步
        self.click(css=plugin_management.plugin_btn_stop)
        self.click(css=plugin_management.plugin_select_pluginName)
        self.click(xpath=plugin_management.select_plugin_bkmonitorbeat)
        self.click(css=plugin_management.common_btn_commit)
        sleep(0.5)
        # 立即执行
        self.click(css=plugin_management.common_btn_commit)
        # 等待并断言
        self.assertText(settings.STATUS)
        global stop_bkmonitorbeat_url
        stop_bkmonitorbeat_url = self.get_url
        print(stop_bkmonitorbeat_url)

    def test_17_start_bkmonitorbeat(self):
        """执行启动bkmonitorbeat插件（linux主机），断言停止启动是否成功"""
        # 进入插件管理
        test_01_login.Login.test_login(self)
        test_01_login.Login.click_plug_in_management(self)
        self.is_visible(10, xpath=plugin_management.search_hostip)
        # 点击搜索框，输入IP
        self.type(xpath=plugin_management.search_hostip, text=BluekingHostIp)
        # 模拟enter键
        MyWebDriver.Keys(xpath=plugin_management.search_hostip).enter()
        self.click(css=plugin_management.common_checkbox_tableCheckAll)
        # 点击批量插件操作
        self.click(css=plugin_management.plugin_btn_operatePlugin)
        # 启动插件选择bkmonitorbeat，下一步
        self.click(css=plugin_management.plugin_btn_start)
        self.click(css=plugin_management.plugin_select_pluginName)
        self.click(xpath=plugin_management.select_plugin_bkmonitorbeat)
        self.click(css=plugin_management.common_btn_commit)
        sleep(0.5)
        # 立即执行
        self.click(css=plugin_management.common_btn_commit)
        # 等待并断言
        self.assertText(settings.STATUS)
        start_bkmonitorbeat_url = self.get_url
        print(start_bkmonitorbeat_url)
        # 断言停止bkmonitorbeat是否成功
        custom_function.test_login_assert(self, stop_bkmonitorbeat_url)
        self.is_visible(30, xpath=plugin_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)
        # 断言启动bkmonitorbeat是否成功
        custom_function.test_login_assert(self, start_bkmonitorbeat_url)
        self.is_visible(30, xpath=plugin_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)

    def test_18_stop_bkmonitorproxy(self):
        """执行停止bkmonitorproxy插件（linux主机）"""
        test_01_login.Login.test_login(self)
        test_01_login.Login.click_plug_in_management(self)
        self.is_visible(10, xpath=plugin_management.search_hostip)
        # 点击搜索框，输入IP
        self.type(xpath=plugin_management.search_hostip, text=BluekingHostIp)
        # 模拟enter键
        MyWebDriver.Keys(xpath=plugin_management.search_hostip).enter()
        # 勾选全部linux主机
        self.click(css=plugin_management.common_checkbox_tableCheckAll)
        # 点击批量插件操作
        self.click(css=plugin_management.plugin_btn_operatePlugin)
        # 停止插件选择bkmonitorproxy，下一步
        self.click(css=plugin_management.plugin_btn_stop)
        self.click(css=plugin_management.plugin_select_pluginName)
        self.click(xpath=plugin_management.select_plugin_bkmonitorproxy)
        self.click(css=plugin_management.common_btn_commit)
        sleep(0.5)
        # 立即执行
        self.click(css=plugin_management.common_btn_commit)
        # 等待并断言
        self.assertText(settings.STATUS)
        global stop_bkmonitorproxy_url
        stop_bkmonitorproxy_url = self.get_url
        print(stop_bkmonitorproxy_url)

    def test_19_start_bkmonitorproxy(self):
        """执行启动bkmonitorproxy插件（linux主机），断言停止启动是否成功"""
        # 进入插件管理
        test_01_login.Login.test_login(self)
        test_01_login.Login.click_plug_in_management(self)
        self.is_visible(10, xpath=plugin_management.search_hostip)
        # 点击搜索框，输入IP
        self.type(xpath=plugin_management.search_hostip, text=BluekingHostIp)
        # 模拟enter键
        MyWebDriver.Keys(xpath=plugin_management.search_hostip).enter()
        # 勾选全部linux主机
        self.click(css=plugin_management.common_checkbox_tableCheckAll)
        # 点击批量插件操作
        self.click(css=plugin_management.plugin_btn_operatePlugin)
        # 启动插件选择bkmonitorproxy，下一步
        self.click(css=plugin_management.plugin_btn_start)
        self.click(css=plugin_management.plugin_select_pluginName)
        self.click(xpath=plugin_management.select_plugin_bkmonitorproxy)
        self.click(css=plugin_management.common_btn_commit)
        sleep(0.5)
        # 立即执行
        self.click(css=plugin_management.common_btn_commit)
        # 等待并断言
        self.assertText(settings.STATUS)
        global start_bkmonitorproxy_url
        start_bkmonitorproxy_url = self.get_url
        print(start_bkmonitorproxy_url)
        # 断言停止bkmonitorproxy是否成功
        custom_function.test_login_assert(self, stop_bkmonitorproxy_url)
        self.is_visible(40, xpath=plugin_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)
        # 断言启动bkmonitorproxy是否成功
        custom_function.test_login_assert(self, start_bkmonitorproxy_url)
        self.is_visible(40, xpath=plugin_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)
    def test_20_stop_gsecmdline(self):
        """执行停止gsecmdline插件（linux主机）"""
        test_01_login.Login.test_login(self)
        test_01_login.Login.click_plug_in_management(self)
        self.is_visible(10, xpath=plugin_management.search_hostip)
        # 点击搜索框，输入IP
        self.type(xpath=plugin_management.search_hostip, text=BluekingHostIp)
        # 模拟enter键
        MyWebDriver.Keys(xpath=plugin_management.search_hostip).enter()
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

    def test_21_start_gsecmdline(self):
        """执行启动gsecmdline插件（linux主机），断言停止启动是否成功"""
        # 进入插件管理
        test_01_login.Login.test_login(self)
        test_01_login.Login.click_plug_in_management(self)
        self.is_visible(10, xpath=plugin_management.search_hostip)
        # 点击搜索框，输入IP
        self.type(xpath=plugin_management.search_hostip, text=BluekingHostIp)
        # 模拟enter键
        MyWebDriver.Keys(xpath=plugin_management.search_hostip).enter()
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




