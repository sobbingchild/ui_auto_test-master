import time

debug_button = {
    'path': '//button[@data-test-id="button_debugScript"]',
    'msg': '调试按钮'
}

online_button = {
    'path': '//div/div/div/div/div/button[1][@class="confirm-option-button bk-primary bk-button-small bk-button"]',
    'msg': '确认上线Button'
}

online_alert_text = {
    'path': '//h2[@class="confirm-title"]',
    'msg': '上线提示'
}

online_alert_button = {
    'path': '//button[@data-test-id="button_onlineScript"]',
    'msg': '上线button'
}

debug_run = {
    'path': '//button[@data-test-id="button_fastExecuteScriptSubmit"]',
    'msg': '调试执行按钮'
}

scriptPage_title = {
    'path': '//div[@class="page-title"]',
    'msg': '无脚本时页面下显示文案'
}

scriptPage_button = {
    'path': '//div[@class="page-action"]/button',
    'msg': '无脚本时新增脚本按钮'
}

append_button = {
    'path': '//div[@class="right-box"]/button',
    'msg': '有脚本时新增脚本按钮'
}

input_script_name = {
    'path': '//input[@type="text"]',
    'msg': '脚本名称'
}

script_description = {
    'path': '//textarea[@type="textarea"]',
    'msg': '脚本描述'
}

script_version = {
    'path': '//input[@type="text"]',
    'msg': '脚本版本'
}

script_content = {
    'path': '//textarea[@class="ace_text-input"]',
    'msg': '脚本内容'
}

submit_button = {
    'path': '//div[@role="action"]//button[1]',
    'msg': '提交按钮'
}

python_click = {
    'path': '//div[contains(text(),"Python")]',
    'msg': '切换python脚本'
}

perl_click = {
    'path': '//div[contains(text(),"Perl")]',
    'msg': '切换perl脚本'
}

bat_click = {
    'path': '//div[contains(text(),"Bat")]',
    'msg': '切换bat脚本'
}

powershell_click = {
    'path': '//div[contains(text(),"Powershell")]',
    'msg': '切换powershell脚本'
}


script_status = {
    'path': '//tbody/tr/td/div[@class="cell"]/span',
    'msg': '脚本状态'
}

del_button = {
    'path': '//div[@class="bk-table-fixed-right"]//span[contains(text(),"删除")]',
    'msg': '删除按钮'
}
##-------------公共脚本元素-----------------

create_public_script_button = {
    'path': '//div[@class="right-box"]/button[1]',
    'msg': '新建脚本按钮'
}

edit_tags_button = {
    'path': '//div[@class="right-box"]/button[2]',
    'msg': '编辑标签按钮'
}

input_public_script_name = {
    'path': '//div[@class="job-form"]/form/div[1]/div/div/div/div/div[1]/input',
    'msg': '公共脚本名称'
}

input_public_script_version = {
    'path': '//div[@class="job-form"]/form/div[4]/div/div/div/div[1]/input',
    'msg': '公共脚本版本号'
}

input_public_script_content = {
    'path': '//textarea[@class="ace_text-input"]',
    'msg': '公共脚本内容'
}

public_bat_click = {
    'path': '//div[@class="jb-ace-header"]/div[1]/div[2]',
    'msg': 'Bat类型公共脚本'
}

public_perl_click = {
    'path': '//div[@class="jb-ace-header"]/div[1]/div[3]',
    'msg': 'Perl类型公共脚本'
}

public_python_click = {
    'path': '//div[@class="jb-ace-header"]/div[1]/div[4]',
    'msg': 'Python类型公共脚本'
}

public_powershell_click = {
    'path': '//div[@class="jb-ace-header"]/div[1]/div[5]',
    'msg': 'Powershell类型公共脚本'
}

public_SQL_click = {
    'path': '//div[@class="jb-ace-header"]/div[1]/div[6]',
    'msg': 'SQL类型公共脚本'
}




##-------------脚本数据-----------------

# 脚本版本
SCRIPT_VERSION = '0.0.1'
PYTHON_SCRIPT_NAME = 'ui_python_script'
# 脚本描述
SCRIPT_TEXT = 'echo UI_AUTO_TEST'
PYTHON_SCRIPT_IMPORT = 'import time'
PYTHON_SCRIPT_SLEEP = 'time.sleep(10)'
PYTHON_SCRIPT_TEXT = 'print ("UI_AUTO_TEST")'
PERL_SCRIPT_TEXT = 'print ("UI_AUTO_TEST")'
BAT_SCRIPT_TEXT = 'print "UI_AUTO_TEST"'
POWERSHELL_SCRIPT_TEXT = 'echo UI_AUTO_TEST'


SHELL_SCRIPT_TEXT = 'echo 1'
SHELL_SCRIPT_SLEEP = 'sleep 10'
# 断言页面版本管理文字
PAGE_TEXT = '版本管理'
# 断言页面title
HTML_TITLE = '脚本管理'
# 上线提示文案
ONLINE_ALERT_TEXT = '确定上线该版本？'
#agent状态
PAGE_AGENT_STATE = '正常'
#执行状态
RUN_STATE = '执行成功'

# 公共脚本断言页面title
HTML_TITLE_PUBLIC = '公共脚本'
