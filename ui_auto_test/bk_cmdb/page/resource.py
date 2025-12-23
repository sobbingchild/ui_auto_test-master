# 搜索业务
business = '//input[@type="text"]'
# 点击业务
click_business = '//div[@title="业务"]'
# 新建业务
new = '//div[1]/div[2]/div/div[1]/div[1]/span[1]/button/div/span'
# 创建的业务名
business_name = '//div[1]/div/div[2]/ul/li[1]/div[2]/div/div[1]/input'
# 点击用户名
click_username = '//div/div[2]/ul/li[1]/div[2]/div/div/div/div'
# 用户名
username = '//div/div[2]/ul/li[1]/div[2]/div/div/div/div/span'
# 确认用户名
sure_username = '//*[@id="tippy-1"]/div/div/div/ul/li/span[2]'
# 提交
commit = '//div[2]/section/div/div[2]/div/span/button/div/span'
# 点击资源
resource = 'nav[data-test-id="global_nav_headerNav"] > a:nth-child(3)'
# 点击主机（主机管理）
host_management = "//div[1]/div[2]/div/div[1]/div[2]/div[1]/div[1]/div/div"
# 点击全部
all = "//div[1]/div[2]/div/div[1]/div[1]/div[1]/div[2]/ul/li[3]/div"
# 高级筛选（全部）
advanced_filter = "//div[1]/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/button[1]"
# '//*[@id="app"]/div[1]/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/button[1]/i'(未分配)
# 筛选框输入主机
filtrate = '[placeholder="请输入IP或云区域ID:IP，多个IP可使用换行分隔"]'
# 查询
query = "/html/body/article/section/div[2]/div/div[2]/div/button[1]/div/span"
# 全部主机
all_host = "//div[4]/div[1]/table/thead/tr/th[1]/div/div/label/span"
all_host_undistributed = "//div[1]/table/thead/tr/th[1]/div/div/label/span"
# 转移到
transfer = "//div[2]/div/div[1]/div[1]/div[1]/div/div[1]/div/span"
# 主机池
host_assembler = "//div/div[1]/div[1]/div[1]/div/div[2]/ul/li[3]/a"
# 归还至目录
catalog = "/html/body/div[5]/div/div[1]/div[2]/div/div[1]/div/div/div/div"
# 空闲机
Idle_machine = "//div/div[2]/div/div/div[2]/ul/li[1]/div/span"
# 确定转移
sure_transfer = "/html/body/div[5]/div/div[1]/div[2]/div/div[2]/button[1]/div/span"

# 更多
more = '//div[3]/div/div[1]/button[@type="button"]/div/span'
# 删除
delete = '//div[3]/div/div[3]/ul/li[1]/button/div/span'
# 确认删除
sure_delete = '//div[4]/div/button[@name="confirm"]/div/span'
# 搜索框搜索
search = '//*[@id="app"]/div[1]/div[2]/div/div[1]/div[1]/div/div[1]/input'
# 搜索的模型名
model_name = '测试模型_demo'
# 点击模型
click_model = '//*[@id="app"]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div/div/div/span'
# 新建实例
creat_inst = '//div[1]/div[1]/span[1]/button/div/span'
# 删除实例
delete_inst = '/html/body/div[1]/div[1]/div[2]/div/div[1]/div[2]/div[5]/div[2]/table/tbody/tr/td[8]/div/span/button/div/span'
# 输入实例名
inst_name = '//div[1]/div/div/div[2]/ul/li/div[2]/div/div[1]/input'
# 输入的实例名
inst_name_text = '测试实例'
# 提交实例
commit_inst = '/html/body/article/section/div[2]/div/div[2]/div/span/button/div/span'
# 确定删除实例
sure_delete_inst = '//div[@class="v-transfer-dom"]/div/div/div/div[4]/div/button[1]/div/span'
# 搜索'主机'
search_host = '//div[@class="bk-input-text"]/input[@type="text"]'
# 点击主机
click_host = '//div[@class="models-layout"]/div[@title="主机"]'
# 快速搜索主机
fast_search = '//input[@type="text"][@placeholder="请输入IP或固资编号"]'
# 高级筛选中搜索主机
high_search = '//div[1]/div[2]/button[@class="bk-button bk-default icon-button option-filter ml10"]'
# 勾选蓝鲸业务下的主机
checkbox_blue_whale_host = '//th[1]/div/div/label/span[@class="bk-checkbox"]'
# 高级筛选中输入主机
input_host = '//div/textarea[@placeholder="请输入IP或云区域ID:IP，多个IP可使用换行分隔"]'
# 查询
click_search = "/html/body/article/section/div[2]/div/div[2]/div/button[1]"
# 搜索业务蓝鲸，断言页面是否存在"业务名"
assert_business = 'li[id="property-item-1"] > span:nth-child(1)'

