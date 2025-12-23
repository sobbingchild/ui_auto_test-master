# -*- coding: utf-8 -*-
# @Time : 2021/12/1 16:47
# @File : test_08_delete_project_task.py


from public_method.login import LoginBase

from bk_sops import settings

from product_page.bk_sops import periodic_task_page

from product_page.bk_sops import index_page

from product_page.bk_sops import clocked_task_page

from public_method import bk_exception

from product_page.bk_sops import template_page

periodic_task_status = True
clocked_task_status = True


class DeleteFlow(LoginBase):

    def test_01_check_periodic_task(self):
        '''等待50S后 检查周期任务是否执行成功并执行了大于一次任务'''
        #self._test_login(target_url=settings.SOPS_URL, index_title=settings.INDEX_TITLE)
        self.open(settings.SOPS_URL)
        # self.wait(5)
        # 进入周期任务
        self.my_click(element=index_page.PERIODIC_TASKS)
        self.sleep(55)
        self.refresh()
        # self.wait(3)
        text = self.my_get_text(element=periodic_task_page.running_time)
        if text == '--':
            global periodic_task_status
            periodic_task_status = False
            raise bk_exception.BluekingException('周期任务执行次数不足')
        print('周期任务执行成功')

    def test_02_delete_periodic_task(self):
        ''' 删除周期任务 '''
        # self.wait(1)
        if not periodic_task_status:
            raise bk_exception.BluekingException('周期任务执行有误，暂停删除任务数据')
        self.sleep(1)
        self.my_click(element=periodic_task_page.delete_periodic_task_button, index=1)
        # elf.wait(3)
        self.assertText('确认删除')
        self.sleep(1)
        self.my_click(element=periodic_task_page.confirm_button)
        self.assertText('周期任务删除成功')
        print('删除周期任务成功')

    def test_03_check_clocked_task(self):
        ''' 断言计划任务是否创建实例成功'''
        # 断言进入任务画布
        # 进入计划任务页面
        self.my_click(element=index_page.CLOCKED_TASK)
        self.assertText('新建')
        self.sleep(1)
        self.refresh()
        self.wait(3)
        try:
            self.assertText('{}_计划执行'.format(template_page.TEMPLATE_NAME))
        except Exception as e:
            print('计划任务创建失败，断言无数据{}'.format(e))
            global clocked_task_status
            clocked_task_status = False
        try:
            text = self.my_get_text(element=clocked_task_page.task_instance)
            assert text == '已执行'
        except Exception as e:
            clocked_task_status = False
            raise bk_exception.BluekingException('计划任务执行/启动失败{}'.format(e))
        print('计划任务执行成功')

    def test_04_delete_clocked_task(self):
        ''' 删除计划任务 '''
        if not clocked_task_status:
            raise bk_exception.BluekingException('计划任务执行/启动失败,暂停删除任务')
        self.click_text('删除')
        # self.my_click(element=clocked_task_page.delete_clocked_task_button)
        self.wait(3)
        self.assertText('确认删除')
        self.sleep(1)
        self.my_click(element=periodic_task_page.confirm_button)
        self.assertText('计划任务删除成功')
        print('删除计划任务成功')

    def show_delete_drop_down_box(self):
        self.execute_script(
            "document.querySelector(\
            'div.operation-btn > \
            div:nth-child(3) > \
            div.bk-dropdown-content.left-align\
            ').classList.add('is-show')"
        )
