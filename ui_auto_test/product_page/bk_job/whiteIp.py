select_biz = {
    'path': '//div[@class="app-wraper"]/div/div/div/div',
    'msg': '目标业务'
}

all_biz = {
    'path': '//div[@class="app-wraper"]/label/span[1]',
    'msg': '全业务'
}

input_biz = {
    'path': '//span[@class="bk-option-name"][contains(text(),"BlueKing")]',
    'msg': '选择BlueKing业务'
}

whiteIp_choose_hosts = {
    'path': '//button[@class="bk-default bk-button-normal bk-button"]/div/span[contains(text(),"添加服务器")]',
    'msg': '添加服务器'
}

whiteIp_choose_agent = {
    'path': '//div[@class="host-table"]/div[2]/div[1]/div[1]/table/tbody/tr[1]/td[1]/span/label',
    'msg': '选择第一个服务器'
}


whiteIp_choose_host_confirm = {
    'path': '//div[@class="bk-dialog-wrapper"]//span/button[@class="bk-primary bk-button-normal bk-button"]',
    'msg': '确认选择的IP button'
}

input_remark = {
    'path': '//div[@class="bk-textarea-wrapper"]/textarea',
    'msg': '备注信息'
}

effective_range_execution = {
    'path': '//span[@class="bk-label-text"][contains(text(),"生效范围")]/../../div/div/label[1]/span[1]',
    'msg': '生效范围=>脚本执行'
}

effective_range_files = {
    'path': '//span[@class="bk-label-text"][contains(text(),"生效范围")]/../../div/div/label[2]/span[1]',
    'msg': '生效范围=>文件分发'
}


remark_text = 'UI自动化测试'