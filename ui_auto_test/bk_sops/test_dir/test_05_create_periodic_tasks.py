# -*- coding: utf-8 -*-
# @Time : 2021/11/29 11:50
# @File : test_05_create_periodic_tasks.py


from bk_sops import settings

from public_method.login import LoginBase

from product_page.bk_sops import periodic_task_page as page

from product_page.bk_sops import index_page


class CreatePeriodicTasks(LoginBase):
    def test_01_create_periodic_tasks(self):
        '''创建周期任务'''
        # 登录态验证
        #self._test_login(target_url=settings.SOPS_URL, index_title=settings.INDEX_TITLE)
        self.open(settings.SOPS_URL)
        # self.accept_alert()
        # 进入周期任务
        self.my_click(element=index_page.PERIODIC_TASKS)
        # self.wait(3)
        self.my_click(element=page.periodiclist_form_create_button)
        # 断言创建周期任务侧滑是否弹出
        self.assertText('新建周期任务')
        self.sleep(1)
        # 选择创建周期任务模板
        self.my_click(element=page.select_template)
        self.my_click(element=page.template_name)
        # self.click(xpath=page.form_template_button)
        # self.click(xpath=template_page.task_next_step_button)
        print('进入周期任务参数侧滑弹出填写页面')

    def test_02_input_task_parameter(self):
        '''填写周期任务参数 1分钟执行一次'''
        # 断言进入填写参数阶段
        # 输入周期任务名称
        # self.my_type(element=page.periodic_task_name, text=template_page.TEMPLATE_NAME)
        # 断言是否自动选择执行方案
        self.sleep(1)
        scheme_text = self.my_get_attribute(element=page.execution_scheme,attribute='data-placeholder')
        assert scheme_text == '此流程无执行方案，无需选择'
        # 选择周期任务执行时间
        self.assertText('暂无参数')
        self.my_clear(element=page.crontab_span)
        self.my_type(element=page.crontab_span, text='* * * * *')
        # 点击下一步
        self.my_click(element=page.create_periodic_task_button)
        # self.assertText('创建周期任务成功')
        print('周期任务创建成功')
