from public_method.login import LoginBase
from product_page.bk_job import home
from product_page.bk_job import account
from product_page import settings
from public_method.base_operate import BaseOperate
BaseOperate = BaseOperate()


class CreateFileManager(LoginBase):
    '''标签'''
    def test_01_FileManager(self):
        '''新建文件源'''
        '''设为公共存储的文件源'''
        self.open(settings.JOB_URL)
        try:
            if self.my_get_elements(element=home.scroll_bar_left):
                self.my_drag_and_drop_by_offset(element=home.scroll_bar_left, x=0, y=200)
        except Exception as e:
            pass
        self.my_click(element=home.navigation_fileManage)
        self.sleep(2)
        self.my_click(element=account.create_file)
        name = BaseOperate.random_data()
        self.my_click(element=account.type_account)
        self.my_type(element=account.file_id, text=name)
        self.my_type(element=account.file_alias, text=name)
        self.my_type(element=account.file_url, text=name)
        # self.my_click(element=account.file_public_checkbox)
        self.my_click(element=account.file_shareobject_input)
        self.my_click(element=account.file_shareobject_select)

        self.my_click(element=account.file_ticket_input)
        self.my_click(element=account.file_ticket_select)

        self.my_click(element=account.account_submit)
        self.assertText("新建公共存储的文件源成功")

    def test_02_FileManager(self):
        '''新建文件源'''
        '''设为非公共存储的文件源'''
        # self.open(settings.JOB_URL)
        # self.my_click(element=home.navigation_fileManage)
        # self.sleep(2)
        self.my_click(element=account.create_file)
        name = BaseOperate.random_data()
        self.my_click(element=account.type_account)
        self.my_type(element=account.file_id, text=name)
        self.my_type(element=account.file_alias, text=name)
        self.my_type(element=account.file_url, text=name)

        self.my_click(element=account.file_public_checkbox)
        self.my_click(element=account.file_ticket_input)
        self.my_click(element=account.file_ticket_select)

        self.my_click(element=account.account_submit)
        self.assertText("新建非公共存储的文件源成功")

    def test_03_FileManager(self):
        '''新建文件源'''
        '''设为公共存储的文件源,全业务'''
        # self.open(settings.JOB_URL)
        # self.my_click(element=home.navigation_fileManage)
        # self.sleep(2)
        self.my_click(element=account.create_file)
        name = BaseOperate.random_data()
        self.my_click(element=account.type_account)
        self.my_type(element=account.file_id, text=name)
        self.my_type(element=account.file_alias, text=name)
        self.my_type(element=account.file_url, text=name)
        # self.my_click(element=account.file_public_checkbox)
        self.my_click(element=account.file_shareobject_all)
        self.my_click(element=account.file_ticket_input)
        self.my_click(element=account.file_ticket_select)

        self.my_click(element=account.account_submit)
        self.assertText("新建公共存储的文件源,全业务成功")

