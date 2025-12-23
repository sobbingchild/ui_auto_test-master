# 搜索云区域
searchcloud = '[data-test-id="cloudManager_input_searchCloud"] > div >input'
# 搜索框输入"2"
input_text = "div:nth-child(1).bk-input-text > .bk-form-input"
# 输入的数字
text = "2"
# 点击云区域
cloud_area = "//section[2]/div[2]/div[1]/div[3]/table/tbody/tr/td[1]/div/span"
# 点击Agent数量
number_of_nodes = '[data-test-id="cloudManager_btn_filterAgent"]'
# 点击云区域
cloud_area_name = '[data-test-id="cloudManager_btn_viewDetail"]'
# 点击安装，进行安装proxy
install = "article > div:nth-child(1) > section:nth-child(2) > button:nth-child(1) > div > span"
# 点击proxy旁边的更多
more = "//div[2]/table/tbody/tr[1]/td[8]/div/div/div/span/div[2]/div/button/div/span"
more_2 = "//div[2]/table/tbody/tr/td[8]/div/div/div/span/div[2]/div/button/div/span"
# 移除proxy
remove_proxy = "div > div:nth-child(2) > div > ul > li:nth-child(2)"
# 重启proxy
reboot_proxy = "div > div:nth-child(2) > div > ul > li:nth-child(3)"
# 重载proxy
reload_proxy = "div > div:nth-child(2) > div > ul > li:nth-child(4)"
# 升级proxy
upgrade_proxy = "div > div:nth-child(2) > div > ul > li:nth-child(5)"
# 卸载proxy
uninstall_proxy = "div > div:nth-child(2) > div > ul > li:nth-child(1)"
# 点击重装
reinstall_proxy = "//div[2]/table/tbody/tr[1]/td[8]/div/div/div/span/div[1]/div/button/div/span"
# 确定移除proxy
sure_remove = ".bk-dialog-footer > div > button > div > span"
# 确定重启/卸载
sure_reboot = "div:nth-child(4) > div > button:nth-child(1) > div"
# 确定重载/升级/重装
sure = "div:nth-child(4) > div > button:nth-child(1) > div > span"
# 断言
asserttext = "暂无数据"
# 输入第一台proxy的主机信息
input_proxy_inter_ip_first = "tr:nth-child(1) > td:nth-child(1) > div > div > div > div:nth-child(1) > input"
input_proxy_internet_first = "tr:nth-child(1) > td:nth-child(2) > div > div > div > div:nth-child(1) > input"
input_proxy_internet_login_first = "tr:nth-child(1) > td:nth-child(3) > div > div > div > div:nth-child(1) > input"
proxy_password_first = "tr:nth-child(1) > td:nth-child(5) > div > div > div > div:nth-child(1) > input"
# 输入第二台proxy的主机信息
input_proxy_inter_ip_second = "tr:nth-child(2) > td:nth-child(1) > div > div > div > div:nth-child(1) > input"
input_proxy_internet_second = "tr:nth-child(2) > td:nth-child(2) > div > div > div > div:nth-child(1) > input"
input_proxy_internet_login_second = "tr:nth-child(2) > td:nth-child(3) > div > div > div > div:nth-child(1) > input"
proxy_password_second = "tr:nth-child(2) > td:nth-child(5) > div > div > div > div:nth-child(1) > input"
# 点击归属业务
business = "section:nth-child(1) > form > div:nth-child(7) > div > div > div > div > div"
# 输入业务id
input_business_id = ".bk-select-search-input"
# 确定归属业务
sure_business = "div.select-item > span.select-item-name"
# 点击安装
install_proxy = '//button[@data-test-id="cloudManager_btn_instalProxy"]'
# 点击云服务商
select_cloud = "[data-test-id='cloudInfo_select_cloudIsp'] > div > div"
# 选择云服务商腾讯云
tencent_cloud = "//div[2]/div/div/div/ul/li[9]/div"
# 提交云区域信息
commit_cloud = "section.add-cloud-footer > button[type='button'] > div >span"
asserttext_creation_cloud = "云区域创建成功"
asserttext_edit_cloud = "编辑成功"
asserttext_delete_cloud = "删除成功"
# 点击稍后安装
click_install = "div.footer-wrapper > button[type='button'] > div > span"
# 点击新建云区域
addcloud = "[data-test-id='cloudManager_btn_addCloud']"
# 编辑云区域
editcloud = "[data-test-id='cloudManager_btn_editCloud']"
# 删除云区域
deletecloud = "[data-test-id='cloudManager_btn_deleteCloud']"
# 确定删除云区域
sure_delete_cloud = "div.footer-wrapper > button:nth-child(1)[type='button'] > div > span"
# 云区域名称
cloudname = "[data-test-id='cloudInfo_input_cloudName'] > div > input"
# 保存云区域信息
savecloud = "section:nth-child(3) > button:nth-child(1) > div > span"
