import seldom

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from seldom.running.config import Seldom

from public_method import bk_exception


import sys


class SeldomMethod(seldom.TestCase):

    # def is_visible(self, timeout, **kwargs):
    #     try:
    #         WebDriverWait(Seldom.driver, timeout).until(
    #             EC.element_to_be_clickable((next(iter(kwargs)), kwargs.get(next(iter(kwargs))))))
    #         return True
    #     except TimeoutError:
    #         return False

    @staticmethod
    def confirm_element_type(element: dict):
        if not isinstance(element, dict):
            raise TypeError('输入元素类型有误')
        path = element.get('path')
        if not path:
            raise bk_exception.ElementPathError('元素定位路径为空')
        return path

    def seldom_method(self, method, element, pattern=True, **kwargs):
        try:
            path = self.confirm_element_type(element)
            if not path:
                raise bk_exception.ElementPathError('元素定位路径为空')
            if pattern is True:
                # if method == 'click':
                #     elm = WebDriverWait(self.browser, Seldom.timeout).until(EC.element_to_be_clickable((By.XPATH, path)))
                #     print(elm)
                return getattr(self, method)(xpath=path, **kwargs)
            else:
                return getattr(self, method)(css=path, **kwargs)
        except bk_exception.ElementPathError:
            raise sys.exc_info()[1]
        except Exception as e:
            print('---------页面操作-------------')
            raise bk_exception.ElementOperationError('{}操作失败,{}'.format(element.get('msg'), e)) from e

    def my_click(self, element: dict, pattern=True, **kwargs):
        self.sleep(1)
        self.seldom_method(method='click', element=element, pattern=pattern, **kwargs)
        self.check_page_error()

    def my_type(self, element: dict, pattern=True, **kwargs):
        self.seldom_method(method='type', element=element, pattern=pattern, **kwargs)

    def my_clear(self, element: dict, pattern=True, **kwargs):
        self.seldom_method(method='clear', element=element, pattern=pattern, **kwargs)

    def my_get_text(self, element: dict, pattern=True, **kwargs):
        return self.seldom_method(method='get_text', element=element, pattern=pattern, **kwargs)

    def my_double_click(self, element: dict, pattern=True, **kwargs):
        self.seldom_method(method='double_click', element=element, pattern=pattern, **kwargs)

    def my_move_to_element(self, element: dict, pattern=True, **kwargs):
        self.seldom_method(method='move_to_element', element=element, pattern=pattern, **kwargs)

    def my_type_enter(self, element: dict, pattern=True, **kwargs):
        self.seldom_method(method='type_enter', element=element, pattern=pattern, **kwargs)

    def my_get_attribute(self, element: dict, pattern=True, **kwargs):
        return self.seldom_method(method='get_attribute', element=element, pattern=pattern, **kwargs)

    def my_get_elements(self, element: dict, pattern=True, **kwargs):
        return self.seldom_method(method='get_elements', element=element, pattern=pattern, **kwargs)

    def my_keys(self, element: dict, pattern=True, **kwargs):
        return self.seldom_method(method='Keys', element=element, pattern=pattern, **kwargs)

    def my_execute_script(self, element: dict, **kwargs):
        try:
            path = self.confirm_element_type(element)
            if not path:
                raise bk_exception.ElementPathError('元素定位路径为空')
            getattr(self, 'execute_script')(script=path, **kwargs)
        except bk_exception.ElementPathError:
            raise sys.exc_info()[1]
        except Exception as e:
            print('---------页面操作-------------')
            raise bk_exception.ElementOperationError('{}操作失败,{}'.format(element.get('msg'), e)) from e

    def my_drag_and_drop_by_offset(self, element: dict, pattern=True, **kwargs):
        self.seldom_method(method='drag_and_drop_by_offset', element=element, pattern=pattern, **kwargs)

    #先放一下，后续移走
    def check_page_error(self):
        # 检查页面是否包含特定的错误信息，这里假设错误信息是 "Error" 或 "Failed"
        # error_texts = ["Error", "Failed"]
        # for error_text in error_texts:
        #     self.assertNotEqual(self.get_text(error_text), error_text, f"Page contains error text: {error_text}")

        # 检查页面是否包含特定的错误元素，这里假设错误元素的类名为 "error-message"
        # error_elements = self.find_elements(class_="error-message")
        # self.assertEqual(len(error_elements), 0, "Page contains error elements.")

        # 使用 JavaScript 检查页面是否有错误，例如检查 window.onerror 事件是否被触发
        has_error = self.execute_script("return window.onerror!== null;")
        self.assertFalse(has_error, "Page contains JavaScript errors.")

    def scroll_to_bottom(self, path_xpath):
        # 获取当前页面的高度
        last_height = self.execute_script("return document.body.scrollHeight")
        while True:
            # 滚动到页面底部
            self.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # 等待页面上的元素出现，这里假设元素的 id 是 'footer'，你可以根据实际情况修改
            self.get_element(xpath=path_xpath)
            # 计算新的页面高度
            new_height = self.execute_script("return document.body.scrollHeight")
            # 如果页面高度不再变化，说明已经滚动到底部
            if new_height == last_height:
                break
            last_height = new_height
            self.click()