# -*- coding: utf-8 -*-
# @Time : 2021/7/24 15:13
# @File : delete_script_page.py
# @Project : bk_job


# 上线提示文案
DELETE_ALERT_TEXT = '确定删除该脚本？'

# 删除提示
delete_alert_text = '//h2[@class="confirm-title"]'
# 确定删除button
delete_alert_button = '//button[@class="confirm-option-button bk-primary bk-button-small bk-button"]'

script_page = '//div[@data-test-id="navigation_scriptManage"]'
# 删除脚本按钮
def del_button():
    # 3.4.0修改table
    #button = "//td//span[text()='{}']/../../../../../..//button".format(script_name)
    button = '//div[@class="bk-table-fixed-right"]//table//td//button//span[contains(text(),"删除")]'
    return button
