# -*- coding: utf-8 -*-
# @Time : 2025/01/13 15:59
# @File : alert_routing.py

alert_routing = {
    'path': '//div[@class="bk-navigation-menu-group"]//span[@class="nav-menu-item"][contains(text(),"告警分派")]',
    'msg': '侧边导航》告警分派'
}

alert_create_routing = {
    'path': '//button/div/span[contains(text(),"新建")]',
    'msg': '新建'
}

alert_routing_name = {
    'path': '//form[@class="bk-form bk-form-vertical"]/div[1]//input[@placeholder="请输入"]',
    'msg': '新建》告警分派名称'
}

alert_routing_team = {
    'path': '//div[@class="tag-list"]/span[contains(text(),"选择告警组")]',
    'msg': '新建》选择告警组'
}

alert_routing_team_search = {
    'path': '//div[@class="bk-select-search-wrapper"]/input[@placeholder="输入关键字搜索"]',
    'msg': '新建》选择告警组》搜索框'
}

alert_routing_match_rule = {
    'path': '//div[@class="rule-line-item"]/span[contains(text(),"选择条件")]',
    'msg': '新建》匹配规则'
}

alert_routing_match_rule_search = {
    'path': '//div[@class="common-condition-component-pop-wrap key-type"]//input[@placeholder="输入关键字搜索"]',
    'msg': '新建》匹配规则》匹配下拉搜索'
}

alert_routing_match_rule_name = {
    'path': '//div[@class="common-condition-component-pop-wrap key-type"]/div[@class="wrap-list"]/div[1]',
    'msg': '新建》匹配规则》选择策略名称'
}

alert_routing_match_rule_condition = {
    'path': '//div[@class="common-condition-component-pop-wrap"]/div/div[1]/span[contains(text(),"=")]',
    'msg': '新建》匹配规则》选择规则'
}

alert_routing_match_rule_value_search = {
    'path': '//div[@class="common-condition-component-pop-wrap"]/div[@class="search-wrap"]//div[@class="bk-input-text"]/input[@placeholder="输入关键字搜索"]',
    'msg': '新建》匹配规则》选择结果搜索'
}

alert_routing_match_rule_value = {
    'path': '//div[@class="common-condition-component-pop-wrap"]/div[@class="wrap-list"]//span[@class="strategy-name-info"]',
    'msg': '新建》匹配规则》选择结果'
}

alert_routing_notification_expand = {
    'path': '//tr[@class="process-list"]/td[3]/div/div[@class="merge icon-expand"]',
    'msg': '新建》如何分派》展开'
}

alert_routing_notification_search = {
    'path': '//div[@class="table-data-row-item alarm-group-select-wrap action-id-wrap"]/div[@data-placeholder="请选择"]',
    'msg': '新建》如何分派》选择'
}

alert_routing_notification_name = {
    'path': '//li[@class="bk-option"]/div[1]/div[@class="bk-option-content-default"]',
    'msg': '新建》如何分派》选择一个名称'
}

alert_routing_debug_save = {
    'path': '//button/div/span[contains(text(),"调试并生效")]',
    'msg': '新建》调试并生效按钮'
}

alert_routing_save = {
    'path': '//button/div/span[contains(text(),"保存")]',
    'msg': '新建》保存'
}