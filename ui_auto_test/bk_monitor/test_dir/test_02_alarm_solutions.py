from public_method.login import LoginBase
from product_page.bk_monitor import home
from product_page.bk_monitor import alarm_solutions as solutions
from public_method.base_operate import BaseOperate
from product_page import settings
BaseOperate = BaseOperate()

class AlertSolutions(LoginBase):
    '''处理套餐'''
    def test_01_create_solutions(self):
        '''新建处理套餐'''
        self.open(settings.MONITOR_URL)
        self.my_click(home.strategy_config_navigation)
        if self.my_get_elements(element=solutions.alert_solutions):
            self.my_click(element=solutions.alert_solutions)
        else:
            self.my_click(element=home.navigation_packup)
            self.my_click(element=solutions.alert_solutions)
        self.my_click(element=solutions.alert_solutions_create)
        self.my_click(element=solutions.alert_solutions_name)
        name = BaseOperate.random_data()
        settings.solutions_name = name
        self.my_type(element=solutions.alert_solutions_name, text=name)
        self.my_click(element=solutions.alert_solutions_type)
        self.my_click(element=solutions.alert_solutions_type_name)
        self.my_click(element=solutions.alert_solutions_request_url)
        self.my_type(element=solutions.alert_solutions_request_url, text="https://www.baidu.com")
        self.sleep(1)
        self.my_click(element=solutions.alert_solutions_request_url_debug)
        self.my_click(element=solutions.alert_solutions_debug_button)
        self.sleep(3)
        self.assertText("调试成功")
        self.my_click(element=solutions.alert_solutions_request_url_debug_done)
        self.my_click(element=solutions.alert_solutions_save)
        self.assertText("添加套餐")

    def test_02_check_solutions(self):
        '''查看新建的处理套餐'''
        self.my_click(element=solutions.alert_solutions)
        self.my_click(element=solutions.alert_solutions_search)
        self.my_type(element=solutions.alert_solutions_search, text=settings.solutions_name)
        self.Keys(xpath=solutions.alert_solutions_search['path']).enter()
        self.my_click(element=solutions.alert_solutions_search_name)
        self.assertText("套餐详情")
        self.assertText("已启用")














