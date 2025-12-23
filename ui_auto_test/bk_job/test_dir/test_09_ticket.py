from public_method.login import LoginBase
from product_page.bk_job import home
from product_page.bk_job import account
from product_page import settings
from product_page.public_components import ip_choose
from public_method.base_operate import BaseOperate
from product_page.bk_job import plandetail
BaseOperate = BaseOperate()


class SoureFileTicket(LoginBase):
    '''凭证'''
    def test_01_ticket_password(self):
        '''新建凭证'''
        '''单一密码'''
        self.open(settings.JOB_URL)
        try:
            if self.my_get_elements(element=home.scroll_bar_left):
                self.my_drag_and_drop_by_offset(element=home.scroll_bar_left, x=0, y=200)
        except Exception as e:
            pass
        self.my_click(element=home.navigation_ticket)
        self.sleep(2)
        self.my_click(element=account.create_ticket)
        name = BaseOperate.random_data().lower()
        # settings.account_linux_name = name
        self.my_type(element=account.ticket_name, text=name)
        # self.my_type(element=account.account_alias, text=name)
        # self.my_click(element=account.ticket_type)
        self.my_type(element=account.ticket_password, text=name)
        self.my_type(element=account.account_descriptions, text=name)
        self.my_click(element=account.account_submit)
        self.assertText("新建单一密码凭据成功")

    def test_02_ticket_username(self):
        '''新建凭证'''
        '''用户名+密码'''
        self.open(settings.JOB_URL)
        self.my_click(element=home.navigation_ticket)
        self.sleep(2)
        self.my_click(element=account.create_ticket)
        name = BaseOperate.random_data().lower()
        # settings.account_linux_name = name
        self.my_type(element=account.ticket_name, text=name)
        # self.my_type(element=account.account_alias, text=name)
        self.my_click(element=account.ticket_type)
        self.my_click(element=account.ticket_type_username)
        self.sleep(2)
        self.my_type(element=account.ticket_username, text=name)
        self.my_type(element=account.ticket_password, text=name)
        self.my_type(element=account.account_descriptions, text=name)
        self.my_click(element=account.account_submit)
        self.assertText("新建用户名密码凭据成功")

    def test_03_ticket_secretKey(self):
        '''新建凭证'''
        '''单一secretKey'''
        self.open(settings.JOB_URL)
        self.my_click(element=home.navigation_ticket)
        self.sleep(2)
        self.my_click(element=account.create_ticket)
        name = BaseOperate.random_data().lower()
        # settings.account_linux_name = name
        self.my_type(element=account.ticket_name, text=name)
        # self.my_type(element=account.account_alias, text=name)
        self.my_click(element=account.ticket_type)
        self.my_click(element=account.ticket_type_secretKey)
        self.sleep(2)
        self.my_type(element=account.ticket_secretKey, text=name)
        self.my_click(element=account.account_submit)
        self.assertText("新建单一secretKey凭据成功")

    def test_04_ticket_appid(self):
        '''新建凭证'''
        '''AppID+SecretKey'''
        self.open(settings.JOB_URL)
        self.my_click(element=home.navigation_ticket)
        self.sleep(2)
        self.my_click(element=account.create_ticket)
        name = BaseOperate.random_data().lower()
        # settings.account_linux_name = name
        self.my_type(element=account.ticket_name, text=name)
        # self.my_type(element=account.account_alias, text=name)
        self.my_click(element=account.ticket_type)
        self.my_click(element=account.ticket_type_appid)
        self.sleep(2)
        self.my_type(element=account.ticket_appid, text=name)
        self.my_type(element=account.ticket_secretKey, text=name)
        self.my_click(element=account.account_submit)
        self.assertText("新建AppID+secretKey凭据成功")

