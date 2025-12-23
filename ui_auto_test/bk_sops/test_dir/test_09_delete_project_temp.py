from public_method.login import LoginBase

from bk_sops import settings

from product_page.bk_sops import index_page

from product_page.bk_sops import template_page as page

from product_page.bk_sops import periodic_task_page

from bk_sops.bk_exception import AssertText


# 搜索创建的模板并删除
class DeleteTemplate(LoginBase):

    def test_01_search_template_flow(self):
        ''' 搜索流程模板'''
        # 登录态验证
        #self._test_login(target_url=settings.SOPS_URL, index_title=settings.INDEX_TITLE)
        self.open(settings.SOPS_URL)
        self.my_click(element=index_page.PROJECT_FLOW)
        # 断言进入了流程模板页面
        self.sleep(1)
        self.assertText('流程')
        self.my_type_enter(element=page.search_temp_name, text=page.TEMPLATE_NAME)
        # 判断是否搜索成功
        self.sleep(1)
        # 加入了收藏按钮 导致索引增加
        temp_name = self.my_get_text(element=page.template_list_name, index=1)
        if temp_name != page.TEMPLATE_NAME:
            raise AssertText('搜索模板名称与创建不符')
        print('搜索成功')

    def test_02_delete_template(self):
        """删除流程模板"""
        # 勾选当前页面中第一个流程模板
        self.my_click(element=page.form_checkbox)
        self.wait(3)
        # 展开批量操作
        # self.show_delete_drop_down_box()
        # self.my_click(element=page.batch_operation)
        self.my_click(element=page.delete_button)
        # self.wait(3)
        self.assertText('确认删除所选的 1 项流程吗?')
        self.my_click(element=periodic_task_page.confirm_button)
        # 删除成功后等待加载页面
        self.sleep(1)
        self.assertText('搜索结果为空')
        print('删除流程成功')
