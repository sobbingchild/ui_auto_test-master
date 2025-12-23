import seldom

from bk_paasv3.test_dir import test_01_login
from bk_paasv3.page import application_development
import datetime
import random


class Add_Services(seldom.TestCase):
    def test_01_add_services(self):
        """启用MySQL服务（数据存储）、启用蓝鲸APM服务（健康监测）"""
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
        # 点击查看应用概览
        self.click(xpath=application_development.application_overview)
        # 点击增强服务
        self.click(xpath=application_development.add_services)
        # 点击数据存储
        self.click(xpath=application_development.data_storage)
        # 启用MySQL服务
        self.click(xpath=application_development.start_mysql_server)
        # 断言
        self.assertText(application_development.assert_start_server_success)
        # 点击健康监测
        self.click(xpath=application_development.health_monitoring)
        # 启用蓝鲸APM服务
        self.click(xpath=application_development.start_apm_server)
        # 断言
        self.assertText(application_development.assert_start_server_success)
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

