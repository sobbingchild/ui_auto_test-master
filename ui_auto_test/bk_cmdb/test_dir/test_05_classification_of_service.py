from time import sleep
from bk_cmdb.page import business
import seldom
from bk_cmdb import settings
from bk_cmdb.test_dir import test_01_login
from public_method.keyboard_operation import MyWebDriver


class Classification_Of_Service(seldom.TestCase):
    def test_01_new_service(self):
        """新建一级、二级服务分类"""
        # 进入首页，点击业务
        test_01_login.Login.test_login(self)
        sleep(1)
        test_01_login.Login.click_business(self)
        sleep(1)
        self.click(xpath=business.businessselector)
        # 等待后输入业务id并点击
        sleep(1)
        self.type(css=business.select_search_input, text=settings.BUSINESS_NAME_CMDB)
        self.click(xpath=business.option_name)
        # 点击服务分类
        self.click(css=business.menu_name_service)
        sleep(1)
        # 点击+号,输入服务分类并确定
        self.click(css=business.addmain)
        self.type(css=business.placeholder_first, text=business.first_service)
        self.click(css=business.button_confirm)
        self.assertText(business.assert_success)
        sleep(1)
        # 点击添加，输入二级服务分类，确定
        self.click(xpath=business.addmain_second)
        self.type(css=business.placeholder_second, text=business.second_service)
        self.click(css=business.button_confirm)
        self.assertText(business.assert_success)
    def test_02_delete_service(self):
        """删除一级、二级服务分类"""
        # 鼠标悬浮事件，悬浮后点击删除
        self.move_to_element(xpath=business.move_second_service)
        # self.is_visible(5, xpath=business.delete_second_service)
        self.click(xpath=business.delete_second_service)
        sleep(1)
        # 确定删除二级服务分类
        self.click(xpath=business.sure_delete_secondservice)
        sleep(1)
        # 断言
        self.assertText(business.assert_delete)
        # 鼠标悬浮事件，悬浮后点击删除
        self.move_to_element(xpath=business.move_first_service)
        self.click(xpath=business.delete_first_service)
        sleep(1)
        # 确认删除分类，断言
        self.click(xpath=business.sure_delete_firstservice)
        self.assertText(business.assert_delete)

    def test_03_edit_service(self):
        """修改一级、二级服务分类名称"""
        # 点击+号,输入服务分类并确定
        self.click(css=business.addmain)
        self.type(css=business.placeholder_first, text=business.first_service)
        self.click(css=business.button_confirm)
        self.assertText(business.assert_success)
        sleep(1)
        # 点击添加，输入二级服务分类，确定
        self.click(xpath=business.addmain_second)
        self.type(css=business.placeholder_second, text=business.second_service)
        self.click(css=business.button_confirm)
        self.assertText(business.assert_success)
        # 点击一级服务分类
        self.click(xpath=business.click_first_service)
        # 修改一级服务分类名称
        MyWebDriver.Keys(css=business.placeholder_first).backspace()
        self.type(css=business.placeholder_first, text=settings.SERVICE_CATEGORY_NAME)
        # 点击确定，断言
        self.click(css=business.button_confirm)
        self.assertText(business.assert_success)
        # 鼠标悬浮事件，悬浮后点击铅笔
        self.move_to_element(xpath=business.move_second_service)
        sleep(1)
        self.click(xpath=business.edit_second_service)
        sleep(1)
        # 修改二级服务分类名称
        MyWebDriver.Keys(css=business.placeholder_second).backspace()
        self.type(css=business.placeholder_second, text=settings.SERVICE_CATEGORY_NAME)
        # 点击确定，断言
        self.click(css=business.button_confirm)
        self.assertText(business.assert_success)
