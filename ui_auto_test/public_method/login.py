# -*- coding: utf-8 -*-


from public_method.base_operate import BaseOperate

from product_page.public_components import login_page

from public_method import bk_exception

from public_method.seldom_method import SeldomMethod
BaseOperate = BaseOperate()
user_name = 'admin'
passwd = BaseOperate.read_data(key='passwd')

class LoginBase(SeldomMethod):
    def _test_login(self, target_url: str, index_title: str, username=user_name, pwd=passwd):
        ''' 登录态验证'''
        if not target_url:
            raise bk_exception.LoginError('URL地址为空,target_url={}'.format(target_url))
        if not index_title:
            raise bk_exception.LoginError('请输入产品title,index_title={}'.format(index_title))
        self.open(target_url)
        self.set_window(1920, 1080)
        self.sleep(1)
        # self.wait(3)
        if self.get_title == login_page.LOGIN_TITLE_ENGLISH or self.get_title == login_page.LOGIN_TITLE:
            if self.get_title == login_page.LOGIN_TITLE_ENGLISH:
                # 判断是否社区版
                msg = self.get_attribute(xpath=login_page.Login_photo, attribute="src")
                if 'logo_ce' in msg:
                    self.click(xpath=login_page.switch_language_ce)
                else:
                    self.click(xpath=login_page.switch_language_ee)
                self.sleep(1)
                if self.get_title != login_page.LOGIN_TITLE:
                    raise bk_exception.LoginError('英文切换中文失败，登录页面有缺陷')
                self.input_username_password(username=username, pwd=pwd, title=self.get_title)
            elif self.get_title == login_page.LOGIN_TITLE:
                self.input_username_password(username=username, pwd=pwd, title=self.get_title)
            else:
                raise bk_exception.LoginError('登录页面title不符合规范,测试失败')
        else:
            self.open(target_url)
            # self.wait(3)
            self.assertInTitle(index_title)
            self.check_notice()
            self.check_version_log()

    def _test_woa_login(self, target_url: str, index_title: str):
        ''' 登录态验证'''
        if not target_url:
            raise bk_exception.LoginError('URL地址为空,target_url={}'.format(target_url))
        if not index_title:
            raise bk_exception.LoginError('请输入产品title,index_title={}'.format(index_title))
        self.open(target_url)
        self.set_window(1920, 1080)
        for i in range(10):
            if self.get_title == index_title:
                break
            try:
                self.click(login_page.quick_login)
                break
            except:
                pass
        if self.get_title == index_title:
            print("====登录成功====")
        else:
            raise bk_exception.LoginError('登录页面title不符合规范,测试失败')




    def check_notice(self):
        """
        判断消息通知是否弹窗
        """
        try:
            self.sleep(1)
            notice = self.get_element(xpath=login_page.notice_alert_windows)
            if notice:
                button_text = self.get_text(xpath=login_page.notice_alert_button)
                if '确定' in button_text:
                    self.click(xpath=login_page.notice_alert_button)
                if '下' in button_text:
                    self.click(xpath=login_page.notice_alert_button)
                    button_text = self.get_text(xpath=login_page.notice_alert_button)
                while '上' in button_text:
                    text_list = self.get_elements(xpath=login_page.notice_alert_button)
                    button_text = text_list[len(text_list) - 1].text
                    self.click(xpath=login_page.notice_alert_button, index=1)
                print('已确认notice')
        except Exception as e:
            if login_page.notice_alert_button in e.args[0]:
                raise bk_exception.ElementPathError(e.args[0])
            pass

    def check_version_log(self):
        '''判断是否有版本日志弹窗'''
        try:
            #VERSION_WINDOWS = self.get_element(xpath=login_page.VERSION_WINDOWS)
            if self.get_element(xpath=login_page.VERSION_WINDOWS):
                self.click(xpath=login_page.CLOSS_VERSION)
        except Exception as e:
            pass

    def input_username_password(self, username, pwd, title):
        # 输入账号
        self.type(xpath=login_page.account, text=username)
        # 输入密码
        self.type(xpath=login_page.password, text=pwd)
        self.click(xpath=login_page.login_button)
        self.sleep(1)
        if title != self.get_title:
            print("{}--登录成功".format(username))
            self.check_notice()
            self.check_version_log()
        else:
            raise bk_exception.LoginError('密码账号错误，登录失败')




    # def is_visible(self, timeout, **kwargs):
    #     try:
    #         WebDriverWait(Seldom.driver, timeout).until(
    #             EC.element_to_be_clickable((next(iter(kwargs)), kwargs.get(next(iter(kwargs))))))
    #         return True
    #     except TimeoutError:
    #         return False
    #
    # @staticmethod
    # def confirm_element_type(element: dict):
    #     if not isinstance(element, dict):
    #         raise TypeError('输入元素类型有误')
    #     path = element.get('path')
    #     if not path:
    #         raise bk_exception.ElementPathError('元素定位路径为空')
    #     return path
    #
    # def seldom_method(self, method, element, pattern=True, **kwargs):
    #     try:
    #         path = self.confirm_element_type(element)
    #         if not path:
    #             raise bk_exception.ElementPathError('元素定位路径为空')
    #         if pattern is True:
    #             return getattr(self, method)(xpath=path, **kwargs)
    #         else:
    #             return getattr(self, method)(css=path, **kwargs)
    #     except bk_exception.ElementPathError:
    #         raise sys.exc_info()[1]
    #     except Exception as e:
    #         print('---------页面操作-------------')
    #         raise bk_exception.ElementOperationError('{}操作失败,{}'.format(element.get('msg'), e)) from e
    #
    # def my_click(self, element: dict, pattern=True, **kwargs):
    #     self.seldom_method(method='click', element=element, pattern=pattern, **kwargs)
    #
    # def my_type(self, element: dict, pattern=True, **kwargs):
    #     self.seldom_method(method='type', element=element, pattern=pattern, **kwargs)
    #
    # def my_clear(self, element: dict, pattern=True, **kwargs):
    #     self.seldom_method(method='clear', element=element, pattern=pattern, **kwargs)
    #
    # def my_get_text(self, element: dict, pattern=True, **kwargs):
    #     return self.seldom_method(method='get_text', element=element, pattern=pattern, **kwargs)
    #
    # def my_double_click(self, element: dict, method, pattern=True, **kwargs):
    #     self.seldom_method(method=method, element=element, pattern=pattern, **kwargs)
    #
    # def my_move_to_element(self, element: dict, method, pattern=True, **kwargs):
    #     self.seldom_method(method=method, element=element, pattern=pattern, **kwargs)
    #
    # def my_type_enter(self, element: dict, method, pattern=True, **kwargs):
    #     self.seldom_method(method=method, element=element, pattern=pattern, **kwargs)
    #
    # def my_get_attribute(self, element: dict, method, pattern=True, **kwargs):
    #     return self.seldom_method(method=method, element=element, pattern=pattern, **kwargs)
    #
    # def my_execute_script(self, element: dict, method, **kwargs):
    #     try:
    #         path = self.confirm_element_type(element)
    #         if not path:
    #             raise bk_exception.ElementPathError('元素定位路径为空')
    #         getattr(self, method)(script=path, **kwargs)
    #     except bk_exception.ElementPathError:
    #         raise sys.exc_info()[1]
    #     except Exception as e:
    #         print('---------页面操作-------------')
    #         raise bk_exception.ElementOperationError('{}操作失败,{}'.format(element.get('msg'), e)) from e
    #
    # def my_drag_and_drop_by_offset(self, element: dict, method, pattern=True, **kwargs):
    #     self.seldom_method(method=method, element=element, pattern=pattern, **kwargs)
