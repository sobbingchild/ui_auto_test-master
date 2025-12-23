# -*- coding: utf-8 -*-
# @Time : 2021/11/30 15:03
# @File : test_06_create_clocked_task.py


import seldom

from bk_sops import settings

import datetime

from public_method.login import LoginBase

from product_page.bk_sops import periodic_task_page

from product_page.bk_sops import clocked_task_page as page

from product_page.bk_sops import index_page


class CreateClockedTasks(LoginBase):
    def test_01_create_clocked_tasks(self):
        ''' 创建计划任务 '''
        # 登录态验证
        #self._test_login(target_url=settings.SOPS_URL, index_title=settings.INDEX_TITLE)
        self.open(settings.SOPS_URL)
        # 进入计划任务页面
        self.my_click(element=index_page.CLOCKED_TASK)
        # self.wait(5)
        self.my_click(element=page.clocked_form_create_button)
        # 断言创建计划任务侧滑框是否弹出
        self.assertText('新建计划任务')
        print('进入计划任务参数填写页面')

    def test_02_input_task_parameter(self):
        ''' 填写计划任务参数'''
        # 断言进入填写参数阶段
        self.sleep(1)
        self.my_click(element=page.clocked_template_select)
        self.my_click(element=periodic_task_page.template_name)
        # self.wait(5)
        # 断言是否自动选择执行方案
        scheme_text = self.my_get_attribute(element=page.execution_scheme,attribute='data-placeholder')
        assert scheme_text == '此流程无执行方案，无需选择'
        # self.my_type(element=page.clocked_task_name, text=template_page.TEMPLATE_NAME)
        self.assertText('参数信息')
        self.assertText('通知方式')
        self.assertText('暂无参数')
        # 输入启动时间
        self.my_type(element=page.start_time_input, text=self.create_start_time())
        # 点击下一步
        self.my_click(element=page.clocked_create_button)
        print('计划任务创建成功')

    def create_start_time(self):
        now_time = datetime.datetime.now()
        add_time_strtime = now_time + datetime.timedelta(minutes=1)
        clocked_time = add_time_strtime.strftime('%Y-%m-%d %H:%M:%S')
        print('计划任务开始时间' + clocked_time)
        return clocked_time
