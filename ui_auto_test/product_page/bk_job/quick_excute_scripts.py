choose_hosts = {
    'path': '//div[@class="task-step-execute-target only-host"]//button/div/span[contains(text(),"添加服务器")]',
    'msg': '添加服务器'
}

choose_agent = {
    'path': '/html/body/div[7]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div[2]/div[1]/div[1]/table/tbody/tr[1]/td[1]/span/label/span',
    'msg': '选择第一个服务器'
}

choose_host_confirm = {
    'path': '//div[@class="bk-dialog-wrapper"]//span/button[@class="bk-primary bk-button-normal bk-button"]',
    'msg': '确认选择的IP button'
}

name_quick_script = {
    'path': '//div[@class="jb-input form-item-content"]//div[@class="bk-input-text"]/input',
    'msg': '快速执行脚本》脚本名称'
}

name_quick_file = {
    'path': '//button/div/span[contains(text(),"添加服务器文件")]',
    'msg': '添加服务器文件'
}

name_source_file = {
    'path': '//button/div/span[contains(text(),"添加文件源文件")]',
    'msg': '添加文件源文件'
}

input_source_file_path_first = {
    'path': '//div[contains(text(),"对象存储")]/../../td[2]/div/button/div/span',
    'msg': '文件源文件一级目录'
}

input_source_file_path_second = {
    'path': '//button/div/span[contains(text(),"blueking")]',
    'msg': '文件源文件二级目录'
}

input_source_file_path_third = {
    'path': '//button/div/span[contains(text(),"bknodeman")]',
    'msg': '文件源文件三级目录'
}

input_source_file = {
    'path': '//span[contains(text(),"t-1.3.tgz")]/../../../../td[1]/div/label',
    'msg': '文件源文件选择'
}

input_confirm_source_file = {
    'path': '//div[contains(text(),"选择文件源文件")]/../../div[4]/button[1]',
    'msg': '确认提交源文件选择'
}

add_one_row = {
    'path': '//button/div/span[contains(text(),"添加一行")]',
    'msg': '文件分发》添加一行'
}

input_file_path = {
    'path': '//div[@class="job-smart-input-area"]',
    'msg': '文件分发》文件路径'
}

input_outgiving_path = {
    'path': '//input[@placeholder="请填写分发路径"]',
    'msg': '文件分发》分发路径'
}

add_file_host = {
    'path': '//div[@class="server-add-only-host-btn"]',
    'msg': '文件分发》分发服务器'
}

select_account = {
    'path': '//div[@class="bk-form-content"]//div[@class="form-item-content"]//div[@class="bk-select-name"]',
    'msg': '选择账户'}

select_root = {
    'path': '//ul/li/div[contains(.,"root")]',
    'msg': '选择root'
}

button_excute_script = {
    'path': '//button[@data-test-id="button_fastExecuteScriptSubmit"]',
    'msg': '执行'
}

button_excute_file = {
    'path': '//button[@data-test-id="button_fastPushFileSubmit"]',
    'msg': '分发文件执行'
}

script_reference = {
    'path': '//label[@class="bk-form-radio-button"]/div[contains(text(),"脚本引用")]',
    'msg': '脚本引用'
}

script_custom = {
    'path': '//label[@class="bk-form-radio-button"]/div[contains(text(),"手工录入")]',
    'msg': '手工录入'
}

script_select = {
    'path': '//div[@data-placeholder="选择引用脚本"]',
    'msg': '选择引用脚本'
}

time_out = {
    'path': '//div[@class="bk-input-number"]/input[@class="bk-form-input"]',
    'msg': '超时时间'
}

relaunch = {
    'path': '//div[@class="action"]/div[contains(.,"去重做")]',
    'msg': '去重做'
}

retry_all = {
    'path': '//span[text()="全部重试"]',
    'msg': '全部重试'
}

ignore_error = {
    'path': '//span[text()="忽略错误"]',
    'msg': '忽略错误'
}

ok_button = {
    'path': '//button[@class="confirm-option-button bk-primary bk-button-small bk-button"]/div/span[contains(text(),"确定")]',
    'msg': '确认按钮'
}


def choice_script(script_name):
    script = {'path': '//div[contains(text(),"{}")]'.format(script_name),
              'msg': '选择引用的脚本'
              }
    return script