# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_06_job_temp.py
   Description :
   date：          2024/7/9
-------------------------------------------------
"""

from public_method.login import LoginBase
from product_page.bk_job import home
from product_page.bk_job import operation
from product_page import settings
from product_page.public_components import ip_choose
from product_page.bk_job import navigation
from public_method.base_operate import BaseOperate
from product_page.bk_job import plandetail
BaseOperate = BaseOperate()



# 不依赖IP
class JobTemp(LoginBase):
    '''作业模板'''
    def test_01_create_job_temp(self):
        '''新建作业模板，添加模板名称'''
        self.open(settings.JOB_URL)
        # 进入作业模板
        self.my_click(element=home.jobs)
        # 新建作业模板
        self.my_click(element=operation.template_create)
        # 断言是否进入新建作业模板
        self.wait(5)
        self.assertText('新建作业模板')
        # 输入作业模板名称
        name = BaseOperate.random_data()
        settings.temp_input = name
        self.my_type(element=operation.temp_name_input, text=name)


    def test_02_create_global_variable(self):
        '''作业模板新建全局变量'''
        self.assertText('新建作业模板')
        value = BaseOperate.random_data()
        # 新增字符串全局变量
        self.add_variable(operation.str_div, value)
        # 勾选赋值可变
        self.my_click(element=operation.assign_variable)
        # 提交
        self.my_click(element=operation.variable_submit)
        self.assertText(value)
        value = BaseOperate.random_data()
        # 新增命名空间变量
        self.add_variable(operation.name_space, value)
        # 提交
        self.my_click(element=operation.variable_submit)
        self.assertText(value)
        value = BaseOperate.random_data()
        # 新增密文变量
        self.add_variable(operation.cipher_text, value)
        # 提交
        self.my_click(element=operation.variable_submit)
        self.wait(3)
        self.assertText(value)
        value = BaseOperate.random_data()
        # 新增数组变量
        self.add_variable(operation.array_variable, value)
        # 勾选赋值可变
        self.my_click(element=operation.assign_variable)
        # 提交
        self.my_click(element=operation.variable_submit)
        self.wait(3)
        self.assertText(value)
        value = BaseOperate.random_data()
        # 新增主机列表变量
        self.add_variable(operation.host_list, value)
        self.my_click(element=operation.variable_submit)
        self.wait(2)
        self.assertText(value)

    # 作业步骤
    def test_03_add_job_steps(self):
        '''增加作业步骤'''
        self.my_click(element=operation.steps_jobs)
        self.assertText('新建作业步骤')
        # 输入脚本内容
        self.my_type(element=navigation.script_content, text=navigation.SCRIPT_TEXT)
        #self.execute_script(page.js_script)
        # 保存作业步骤
        self.my_click(element=operation.variable_submit)
        self.assertText('执行脚本')
        self.my_click(element=operation.submit)
        self.assertText('作业创建成功')

    def test_04_edit_temp(self):
        '''编辑作业模板'''
        # 跳转作业模板地址
        self.open(settings.JOB_URL)
        self.my_click(element=home.jobs)
        self.my_type(element=ip_choose.search, text=settings.temp_input)
        self.sleep(1)
        self.Keys(xpath=ip_choose.search['path']).enter()
        self.my_click(element=operation.tags_temp)
        self.my_click(element=operation.temp_more)
        self.my_click(element=operation.edit_temp)
        self.wait(3)
        self.my_click(element=operation.steps_jobs)
        self.wait(2)
        self.assertText('新建作业步骤')
        # 修改步骤类型
        #self.click(xpath=page.script_execution)
        # 选择人工确认
        self.my_click(element=operation.edit_temp_confirmation)
        self.wait(2)
        # 点击保存
        self.my_click(element=operation.variable_submit)
        # 保存作业模板
        self.my_click(element=operation.submit)
        self.assertText('编辑保存成功')

    def test_05_clone_temp(self):
        '''克隆作业模板'''
        # 跳转作业模板地址
        self.open(settings.JOB_URL)
        self.my_click(element=home.jobs)
        self.my_type(element=ip_choose.search, text=settings.temp_input)
        self.sleep(1)
        self.Keys(xpath=ip_choose.search['path']).enter()
        self.my_click(element=operation.tags_temp)
        self.my_click(element=operation.temp_more)
        self.my_click(element=operation.copy_temp)
        self.my_click(element=operation.got_it)
        self.assertText('克隆作业模板')
        # 提交克隆的作业模板
        self.my_click(element=operation.submit)
        self.wait(3)
        self.assertText('作业创建成功')

    def test_06_check_temp(self):
        '''作业模板创建成功》查看作业模板'''
        # 立即查看作业模板
        self.my_click(element=operation.check_temp)
        # 断言是否跳转到查看作业模板
        self.sleep(1)
        self.assertText('查看作业模板')
        # 断言模板名称是否带copy
        self.assertText('copy')
        # 删除克隆模板
        self.my_click(element=operation.check_del_temp)
        self.my_click(element=operation.confirm_button)
        self.assertText("全部作业")

    def test_07_debug_launch_temp(self):
        '''调试作业模板'''
        self.open(settings.JOB_URL)
        self.my_click(element=home.jobs)
        self.my_type(element=ip_choose.search, text=settings.temp_input)
        self.sleep(1)
        self.Keys(xpath=ip_choose.search['path']).enter()
        self.my_click(element=operation.tags_temp)
        # 点击调试
        self.my_click(element=operation.debug_temp)
        # 断言是否进入调试页面
        self.assertText('调试')
        self.my_click(element=operation.launch_button)
        # 断言跳转到设置全局变量页面
        self.assertText('设置全局变量')
        self.my_click(element=operation.launch_global_button)
        self.my_click(element=operation.continue_launch)
        self.my_click(element=operation.confirm_button)
        # 断言跳转到作业执行详情页面
        self.assertText('作业执行详情')
        # 确定执行
        self.sleep(1)
        # 断言执行成功
        self.assertText('执行成功')

    def test_08_plans_temp(self):
        '''执行方案'''
        self.open(settings.JOB_URL)
        self.my_click(element=home.jobs)
        self.my_type(element=ip_choose.search, text=settings.temp_input)
        self.sleep(1)
        self.Keys(xpath=ip_choose.search['path']).enter()
        self.my_click(element=operation.tags_temp)
        # 点击执行方案
        self.my_click(element=operation.plandetail_temp)
        # 断言是否进入调试页面
        self.assertText('我的方案')
        self.sleep(1)
        self.my_click(element=plandetail.plan_create)
        self.sleep(1)
        self.my_click(element=plandetail.plan_create_submit)
        # 断言跳转到作业执行详情页面
        self.assertText('操作成功')

    def add_variable(self, variable_obj, variable_name):
        '''全局变量类型'''
        self.my_click(element=operation.global_variables)
        self.assertText('新建全局变量')
        # 选择变量类型
        self.my_click(element=variable_obj)
        # 输入变量名称
        self.my_type(element=operation.name_variables, text=variable_name)
        self.wait(2)
        if '主机列表' not in variable_obj['path']:
            # 输入初始值
            self.my_type(element=operation.default_value, text=variable_name)
        else:
            # 点击选择主机
            self.my_click(element=operation.select_host)
            self.my_click(element=ip_choose.choose_agent)
            self.my_click(element=ip_choose.choose_host_confirm)
        self.wait(2)
