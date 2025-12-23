from time import sleep
import seldom
from bk_nodeman import settings
from bk_nodeman.page import plugin_management,agent_management
from bk_nodeman.test_dir import test_01_login
class Strategy(seldom.TestCase):
    def test_01_new_strategy(self):
        """新建部署策略（选择云区域linux主机）"""
        test_01_login.Login.test_login(self)
        #点击插件部署
        self.click(xpath=plugin_management.strategy)
        sleep(0.5)
        #点击新建策略
        self.click(css=plugin_management.addpolicy)
        sleep(0.5)
        #点击新建策略
        self.click(xpath=plugin_management.go_addpolicy)
        #点击去新建策略
        self.click(css=plugin_management.common_btn_commit)
        sleep(0.5)
        #输入策略名称
        self.type(css=plugin_management.input_policyname,text=plugin_management.policyname)
        #点击自定义输入
        self.click(css=plugin_management.custom_input)
        #输入linux ip
        self.type(css=plugin_management.input_ip,text=settings.LINUX_IP_PAGENT_FIRST)
        #点击解析
        self.click(css=plugin_management.analysis)
        sleep(0.5)
        #下一步
        self.click(css=plugin_management.common_btn_stepNext)
        sleep(0.5)
        #下一步
        self.click(xpath=plugin_management.next_step)
        sleep(0.5)
        #下一步
        self.click(xpath=plugin_management.next_step_second)
        sleep(0.5)
        #立即执行
        self.click(xpath=plugin_management.execute)
        #判断执行状态
        self.is_visible(120,xpath=agent_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)
    def test_02_edit_strategy(self):
        """编辑部署策略（选择直连区域linux主机）"""
        #点击部署策略
        self.click(xpath=plugin_management.strategy)
        self.sleep(0.5)
        #搜索框搜索部署策略
        self.click(xpath=plugin_management.search_strategy)
        self.type(xpath=plugin_management.search_strategy,text=plugin_management.policyname)
        sleep(3)
        #点击编辑
        self.click(xpath=plugin_management.editpolicy)
        #点击自定义输入
        self.click(css=plugin_management.custom_input)
        #输入linux ip
        self.type(css=plugin_management.input_ip, text=settings.LINUX_IP_PAGENT_SECOND)
        #点击解析
        self.click(css=plugin_management.analysis)
        sleep(1)
        #下一步
        self.click(css=plugin_management.common_btn_stepNext)
        sleep(1)
        #下一步
        self.click(xpath=plugin_management.next_step)
        sleep(1)
        #下一步
        self.click(xpath=plugin_management.next_step_second)
        sleep(1)
        #立即执行
        self.click(xpath=plugin_management.execute)
        #判断执行状态
        self.is_visible(90,xpath=agent_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)

    def test_03_stop_strategy(self):
        """停止部署策略（停用,停用部署策略同时停用插件）"""
        #点击部署策略
        self.click(xpath=plugin_management.strategy)
        sleep(0.5)
        #搜索框搜索部署策略
        self.click(xpath=plugin_management.search_strategy)
        self.type(xpath=plugin_management.search_strategy,text=plugin_management.policyname)
        sleep(3)
        #停用,停用部署策略同时停用插件
        self.click(xpath=plugin_management.stoppolicy)
        self.click(css=plugin_management.stopplugin)
        #确定
        self.click(css=plugin_management.common_btn_commit)
        sleep(1)
        #立即执行
        self.click(css=plugin_management.common_btn_commit)
        #判断执行状态
        self.is_visible(15,xpath=agent_management.execute_successfully_install)
        self.assertText(settings.EXECUTE_SUCCESSFULLY)
    def test_04_delete_strategy(self):
        """删除部署策略"""
        #点击部署策略
        self.click(xpath=plugin_management.strategy)
        sleep(0.5)
        #搜索框搜索部署策略
        self.click(xpath=plugin_management.search_strategy)
        self.type(xpath=plugin_management.search_strategy,text=plugin_management.policyname)
        sleep(3)
        #删除部署策略
        self.click(xpath=plugin_management.deletepolicy)
        #确定删除部署策略
        self.click(xpath=plugin_management.sure_delete)
        self.assertText(plugin_management.asserttext_delete)



