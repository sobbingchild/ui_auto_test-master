# 点击搜索框
search_input = "div.search-input-input > div.div-input"
# 点击搜索框
data_placeholder = "[data-placeholder='搜索IP，云区域']"
# 勾选主机
linux_host = "[data-test-id='common_checkbox_tableCheckAll']"
linux_host_2 = "section:nth-child(2) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > table > tbody > tr > td:nth-child(1) > div > div > label > span"
# 勾选全部linux主机
check_linux_host = "//div[1]/table/thead/tr[1]/th[1]/div/div/div/div[1]/label/span"
# 勾选windows主机
windows_host = "[data-test-id='common_checkbox_tableCheckAll']"
windows_host_2 = "div:nth-child(2) > table > tbody > tr > td:nth-child(1) > div > div > label > span"
# 点击批量
batch = '[data-test-id="agentStatus_btn_operate"]'
# 点击批量
batch_2 = "div.bk-tooltip-ref > span.icon-down-wrapper > span"
# 点击移除
remove_linux = "//section[1]/div[1]/div[3]/div[2]/ul/li[4]/a"
remove_windows = "section:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > ul > li:nth-child(4) > a"
# 点击移除（选择操作系统为linux/windows后）
remove_host = "div:nth-child(2) > ul > li:nth-child(4) > a"
# 点击安装Agent
install_agent = '[data-test-id="agentStatus_btn_install"]'
# 点击重启
reboot_linux = "//section[1]/div[1]/div[3]/div[2]/ul/li[6]/a"
reboot_windows = "ul > li:nth-child(6) > a"
reboot_pagent = "div:nth-child(2) > ul > li:nth-child(6) > a"
# 点击重载配置
reload_linux = "//section[1]/div[1]/div[3]/div[2]/ul/li[5]/a"
reload_windows = "ul > li:nth-child(5) > a"
reload_pagent = "div:nth-child(2) > ul > li:nth-child(5) > a"
# 点击升级
upgrade_linux = "section:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > ul > li:nth-child(2) > a"
upgrade_windows = "div:nth-child(3) > div:nth-child(2) > ul > li:nth-child(2) > a"
# 点击卸载
uninstall_linux = '//li/a[@data-test-key="uninstall"]'
uninstall_linux_pagent = "div:nth-child(3) > div:nth-child(2) > ul > li:nth-child(3) > a"
# 点击安装/重装
install_linux = "section:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > ul > li:nth-child(1) > a"
# 确定移除/重启/重载等操作
confirm = "[name='confirm'] > div > span"
confirm_remove = "button[type='button'][name='confirm'] > div > span"
# 确定移除/重启（选择操作系统后）
sure_remove = "button[type='button'][name='confirm'] > div > span"
# 再次点击重载配置
reload = ".install > span"
# 确定升级
sure_upgrade = ".footer-wrapper > button > div > span"
# 确定重装或者确定卸载
confirm_reinstall = "div.install > span"
# 确定重载配置pagent(linux)
confirm_3 = "div.install > span:nth-child(1)"
# 点击普通安装
general_installation = '[data-test-id="common_btn_moreItem"]'
# 点击安装到业务
install_business = '//article/section[1]/div/form/div[2]/div/div/div/div/div'
# 输入业务id
input_business_id = ".bk-select-search-input"
# 业务ID
business_id = "2"
# 点击业务节点管理测试用
business = "span.select-item-name"
business_click = '//div/div[2]/div/div/div[2]/ul/li/div/div/span'
# 点击云区域(Agent管理)
click_cloud_area = "//div/div[2]/div[2]/div/div[3]/div/article/section[1]/div/form/div[3]/div/div/div/div/div"
click_cloud_area_2 = "section:nth-child(1) > div > form > div:nth-child(3) > div > div > div > div > div"
# 选择为直连区域
directly_connected_area = "[title='直连区域']"
# 选择云区域节点管理测试用
cloud_area = "[title='节点管理UI自动化']"
# 点击操作系统
operating_system = "td:nth-child(2) > div > div > div > div > div > div"
# 选择操作系统
operating_system_select = "li:nth-child(1).bk-search-list-menu-item > div.item-name"
# 选择系统为linux
linux_system = "li:nth-child(1).bk-search-list-menu-item > div.item-name"
# 选择系统为windows
windows_system = "li:nth-child(2).bk-search-list-menu-item > div.item-name"
# 确认系统为linux
sure_system = "div:nth-child(3).bk-search-list-footer > span:nth-child(1).footer-btn"
# 选择操作系统为windows
system = '//div[@title="Windows"]'
# 输入IP及密码
input_ip = "[type='textarea']"
input_password = '//div[@class="input-type input-password"]/div/div/input'
# 在卸载重装界面输入密码
input_password_reinstall = "td:nth-child(10) > div > div > div > div:nth-child(1) > input"
# 点击安装
install = "//section[1]/div/div/button[1]/div/span/div/span[1]"
install_2 = "span > div.form-btn-install > span:nth-child(1)"
# 点击全部业务
click_business = '[data-test-id="common_select_biz"]'
# 搜索框搜索业务
search_business = '.bk-select-search-input'
#判断执行成功的元素是否在界面上
execute_successfully_install = '//div[3]/table/tbody//tr/td[8]/div/div/span[2]'


