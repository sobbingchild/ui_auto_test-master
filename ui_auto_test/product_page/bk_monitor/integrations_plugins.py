# -*- coding: utf-8 -*-
# @Time : 2025/01/09 15:59
# @File : integrations_plugins.py

create_plugins = {
    'path': '//button[@class="left-button mc-btn-add bk-primary bk-button-normal bk-button"]',
    'msg': '数据采集》新建'
}

plugins_id = {
    'path': '//div/input[@placeholder="英文"]',
    'msg': '数据采集》新建》插件id'
}

plugin_config = {
    'path': '//div[@class="line-numbers"][contains(text(),"12")]',
    'msg': '采集配置》linux'
}

plugin_config_input = {
    'path': '/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/div[6]/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/div[1]/div[4]/div[3]',
    'msg': '采集配置》linux'
}

create_plugin_next = {
    'path': '//button/div/span[contains(.,"下一步")]',
    'msg': '采集配置》linux'
}

plugin_test_probe = {
    'path': '//div[@class="item-host-ip"]/span[contains(text(),"点击选择测试目标")]',
    'msg': '采集配置》调试框点击'
}

plugin_test_probe_ip = {
    'path': '//table[@class="bk-table-body"]/tbody/tr[@data-table-row="row-0"]/td',
    'msg': '采集配置》ip选择'
}

plugin_dubug = {
    'path': '//button/div/span[contains(.,"开始调试")]',
    'msg': '采集配置》开始调试'
}

plugin_dubuging = {
    'path': '//button/div/span[contains(.,"调试中")]',
    'msg': '采集配置》开始调试'
}

plugin_save = {
    'path': '//button[@class="mc-btn-add bk-primary bk-button-normal bk-button"]/div/span[contains(.,"保存")]',
    'msg': '采集配置》保存'
}

plugin_create_closs = {
    'path': '//button[@class="mr10 bk-default bk-button-normal bk-button"]/div/span[contains(.,"关闭")]',
    'msg': '采集配置新建成功》关闭'
}

plugin_search = {
    'path': '//div[@class="bk-input-text"]/input[@placeholder="插件名称(ID或别名)"]',
    'msg': '插件》查询'
}

plugin_name_click = {
    'path': '//div[@class="desc-alias"]/span[@class="desc-alias-title"]',
    'msg': '插件》名称'
}

plugin_more = {
    'path': '//span/i[@class="bk-icon icon-more"]',
    'msg': '插件列表》更多'
}

plugin_more_del = {
    'path': '//div[@class="operator-group"]/span[contains(.,"删除")]',
    'msg': '插件列表》更多》删除'
}

plugin_more_del_comfirm = {
    'path': '//button[@class="bk-primary bk-button-normal bk-button"]/div/span[contains(.,"删除")]',
    'msg': '插件列表》更多》删除》确认'
}

