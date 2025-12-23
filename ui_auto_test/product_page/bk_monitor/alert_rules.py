# -*- coding: utf-8 -*-
# @Time : 2025/01/09 15:59
# @File : alert_rules.py

alert_rules = {
    'path': '//div[@class="bk-navigation-menu-group"]//span[contains(text(),"告警策略")]',
    'msg': '侧边导航》告警策略'
}

alert_new = {
    'path': '//button[@class="bk-primary bk-button-normal bk-button header-btn mc-btn-add"]'
            '//span[contains(text(),"新建")]',
    'msg': '告警策略》新建'
}

alert_new_name = {
    'path': '//div[@class="bk-form-control with-right-icon base-config-input simplicity-input"]'
            '/div[@class="bk-input-text"]/input',
    'msg': '告警策略》新建》告警名称'
}

alert_new_priority = {
    'path': '//div[@class="bk-form-control with-right-icon base-config-input simplicity-input"]'
            '/div[@class="bk-input-number"]/input',
    'msg': '告警策略》新建》优先级'
}

alert_new_metrics = {
    'path': '//div//li[@id="set-panel-item-time_series"]',
    'msg': '告警策略》新建》指标数据'
}

alert_new_metrics_add = {
    'path': '//div[@class="form-content monitor-input metric-wrap"]',
    'msg': '告警策略》新建》指标数据》新增'
}

alert_new_metrics_search = {
    'path': '//*[@class="subtitle"][contains(text(),"磁盘空间使用率")]',
    'msg': '告警策略》新建》指标数据》搜索'
}

alert_new_static = {
    'path': '//div[@class="type-list-item"]/span[contains(text(),"静态阈值")]',
    'msg': '告警策略》新建》指标数据》静态阈值'
}

alert_new_handling = {
    'path': '//span[@class="btn-content"]/span/span[contains(text(),"选择添加告警场景")]',
    'msg': '告警策略》新建》选择添加告警场景'
}

alert_new_handling_triggered = {
    'path': '//div[@class="bk-option-content"]/div[@title="告警触发时"]',
    'msg': '新建》选择添加告警场景》告警触发时'
}

alert_new_handling_triggered_select = {
    'path': '//div[@class="group-select-component select-warp"]/div[@class="select-wrap is-hover"]',
    'msg': '新建》选择添加告警场景》选择'
}

alert_new_handling_triggered_search = {
    'path': '//div[@class="bk-input-text"]/input[@placeholder="输入关键字"]',
    'msg': '新建》选择添加告警场景》搜索'
}

alert_new_handling_triggered_search_save = {
    'path': '//ul[@class="panel-item child-item"]/li[@class="list-item"]',
    'msg': '新建》确定套餐'
}

alert_new_alarm_team = {
    'path': '//span[@class="add-tag"]/span[contains(text(),"添加告警组")]',
    'msg': '告警策略》新建》指标数据》添加告警组'
}

alert_new_alarm_team_search = {
    'path': '//input[@placeholder="输入关键字搜索"]',
    'msg': '告警策略》新建》搜索告警组'
}

alert_new_add_ip = {
    'path': '//div[@class="ip-wrapper-title"][contains(text(),"添加监控目标")]',
    'msg': '告警策略》新建》搜索告警组'
}

alert_new_collapse = {
    'path': '//span[@class="nav-append-wrap"]/span[@class="icon-monitor icon-audit active"]',
    'msg': '告警策略》新建》预览数据按钮'
}

alert_new_submit = {
    'path': '//button//span[contains(text(),"提交")]',
    'msg': '告警策略》新建》提交按钮'
}

alert_rules_search = {
    'path': '//div[@class="search-container-input"]/div[@class="div-input input-before"]',
    'msg': '告警策略》搜索'
}

alert_rules_search_icon = {
    'path': '//span[@class="search-nextfix-icon"]',
    'msg': '告警策略》搜索icon'
}

alert_rules_search_name = {
    'path': '//li[@id="strategy_name"]',
    'msg': '告警策略》搜索策略名称'
}

alert_search_name = {
   'path': '//div/span/a[@class="name-text-link"]',
   'msg': '告警策略》搜索》搜索出的告警名称'
}

alert_event_icon = {
    'path': '//span[@class="alert-tag red"]/i',
    'msg': '告警策略》产生告警的icon'
}

alert_mute_icon = {
    'path': '//span[@class="alert-tag wuxian"]/i',
    'msg': '告警策略》屏蔽的icon'
}

alert_event_more = {
    'path': '//span/i[@class="bk-icon icon-more"]',
    'msg': '告警策略》列表更多'
}

alert_event_more_button = {
    'path': '//ul[@class="operator-group"]/li[contains(text(),"快捷屏蔽")]',
    'msg': '告警策略》列表更多》快捷屏蔽'
}

alert_event_more_button_del = {
    'path': '//ul[@class="operator-group"]/li[contains(text(),"删除")]',
    'msg': '告警策略》列表更多》删除'
}
alert_event_del_confirm = {
    'path': '//div[@class="bk-dialog bk-info-box"]//div[@class="footer-wrapper"]/button/div/span[contains(.,"确定")]',
    'msg': '删除》二次确定'
}

alert_rules_team = {
    'path': '//span[@class="classifiy-label"]/span[@class="text-overflow"]',
    'msg': '告警策略》点击告警组'
}

