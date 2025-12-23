import seldom

from bk_paasv3.test_dir import test_01_login
from bk_paasv3.page import application_development
from public_method.keyboard_operation import MyWebDriver
import datetime
import random


class Application_Visual(seldom.TestCase):
    def test_01_create_application_visual(self):
        """创建普通应用（基于可视化开发平台）"""
        # 进入首页
        test_01_login.Login.test_login(self)
        # 创建应用
        self.click(xpath=application_development.create_application)
        # 新建应用ID
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        char = random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(
            alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(
            alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(
            alphabet)
        self.type(xpath=application_development.application_id, text=application_development.testchar + char)
        # 应用名称
        global application_name
        application_name = application_development.testchar + str(datetime.datetime.now().month) + str(
            datetime.datetime.now().day) + char
        self.type(xpath=application_development.application_name, text=application_name)
        # 蓝鲸可视化开发平台
        self.click(xpath=application_development.visual_plaform)
        # 创建应用
        self.click(xpath=application_development.sure_create_application)
        # 断言
        self.assertText(application_development.assert_create_success)

    def test_02_modify_the_configuration_rest(self):
        """修改运行时配置、重置生效环境"""
        # 进入首页
        test_01_login.Login.test_login(self)
        # 点击应用开发
        self.click(xpath=application_development.application_development)
        # 搜索框搜索应用
        self.type(xpath=application_development.search_application, text=application_name)
        # 模拟enter键
        MyWebDriver.Keys(xpath=application_development.search_application).enter()
        # 应用
        self.click(xpath=application_development.click_application)
        # 应用引擎
        self.click(xpath=application_development.application_engine)
        # 环境配置
        self.click(xpath=application_development.environment_configuration)
        # 修改运行时配置
        self.click(xpath=application_development.config)
        # 选择Python
        self.click(xpath=application_development.select_python)
        # 确定
        self.click(xpath=application_development.confirm)
        # 断言
        self.assertText(application_development.assert_success)
        # 点击所有环境
        self.click(xpath=application_development.all_environmental)
        # 重置
        self.click(xpath=application_development.reset)

    def test_03_environment_configuration(self):
        """新建/编辑/删除环境变量配置、修改主模板设置"""
        # 进入首页
        test_01_login.Login.test_login(self)
        # 点击应用开发
        self.click(xpath=application_development.application_development)
        # 搜索框搜索应用
        self.type(xpath=application_development.search_application, text=application_name)
        # 模拟enter键
        MyWebDriver.Keys(xpath=application_development.search_application).enter()
        # 应用
        self.click(xpath=application_development.click_application)
        # 应用引擎
        self.click(xpath=application_development.application_engine)
        # 环境配置
        self.click(xpath=application_development.environment_configuration)
        # 输入环境变量配置KEY、VALUE、
        self.type(xpath=application_development.environment_variable_key, text='TEST_1')
        self.type(xpath=application_development.environment_variable_value, text='1')
        self.click(xpath=application_development.add_environment_variable)
        # 编辑环境变量配置
        self.click(xpath=application_development.edit_environment_variable_config)
        self.type(xpath=application_development.environment_variable_content, text='测试')
        self.click(xpath=application_development.submit_content)
        self.assertText(application_development.assert_submit_success)
        # 删除环境变量配置
        self.click(xpath=application_development.delete_environment_variable_config)
        # 确定
        self.click(xpath=application_development.sure_delete)
        self.assertText(application_development.assert_delete_environment)
        # 点击访问入口
        self.click(xpath=application_development.access_entry)
        # 点击修改主模块设置
        self.click(xpath=application_development.edit_main_module_settings)
        self.assertText(application_development.assert_main_module_settings)

    def test_04_delete_application_visual(self):
        """删除普通应用"""
        # 进入首页
        test_01_login.Login.test_login(self)
        # 点击应用开发
        self.click(xpath=application_development.application_development)
        # 搜索框搜索应用
        self.type(xpath=application_development.search_application, text=application_name)
        # 模拟enter键
        MyWebDriver.Keys(xpath=application_development.search_application).enter()
        # 点击应用
        self.click(xpath=application_development.click_application)
        # 点击基本设置
        self.click(xpath=application_development.basic_setup)
        # 点击基本信息
        self.click(xpath=application_development.basic_information)
        # 删除应用
        self.click(xpath=application_development.delete_application)
        # 获取文本
        textmessage = self.get_text(xpath=application_development.get_the_text)
        # 输入文本信息
        self.type(xpath=application_development.input_text_message, text=textmessage)
        # 确定
        self.click(xpath=application_development.sure)
        # 断言
        self.assertText(application_development.assert_delete_applicatin)
