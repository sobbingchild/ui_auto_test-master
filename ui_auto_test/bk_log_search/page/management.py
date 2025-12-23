# 管理
management = '//ul/li[@data-test-id="topNavBox_li_manage"]'
# 新建采集项
create_log_collection = '//button[@data-test-id="logCollectionBox_button_addNewCollectionItem"]'
# 采集项名称
log_collection_name = '//div[@data-test-id="baseMessage_input_fillName"]/div[1]/input'
log_collection_name_Chinese = '新建采集项测试'
# 采集项英文名称
log_collection_name_English = '//div[@data-test-id="baseMessage_input_fillEnglishName"]/div[1]/input'
log_collection_name_fillEnglishName = 'create_log_collection_test_'
# 数据分类
selectDataClassification = '//div[@data-test-id="sourceLogBox_div_selectDataClassification"]/div'
# 主机设备
host_devices = '//ul/li[3]/div'
# 选择目标
addCollectionTarget = '//button[@data-test-id="sourceLogBox_button_addCollectionTarget"]'
# 手动输入
selfdefined_input = '/html/body//div/div/div/div/div[2]/div/div[1]/div/div[1]/div[5]/span'
# 输入框
input_box = '//div/div[1]/div/div[1]/div/div[1]/div[1]/textarea'
# 解析
analysis = '//div/div[1]/div/div[1]/div/div[3]/button[1]/div/span'
# 确定
confirm = '//div[3]/div/span/button/div/span'
# 日志路径
logpath = '//div[@data-test-id="sourceLogBox_input_addLogPath"]/div[1]/input'
logpath_name = '/var/log/messages'
# 下一步
nextPage = '//button[@title="开始采集"]'
nextStep = '//button[@data-test-id="collectionDistribution_button_nextStep"]'
# 跳过
Pass = '//button[@data-test-id="fieldExtractionBox_button_Pass"]'
# 集群
cluster = '//div[1]/div[3]/table/tbody/tr[1]/td[1]/div/label/input'
# 完成
accomplish = '//button[@data-test-id="storageBox_button_nextPage"]'
# 检索
search = '//div[3]/table/tbody/tr[1]/td[8]/div/div/span[1]/button/div/span'
# 清除、搜索条件
query_input = '//div[@data-test-id="dataQuery_input_checkForPhrases"]/div[1]/textarea'
search_condition = 'log : HTTP'
# 查询
filterSearch = '//button[@data-test-id="dataQuery_button_filterSearch"]'
# 原始
original = '//div/div[2]/div[3]/div[2]/div/div[1]/div[1]/button[2]'
# 更多
more = '//tbody/tr[1]/td[8]/div/div/div/div[1]/i'
# 停用
block_up = '//table/tbody/tr[1]/td[8]/div/div/div/div[3]/ul/li[2]'
# 确认停用
sure_block_up = '//section/div[1]/section[2]/div[1]/div[2]/button[1]'
# 删除采集项
delete_log_collection = '//table/tbody/tr[1]/td[8]/div/div/div/div[3]/ul/li[3]'
# 确认删除采集项
sure_delete_log_collection = '/html/body/div[10]/div/div/div/div[4]/div/button[1]/div/span'
# 分隔符
separator = '//button[@data-test-id="fieldExtractionBox_button_filterMethodbk_log_delimiter"]'
# 请选择
please_select = '//div[@data-test-id="fieldExtractionBox_div_selectSeparator"]/div'
# 竖线
long_string = '//div[2]/div/div/div/ul/li[1]/div/div'
# 调试
debug = '//button[@data-test-id="fieldExtractionBox_button_debugging"]/div/span'
# 隐藏
conceal_first = '//div[2]/form/div/div[3]/table/tbody/tr[5]/td[6]/div/span'
conceal_second = '//div[2]/form/div/div[3]/table/tbody/tr[4]/td[6]/div/span'
conceal_thirdly = '//div[2]/form/div/div[3]/table/tbody/tr[3]/td[6]/div/span'
conceal_fourthly = '//div[2]/form/div/div[3]/table/tbody/tr[2]/td[6]/div/span'
# 字段名
field_name = '//div[3]/table/tbody/tr/td[1]/div/div/div/div/div[1]/input'
# 下一步
button_nextPage = '//button[@data-test-id="fieldExtractionBox_button_nextPage"]/div/span'
button_nextStep = '//div/button[@data-test-id="collectionDistribution_button_nextStep"]'
# 返回列表
button_backToList = '//button[@data-test-id="finishBox_button_backToList"]/div/span'
# 搜索名称
search_name = '//input[@placeholder="搜索名称、存储索引名"]'
# 编辑
edit = '//div[3]/table/tbody/tr[1]/td[8]/div/div/button/div/span'

# 断言
assert_status = '正常'
assert_success = '成功'
assert_create_success = "采集项创建完成"
assert_message = '/var/log/messages'
assert_block_up = "采集项停用完成"