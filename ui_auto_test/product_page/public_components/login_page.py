# -*- coding: utf-8 -*-
# @Time : 2021/7/22 15:59
# @File : login_page.py


LOGIN_TITLE_ENGLISH = 'Login | Tencent BlueKing'

LOGIN_TITLE = '登录 | 蓝鲸智云'
# 切换中英文按钮
switch_language_ee = '//*[@id="language-form"]/a'
switch_language_ce = '//span[@id="ch"]'

# 账户名input框
account = '//input[@id="user"]'
# 密码input框
password = "//input[@id='password']"
# 登录button
login_button = '//button[@id="login-btn"]'
# login页面图片
Login_photo = '//div[@class="logo-title"]/img'

# notice 弹窗
# notice_alert_windows = '//div[@class="bk-dialog-header"]'
notice_alert_windows = '//div[@class="bk-dialog-content bk-dialog-content-drag" and @style="width: 480px;"]/div[@class="bk-dialog-header"]'
# notice 弹窗 确认关闭
notice_alert_button = '//div[@class="bk-dialog-content bk-dialog-content-drag" and @style="width: 480px;"]//button'
#关闭版本说明弹窗
CLOSS_VERSION = '/html/body/div[3]/div[2]/div/div/i[@class="bk-dialog-close bk-icon icon-close"]'
VERSION_WINDOWS = '/html/body/div[3]/div[2]/div/div/div[2]'

##woa元素
quick_login = '//div/input[@id="btn_smartlogin"]'
