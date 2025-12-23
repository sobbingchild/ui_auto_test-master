# -*- coding: utf-8 -*-
# @Time : 2024/11/06 15:59
# @File : account.py

create_account = {
    'path': '//button[@data-test-id="button_createAccount"]',
    'msg': '创建账号按钮'
}

create_ticket = {
    'path': '//button[@data-test-id="button_createTicket"]',
    'msg': '创建凭证按钮'
}


create_tag = {
    'path': '//button[@data-test-id="button_createTag"]',
    'msg': '创建标签按钮'
}

create_file = {
    'path': '//button[@class="w120 bk-primary bk-button-normal bk-button"]',
    'msg': '创建文件源按钮'
}



usage_account = {
    'path': '//div[@class="radio-button-group-wraper"]//div[contains(text(),"数据库账号")]',
    'msg': '新建账号》账号用途'
}

type_account = {
    'path': '//div[@class="radio-button-group-wraper"]//div[contains(text(),"Windows")]',
    'msg': '新建账号》账号类型windows'
}

account_name = {
    'path': '//div[@class="bk-form-control"]/div[@class="bk-input-text"]/'
            'input[@placeholder="使用小写字母或 _ 开头，由 2-32 个英文字母、数字、_ 或 - 组成的字符"]',
    'msg': '账号名称'
}

ticket_name = {
    'path': '//span[@class="bk-label-text"][contains(text(),"名称")]/../../div/div/div[1]/input',
    'msg': '凭证名称'
}

tag_name = {
    'path': '//span[@class="bk-label-text"][contains(text(),"标签名称")]/../../div/div/div/div/input',
    'msg': '标签名称'
}

account_windows_name = {
    'path': '//div[@class="bk-form-control"]/div[@class="bk-input-text"]/input[@placeholder="由1~32个大小写字母、数字或-组成的字符"]',
    'msg': 'windows账号名称'
}

account_mysql_name = {
    'path': '//div[@class="bk-form-control"]/div[@class="bk-input-text"]/input[@placeholder="由1~16个大小写字母 / 数字 / . / - / _ 组成的字符"]',
    'msg': 'windows账号名称'
}

account_alias = {
    'path': '//div[@class="bk-form-control"]/div[@class="bk-input-text"]/input[@placeholder="在出现同名账号的情况下，账号的别名显得格外重要..."]',
    'msg': '账号别名'
}

account_descriptions = {
    'path': '//textarea[@class="bk-form-textarea textarea-maxlength"]',
    'msg': '账号描述'
}

ticket_descriptions = {
    'path': '//textarea[@class="bk-form-textarea textarea-maxlength"]',
    'msg': '凭证描述'
}

tag_descriptions = {
    'path': '//textarea[@class="bk-form-textarea textarea-maxlength"]',
    'msg': '标签描述'
}

ticket_password = {
    'path': '//span[@class="bk-label-text"][contains(text(),"密码")]/../../div/div/div[1]/input',
    'msg': '凭证密码'
}

ticket_type = {
    'path': '//div[@class="bk-select-name"]',
    'msg': '凭证密码类型'
}

ticket_type_username = {
    'path': '//ul[@class="bk-options bk-options-single"]/li[2]',
    'msg': '凭证密码类型>>用户名+密码'
}

ticket_type_secretKey = {
    'path': '//ul[@class="bk-options bk-options-single"]/li[3]',
    'msg': '凭证密码类型>>单一SecretKey'
}

ticket_type_appid = {
    'path': '//ul[@class="bk-options bk-options-single"]/li[4]',
    'msg': '凭证密码类型>>AppID+SecretKey'
}

ticket_username = {
    'path': '//span[@class="bk-label-text"][contains(text(),"用户名")]/../../div/div/div[1]/input',
    'msg': '凭据>用户名'
}

ticket_secretKey = {
    'path': '//span[@class="bk-label-text"][contains(text(),"SecretKey")]/../../div/div/div[1]/input',
    'msg': '凭据>SecretKey'
}

ticket_appid = {
    'path': '//span[@class="bk-label-text"][contains(text(),"AppId")]/../../div/div/div[1]/input',
    'msg': '凭据>AppID+SecretKey'
}

file_id = {
    'path': '//span[@class="bk-label-text"][contains(text(),"文件源标识")]/../../div/div/div[1]/input',
    'msg': '文件源标识'
}

file_alias = {
    'path': '//span[@class="bk-label-text"][contains(text(),"文件源别名")]/../../div/div/div[1]/input',
    'msg': '文件源别名'
}

file_url = {
    'path': '//span[@class="bk-label-text"][contains(text(),"制品库根地址")]/../../div/div/div[1]/input',
    'msg': '制品库根地址'
}

file_public_checkbox = {
    'path': '//span[@class="bk-label-text"][contains(text(),"制品库根地址")]/../../div/div/div[1]/input',
    'msg': '是否设为公共存储--默认开启'
}

file_shareobject_input = {
    'path': '//div[@class="share-object-box"]/div/div/div/div',
    'msg': '共享对象'
}

file_shareobject_select = {
    'path': '//span[@class="bk-option-name"][contains(text(),"BlueKing")]',
    'msg': '共享对象选择=>BlueKing'
}

file_shareobject_all = {
    'path': '//span[@class="bk-checkbox-text"][contains(text(),"全业务")]/../span[1]',
    'msg': '共享对象选择=>全业务'
}

file_ticket_input = {
    'path': '//span[@class="bk-label-text"][contains(text(),"身份凭证")]/../../div/div/div/div/div',
    'msg': '身份凭证'
}

file_ticket_select = {
    'path': '//ul[@class="bk-options bk-options-single"]/li[1]/div',
    'msg': '身份凭证选择=>第一条'
}




account_submit = {
    'path': '//span[contains(text(),"提交")]',
    'msg': '新建账号》提交按钮'
}

tag_submit = {
    'path': '//span[@class="bk-label-text"][contains(text(),"标签名称")]/../../../../../../div[4]/button[1]/div/span',
    'msg': '新建标签》提交按钮'
}

account_passw = {
    'path': '//div[@class="bk-input-password"]/input[@placeholder="输入密码"]',
    'msg': 'windows系统账号密码'
}

account_passw_confirm = {
    'path': '//div[@class="bk-input-password"]/input[@placeholder="输入确认密码"]',
    'msg': 'windows系统账号再次确认密码'
}

account_port = {
    'path': '//div[@class="bk-input-number"]/input[@class="bk-form-input"]',
    'msg': '新建账号》端口号'
}

del_account = {
    'path': '//div[@class="bk-table-fixed-body-wrapper"]//button[@data-test-id="button_deleteAccount"]',
    'msg': '删除账号按钮'
}

