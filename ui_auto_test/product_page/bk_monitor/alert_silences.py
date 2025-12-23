# -*- coding: utf-8 -*-
# @Time : 2025/01/09 15:59
# @File : alert_silences.py

alert_silences = {
    'path': '//div[@class="bk-navigation-menu-group"]//span[contains(text(),"告警屏蔽")]',
    'msg': '侧边导航》告警屏蔽'
}

alert_silences_search = {
    'path': '//bk-weweb[@id="alarmShield"]',
    'msg': '搜索'
}

alert_silences_search_button = {
    'path': '//div[@class="search-nextfix"]/span[@class="search-nextfix-icon is-focus"]',
    'msg': '搜索》搜索按钮'
}

alert_silences_unmute = {
    'path': '//button[@class="is-text bk-button-primary bk-button "]/span[contains(text(),"解除")]',
    'msg': '告警屏蔽》解除'
}

alert_silences_confirm = {
    'path': '//button[@class=" bk-button-primary bk-button "]/span[contains(text(),"确定")]',
    'msg': '告警屏蔽》解除》确定'
}

alert_silences_create = {
    'path': '//button[@class="bk-button-primary bk-button add-btn"]/span[contains(.,"新增屏蔽")]',
    'msg': '告警屏蔽》新增屏蔽'
}

silences_create_policy = {
    'path': '//button[@class="  bk-button "]/span[contains(text(),"基于策略屏蔽")]',
    'msg': '告警屏蔽》基于策略'
}

silences_search_policy = {
    'path': '//div[@class="bk-input--default resizable bk-input"]/input[@placeholder="请选择"]',
    'msg': '告警屏蔽》选择策略'
}

silences_search_policy_confirm = {
    'path': '//ul[@class="bk-select-options"]/li[1]/label[@class="bk-checkbox bk-checkbox-default bk-select-checkbox"]',
    'msg': '告警屏蔽》选择策略确定'
}

silences_severity = {
    'path': '//lable[@class="bk-checkbox bk-checkbox-default"]/span[contains(text(),"致命")]',
    'msg': '告警屏蔽》告警等级'
}

silences_time_range = {
    'path': '//input[@class="bk-date-picker-editor"]',
    'msg': '告警屏蔽》生效范围'
}

silences_time_search = {
    'path': '//span[@class="bk-date-picker-cells-cell bk-date-picker-cells-cell-selected bk-date-picker-cells-cell-today"]',
    'msg': '告警屏蔽》生效范围》当天时间'
}

silences_create_confirm = {
    'path': '//button[@class="bk-button-primary bk-button min-w88 mr8"]/span[contains(text(),"确定")]',
    'msg': '告警屏蔽》确定'
}
