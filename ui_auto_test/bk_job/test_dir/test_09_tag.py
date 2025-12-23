from public_method.login import LoginBase
from product_page.bk_job import home
from product_page.bk_job import account
from product_page import settings
from product_page.public_components import ip_choose
from public_method.base_operate import BaseOperate
from product_page.bk_job import plandetail
BaseOperate = BaseOperate()


class CreateTag(LoginBase):
    '''标签'''
    def test_01_tag(self):
        '''新建标签'''
        '''普通标签'''
        self.open(settings.JOB_URL)
        try:
            if self.my_get_elements(element=home.scroll_bar_left):
                self.my_drag_and_drop_by_offset(element=home.scroll_bar_left, x=0, y=200)
        except Exception as e:
            pass
        self.my_click(element=home.navigation_tag)
        self.sleep(2)
        self.my_click(element=account.create_tag)
        name = BaseOperate.random_data().lower()
        # settings.account_linux_name = name
        self.my_type(element=account.tag_name, text=name)
        # self.my_type(element=account.account_alias, text=name)
        self.my_type(element=account.tag_descriptions, text=name)
        self.my_click(element=account.tag_submit)
        self.assertText("新建标签成功")