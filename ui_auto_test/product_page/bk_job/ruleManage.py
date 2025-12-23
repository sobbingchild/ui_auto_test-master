Syntax_detection_expression = {
    'path': '//span[@class="bk-label-text"][contains(text(),"语法检测表达式")]/../../div/div/div[1]/input',
    'msg': '语法检测表达式'
}

Rule_description = {
    'path': '//span[@class="bk-label-text"][contains(text(),"规则说明")]/../../div/div/div[1]/input',
    'msg': '规则说明'
}

Script_type = {
    'path': '//span[@class="bk-label-text"][contains(text(),"脚本类型")]/../../div/div/div[1]/div/div',
    'msg': '脚本类型'
}

Action = {
    'path': '//span[@class="bk-label-text"][contains(text(),"动作")]/../../div/div/div[1]/div/div',
    'msg': '动作'
}

Type_all = {
    'path': '//span[@class="bk-option-name"][contains(text(),"全选")]',
    'msg': '脚本类型=>全选'
}

Type_bat = {
    'path': '//span[@class="bk-option-name"][contains(text(),"Bat")]',
    'msg': '脚本类型=>Bat'
}

Type_shell = {
    'path': '//span[@class="bk-option-name"][contains(text(),"Shell")]',
    'msg': '脚本类型=>Shell'
}

Action_Type_Scan = {
    'path': '//span[@class="bk-option-name"][contains(text(),"扫描")]',
    'msg': '动作类型=>扫描'
}

Action_Type_Intercept = {
    'path': '//span[@class="bk-option-name"][contains(text(),"拦截")]',
    'msg': '动作类型=>拦截'
}

Save_button = {
    'path': '//div[@class="jb-sideslider-footer"]/button[1]',
    'msg': '保存按钮'
}

Rule_text = 'rm -rf'
Description_text = 'UI自动化测试'