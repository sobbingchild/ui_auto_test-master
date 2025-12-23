# -*- coding: utf-8 -*-
# @Time : 2025/01/09 15:59
# @File : alert_solutions.py

alert_solutions = {
    'path': '//div[@class="bk-navigation-menu-group"]//span[@class="nav-menu-item"][contains(text(),"处理套餐")]',
    'msg': '侧边导航》处理套餐'
}

alert_solutions_create = {
    'path': '//button[@class="bk-primary bk-button-normal bk-button add-btn"]',
    'msg': '处理套餐》新建'
}

alert_solutions_name = {
    'path': '//div[@class="verify-item-wrap"]/div/div/input[@placeholder="请输入"]',
    'msg': '处理套餐》新建》名称输入框'
}

alert_solutions_type = {
    'path': '//div[@class="common-item-component"]/div/div[@data-placeholder="选择"]',
    'msg': '新建》套餐类型下拉框'
}

alert_solutions_type_name = {
    'path': '//div[@class="meal-options"]/span[contains(text(),"HTTP回调")]',
    'msg': '新建》套餐类型》HTTP回调'
}

alert_solutions_request_url = {
    'path': '//div[@class="bk-input-text"]/input[@placeholder="输入请求 URL"]',
    'msg': '新建》套餐类型》HTTP回调》URL'
}

alert_solutions_request_url_debug = {
    'path': '//div/span[contains(text(),"调试")]',
    'msg': '新建》套餐类型》HTTP回调》URL'
}

alert_solutions_debug_button = {
    'path': '//div[@class="bk-dialog-footer"]//span[contains(text(),"调试")]',
    'msg': '新建》套餐类型》HTTP回调》URL'
}

alert_solutions_request_url_debug_done = {
    'path': '//div[@class="status-operate"]/button[@class="bk-default bk-button-normal bk-button"]',
    'msg': '新建》套餐类型》HTTP回调》调试完成'
}

alert_solutions_save = {
    'path': '//div[@class="operate-warpper"]/button[@class="bk-primary bk-button-normal bk-button"]',
    'msg': '新建》保存'
}

alert_solutions_search = {
    'path': '//div[@class="bk-input-text"]/input[@placeholder="搜索套餐名称 / 类型 / 修改人"]',
    'msg': '搜索'
}

alert_solutions_search_name = {
    'path': '//div[@class="meal-name-div"]/div[@class="meal-name"]',
    'msg': '搜索》名称'
}
