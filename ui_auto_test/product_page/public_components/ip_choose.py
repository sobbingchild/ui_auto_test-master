choose_agent = {
    'path': '//div[@class="talbe-content not-empty"]/table/tbody/tr[1]/td[1]',
    'msg': '选择第一个IP'
}

choose_two_agent = {
    'path': '//div[@class="talbe-content not-empty"]//tr[2]/td[1][@class="columu-fixed"]',
    'msg': '选择第二个IP'
}

choose_host_confirm = {
    'path': '//span/button[@class="bk-primary bk-button-normal bk-button"]',
    'msg': '确认选择的IP button'
}

search = {
    'path': '//div/textarea[@class="input-box"]',
    'msg': 'IP选择器搜索框'
}

del_icon_search = {
    'path': '//i[@class="tag-clear bk-icon icon-close"]',
    'msg': '删除搜索框内的内容'
}

host_search_confirm = {
    'path': '//td[contains(@class, "search-suggest-item-label") and contains(., "OS 名称： ")]',
    'msg': '通过OS搜索确认'
}

first_agent_ip = {
    'path': '//div[@class="talbe-content not-empty"]/table/tbody/tr[1]/td[2]/div/span/span[1]',
    'msg': '选择筛选出来的第一台机器'
}

search_total = {
    'path': '//div[contains(text(),"共计")]',
    'msg': '搜索结果条数'
}


#服务器搜索类型
host_search_input = 'linux'
# 滚动条
scroll_bar = "//div[@class='jb-navigation-main']/div[@class='scroll-faker']/div[@class='scrollbar-vertical']/div[@class='scrollbar-inner']"