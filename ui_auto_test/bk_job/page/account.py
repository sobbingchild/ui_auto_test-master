# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     account.py
   Description : 
   Author :       v_adanchen
   date：          2021/9/18
-------------------------------------------------
"""
from bk_job import settings

navigation_accountManage = "//div[@data-test-id='navigation_accountManage']"
new_account = "//div[@class='list-action-layout']/div/button"
# 名称
name = "//div[@class='bk-form-control']/div[@class='bk-input-text']/input[@placeholder='由小写字母或下划线开头，和 2~32个字母 / 数字 / _ 或 - 组成的字符']"
# 别名
alias = "//div[@class='bk-form-control']/div[@class='bk-input-text']/input[@placeholder='在出现同名账号的情况下，账号的别名显得格外重要...']"
# 提交
commit_new = "//div[@class='bk-sideslider-footer']/div/button[1]"
# 编辑
edit = '//div[@class="bk-table-fixed-right"]//button[@data-test-id="button_editAccount"]'
# 搜索
search = "//div[@class='search-input-box']/textarea"
# 账号别名
search_account = "//tbody/tr[1]/td/div[contains(.,'{}')]".format(settings.TEST_ALIAS_ACCOUNT)
# 删除
del_account = '//div[@class="bk-table-fixed-right"]//button[@data-test-id="button_deleteAccount"]'
# 确定删除
del_comfirm = "//div[@class='jb-popover-content']/div[@class='confirm-options']/button[1]"