### 业务集下
# 点击业务集
click_business_set = '//div[@title="业务集"]'
# 新建
creat_business_set = '//span/button[@class="fl bk-primary bk-button-normal bk-button"]'
# 业务集名
business_set_name = '//div[2]/ul/li[1]/div[2]/div/div[1]/input'
businessset_name = '测试业务集'
# 提交
commit_businessset_name = '//span/button[@class="button-save bk-primary bk-button-normal bk-button"]'
# 预览
preview = '//div[2]/table/tbody/tr[1]/td/div/span[1]/button'
# preview ='//button[class="bk-primary bk-button-normal bk-button-text"][1]/div/span'
# 搜索业务
# search_business = '/html/body/div[6]/div/div/div/div[3]/div/div[1]/div/div[1]/input'
search_business ='//div[@class="v-transfer-dom"][3]/div/div/div/div[3]/div/div[1]/div/div[1]/input'

# 搜索到元素（配置平台自动化测试）
business_searchname = '//div[2]/ul/li/a[@title="配置平台自动化测试"]'
# 编辑
edit_business_set = '//div[2]/table/tbody/tr[1]/td/div/span[2]/button'
# 业务集描述
# business_set_describe = '//div[2]/ul/li[2]/div[2]/div/div[1]/input'
business_set_describe ='//div[@data-vv-name="bk_biz_set_desc"]/div/input'
# 删除
delete_business_set = '//div[2]/table/tbody/tr[1]/td/div/span[3]/button'
# 确定删除
# sure_delete_business_set = '//div[7]/div/div/div/div[4]/div/button[1]'
sure_delete_business_set = '//div[@class="bk-dialog-footer"]/div/button[1]/div/span'
# 关闭窗口
# close_windows = '/html/body/div[6]/div/div/div/i'
close_windows ='//div[@class="v-transfer-dom"][3]/div/div/div/i'
### 业务下
click_test_business = '//div[3]/table/tbody/tr/td[2]/div/span'
# 生命周期
# lifecycle = '//li[2]/span[3]/button/div/span/i'
lifecycle ='//*[@id="property-item-2"]/span/button/div/span/i'
# 选择生命周期
select_lifecycle = '//div[@title="测试中"]'
# 勾选生命周期
check_lifecycle = '//i[@class="form-confirm bk-icon icon-check-1"]'
# 搜索业务名
search_business_name = '//div[1]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/input'
# 归档
pigeonhole = "//div/div[1]/div[2]/div[4]/div[2]/table/tbody/tr//td/div/span/button/div/span"
# #根据业务名选择业务
# OPTION_NAME = '//div/div/span[contains(text(),"{}")]'.format(settings.BUSINESS_NAME_CMDB)
# 确定归档
sure_pigeonhole ='//div[@class="v-transfer-dom"]/div/div/div/div[4]/div/button[1]/div/span'
# 已归档
filed = '//*[@id="app"]/div[1]/div[2]/div/div[1]/div[1]/div[1]/span/button/i'
# 输入业务
inpu_business_name = '[placeholder="请输入业务"]'
# 彻底删除
completely_cancel = '//div[2]/table/tbody/tr//td/div/span/div/div/button/div/span'

# 恢复业务
#恢复业务正确路径
recover_business ='//div[2]/table/tbody/tr/td/div/span/button/div/span'
# #彻底删除
# completely_cancel = '//div/span/div/div/button/div/span[contains(text(),"{}")]'.format(settings.COMPLETELY_CANCEL)
# 确定删除
sure_delete_business = '//div/div[2]/div/div/div[2]/button[1]'
# 确定恢复
sure_recover_business ='//div[@class="recovery-dialog v-transfer-dom"]/div/div/div/div[4]/div/button[1]/div/span'
# 恢复的业务名
recover_business_name = '//input[@placeholder="请输入业务名"]'
# 返回业务
return_business = '//*[@id="app"]/div[1]/div[1]/i'



### 断言
# 归档断言
assert_pigeonhole = "归档成功"
# 断言是否创建成功
asserttext_creat = "创建成功"
# 断言是否删除成功
asserttext_delete = "删除成功"

# 断言模型是否删除成功
asserttext_delete_mod ="删除成功"
# 断言删除成功
assert_delete_business = " 已彻底删除"
# 断言转移成功
asssert_transfer = "转移成功"
# 删除断言
assert_delete = "成功删除选中的主机"
# 断言
asserttext = '创建成功'
# 断言修改成功
assert_update = '修改成功'
# 恢复业务成功
assert_recover_business_success = '恢复业务成功'
# 编辑成功
assert_edit_success = '编辑成功'
