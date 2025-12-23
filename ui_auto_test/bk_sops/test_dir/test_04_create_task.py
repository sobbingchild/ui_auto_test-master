# -*- coding: utf-8 -*-
# @Time : 2021/11/18 16:09
# @File : test_04_create_task.py

from bk_sops import settings


from public_method.login import LoginBase

from product_page.bk_sops import template_page as page

from product_page.bk_sops import index_page


class CreateTask(LoginBase):
    def test_01_create_task(self):
        '''根据模板进入查看模板并创建任务'''
        # 登录态验证
        self.open(settings.SOPS_URL)
        #self.accept_alert()
        #self._test_login(target_url=settings.SOPS_URL, index_title=settings.INDEX_TITLE)
        self.my_click(element=index_page.PROJECT_FLOW)
        #self.sleep(1)
        # 断言流程名称
        # self.type(xpath=page.search_temp_name,text=page.TEMPLATE_NAME)
        self.my_type_enter(element=page.search_temp_name,text=page.TEMPLATE_NAME)
        self.assertText(page.TEMPLATE_NAME)
        # 进入对应流程模板
        self.sleep(1)
        self.my_click(element=page.template_flow_name)
        # 断言进入查看模板
        #self.wait(3)
        self.assertText('查看流程')
        # 点击新建任务
        self.my_click(element=page.create_task_button)
        #self.wait(3)
        # 断言进入新建任务
        self.assertText('新建任务')
        self.assertText('执行方案')
        self.assertText(page.NODE_NAME)
        # 点击下一步
        self.my_click(element=page.task_next_step_button)
        print('进入任务参数填写页面')

    def test_02_input_task_parameter(self):
        '''填写任务参数'''
        # 断言进入填写参数阶段
        self.wait(5)
        self.assertText('任务信息')
        self.assertText('任务类型')
        self.assertText('参数信息')
        # 点击下一步
        self.sleep(1)
        self.my_click(element=page.form_create_task_button)
        print('任务创建成功')

    def test_03_create_task(self):
        '''执行任务并断言任务执行成功'''
        # 断言进入任务画布
        self.wait(5)
        self.assertText('未执行')
        self.my_click(element=page.task_execute_button)
        # 等待任务执行
        self.sleep(3)
        self.assertText('完成')
        print('任务执行成功')
