# -*- coding: utf-8 -*-
# @Time : 2025/01/09 15:59
# @File : integrations_collection.py

collection_navigation = {
    'path': '//span[@class="navigation-menu-item-name"]/span[contains(text(),"数据采集")]',
    'msg': '侧边导航栏》数据采集'
}

plugins_navigation = {
    'path': '//span[@class="navigation-menu-item-name"]/span[contains(text(),"指标插件")]',
    'msg': '侧边导航栏》指标插件'
}

sources_navigation = {
    'path': '//span[@class="navigation-menu-item-name"]/span[contains(text(),"告警源")]',
    'msg': '侧边导航栏》告警源'
}

metrics_navigation = {
    'path': '//span[@class="navigation-menu-item-name"]/span[contains(text(),"自定义指标")]',
    'msg': '侧边导航栏》自定义指标'
}

events_navigation = {
    'path': '//span[@class="navigation-menu-item-name"]/span[contains(text(),"自定义事件")]',
    'msg': '侧边导航栏》自定义事件'
}

import_navigation = {
    'path': '//span[@class="navigation-menu-item-name"]/span[contains(text(),"导入导出")]',
    'msg': '侧边导航栏》导入导出'
}

create_collection = {
    'path': '//button[@class="mc-btn-add bk-primary bk-button-normal bk-button"]',
    'msg': '数据采集》新建'
}

create_collection_name = {
    'path': '//div/input[@placeholder="输入采集任务名"]',
    'msg': '数据采集》新建》名称'
}

create_collection_plugins = {
    'path': '//div[@class="bk-select is-unselected is-default-trigger select-big"]',
    'msg': '数据采集》新建》插件'
}

create_collection_plugins_serach = {
    'path': '//div[@class="bk-select-search-wrapper"]/input[@class="bk-select-search-input"]',
    'msg': '数据采集》新建》插件》搜索'
}

create_collection_match = {
    'path': '//label[@class="bk-form-radio"]/div[contains(.,"命令行匹配")]',
    'msg': '数据采集》新建》命令行匹配'
}

create_collection_process = {
    'path': '//div[@class="bk-input-text"]/input[@placeholder="进程关键字"]',
    'msg': '数据采集》新建》进程关键字'
}

create_collection_host = {
    'path': '//tbody/tr/td[1]/span/label[@class="bk-form-checkbox"]',
    'msg': '数据采集》新建》IP选择'
}

create_collection_deploy = {
    'path': '//button/div/span[contains(.,"开始下发")]',
    'msg': '数据采集》新建》下发'
}

create_collection_done = {
    'path': '//button/div/span[contains(.,"完成")]',
    'msg': '数据采集》新建》完成'
}

create_collection_closs = {
    'path': '//button/div/span[contains(.,"关闭")]',
    'msg': '数据采集》新建》完关闭'
}

collection_search = {
    'path': '//div[@class="bk-input-text"]/input[@placeholder="采集配置名称/ID"]',
    'msg': '数据采集》查询'
}

collection_name_click = {
    'path': '//div/span[@class="col-name-desc"]',
    'msg': '数据采集》点击查询结果名称'
}

collection_link_state = {
    'path': '//li/div[contains(text(),"链路状态")]',
    'msg': '数据采集详情》链路状态'
}

collection_states = {
    'path': '//li/div[contains(text(),"采集状态")]',
    'msg': '数据采集详情》采集状态'
}

collection_more_del = {
    'path': '//div[@class="operator-group"]/span[contains(text(),"删除")]',
    'msg': '数据采集》更多》删除'
}

collection_more_del_confirm = {
    'path': '//button[@class="del-btn bk-primary bk-button-normal bk-button"]/div/span[contains(text(),"删除")]',
    'msg': '数据采集》更多》删除确认'
}

