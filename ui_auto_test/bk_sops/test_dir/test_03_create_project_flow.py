# -*- coding: utf-8 -*-
# @Time : 2021/11/10 17:48
# @File : test_03_create_project_flow.py


from bk_sops import settings

# from bk_sops.access_test_dir.test_01_login import LoginBase

from product_page.bk_sops import template_page as page
from product_page.bk_sops import index_page
from public_method.login import LoginBase
# from public_method.keyboard_operation import MyWebDriver


class CreateFlow(LoginBase):
    def test_01_create_template(self):
        '''创建流程模板'''
        # 登录态验证
        #self._test_login(target_url=settings.SOPS_URL, index_title=settings.INDEX_TITLE)
        self.open(settings.SOPS_URL)
        # self._test_login()
        # 点击进入项目流程
        self.my_click(element=index_page.PROJECT_FLOW)
        # 断言是否进入到SOPS_UI项目
        if settings.BIZ_NAME not in self.my_get_text(element=page.select_biz_name):
            self.my_click(element=page.select_biz_name)
            # self.wait(1)
            self.my_type(element=page.biz_input, text=settings.BIZ_NAME)
            # self.sleep(1)
            self.my_click(element=page.select_biz)
            print('切换业务成功')
        self.sleep(1)
        self.my_click(element=page.create_template_button)
        # self.execute_script(page.create_template_button)
        self.assertText('新建流程')
        self.assertText('保存并新建任务')
        print('进入流程创建模板画布')

    def test_02_create_node(self):
        ''' 选择定时插件创建流程节点'''
        self.my_double_click(element=page.flow_node)
        # self.wait(3)
        # 选择蓝鲸通知类插件
        self.my_click(element=page.list_bk)
        # 获取当前节点名称
        page.NODE_NAME = self.my_get_text(element=page.sleep_timer)
        # 选择定时插件
        self.my_click(element=page.sleep_timer)
        # self.wait(1)
        # 断言进入节点配置
        self.assertText('节点配置')
        # 输入定时时间
        self.my_click(element=page.timer_input)
        self.sleep(3)
        self.my_type(element=page.timer_input, text='1')
        # 保存节点
        self.my_click(element=page.node_save_button)
        # 编辑流程名称
        print('流程节点创建成功')

    def test_03_edit_template_name(self):
        ''' 修改模板名称并保存模板'''
        self.my_click(element=page.template_base_message)
        self.my_double_click(element=page.template_name)
        #MyWebDriver.Keys(xpath=page.template_name['path']).delete()
        self.my_keys(element=page.template_name).delete()
        # self.my_keys(element=page.template_name).delete()
        self.my_type(element=page.template_name, text=page.TEMPLATE_NAME)
        self.my_click(element=page.template_base_message_save_button)
        # 保存流程模板
        self.my_click(element=page.template_save_button)
        print('流程模板创建成功')
