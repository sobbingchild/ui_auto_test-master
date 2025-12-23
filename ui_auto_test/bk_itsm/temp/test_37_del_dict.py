# -*- coding: utf-8 -*-
# @Time : 2021/1/25 14:58
# @File : test_37_del_dict.py
# @Project : ITSM_257

import seldom
import sys
import time

sys.path.append("../")
import settings

dict_name = 'ui_auto_test'


class DelDict(seldom.TestCase):
    def test_del_dict(self):
        try:
            self.get(settings.ITSM_URL)
            self.set_window(1920, 1080)
            self.wait(3)
            if self.get_title == settings.LOGIN_TITLE_ENGLISH:
                self.click(xpath='//*[@id="language-form"]/a')
                time.sleep(3)
            if self.get_title == settings.LOGIN_TITLE:
                # 输入账号
                self.type(xpath='//input[@id="user"]', text=settings.USER_NAME)
                # 输入密码
                self.type(xpath="//input[@id='password']", text=settings.PASSWORD)
                self.click(xpath='//button[@id="login-btn"]')
                self.wait(3)
                self.assertTitle(settings.INDEX_TITLE)
            else:
                self.get(settings.ITSM_URL)
                self.assertTitle(settings.INDEX_TITLE)
        except Exception as e:
            return print("登录失败")
        # 跳转到后台管理
        self.click(xpath='//ul[@class="nav-list"]/li[3]')
        self.wait(3)
        assert self.get_text(xpath='//p[@class="bk-come-back"]') == '服务'
        time.sleep(1)
        self.click(xpath='//div[@class="navigation-sbmenu-title"]/span[2]', index=1)
        self.wait(3)
        # 点击数据字典
        self.click(xpath='//div/a[9]')
        self.wait(1)
        assert self.get_text(xpath='//div[@class="is-title"]/p') == '数据字典'
        self.type(xpath='//input[@placeholder="请输入编码"]', text=dict_name)
        self.Keys(xpath='//input[@placeholder="请输入编码"]').enter()
        self.wait(1)
        self.click(xpath='//span[@title="ui_auto_test"]/../../../td//button[2]')
        assert self.get_text(xpath='//div[@class="header"]') == '确认删除此数据字典？'
        self.click(xpath='//button[@name="confirm"]')
        self.wait(1)
        self.assertText('删除成功')


if __name__ == "__main__":
    seldom.main(debug=True)
