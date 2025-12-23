import seldom

from bk_paasv3.access_test_dir import test_01_login
from bk_paasv3.page import application_development
import datetime
import random
from public_method.keyboard_operation import MyWebDriver
from time import sleep

class Application_Visual(seldom.TestCase):
    def test_01_create_application_visual(self):
        """创建普通应用（基于可视化开发平台）"""
        # 进入首页
        test_01_login.Login.test_login(self)
        # 创建应用
        self.click(xpath=application_development.create_application)
        # 点击蓝鲸可视化开发平台
        self.click(xpath=application_development.visual_plaform)
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
        # 创建应用
        self.click(xpath=application_development.sure_create_application)
        # 断言
        self.assertText(application_development.assert_create_success)

    def test_02_delete_application_visual(self):
        """删除普通应用"""
        # 进入首页
        test_01_login.Login.test_login(self)
        # 点击应用开发
        self.click(xpath=application_development.application_development)
        # 搜索框搜索应用
        self.type(xpath=application_development.search_application, text=application_name)
        sleep(3)
        # 模拟enter键
        MyWebDriver.Keys(xpath=application_development.search_application).enter()
        sleep(3)
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
