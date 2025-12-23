# -*- coding: utf-8 -*-
# @Time : 2021/12/1 14:31
# @File : test_07_create_mini_app.py

from bk_sops import settings

from public_method.login import LoginBase

from product_page.bk_sops import mini_app_page as page

from product_page.bk_sops import template_page
from product_page.bk_sops import periodic_task_page
from product_page.bk_sops import index_page


class CreateMiniApp(LoginBase):
    def test_01_create_mini_app(self):
        ''' 创建轻应用 '''
        # 登录态验证
        #self._test_login(target_url=settings.SOPS_URL, index_title=settings.INDEX_TITLE)
        self.open(settings.SOPS_URL)
        # 跳转到轻应用页面
        self.my_click(element=index_page.MINI_APP)
        self.my_click(element=page.mini_app_form_create_button)
        #self.wait(3)
        self.assertText('新建轻应用')
        # 选择流程模板
        self.my_click(element=page.template_select_div)
        #self.wait(3)
        self.my_click(element=page.template_name)
        # 点击确认创建轻应用
        self.my_click(element=page.form_confirm_button)
        self.assertText(template_page.TEMPLATE_NAME)
        print('轻应用创建成功')

    # 删除轻应用
    def test_02_delete_mini_app(self):
        ''' 删除轻应用'''
        self.sleep(1)
        self.my_move_to_element(element=page.mini_app_content)
        self.my_move_to_element(element=page.mini_app_operation)
        self.my_click(element=page.mini_app_delete_button, index=2)
        self.assertText('确认删除轻应用')
        self.my_click(element=periodic_task_page.confirm_button)
        if settings.ENVIRONMENT == False:
            self.assertText('什么是轻应用？')
        print('轻应用删除成功')
