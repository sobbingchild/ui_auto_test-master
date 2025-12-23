
#新建按钮
create_plugin = '//button[@class="left-button mc-btn-add bk-primary bk-button-normal bk-button"]'

#插件ID
plugin_id = '//div[@class="step-plugin"]/div[2]/div[2]/div/div/div[1]/input'
#插件别名
plugin_item = '//div[@class="step-plugin"]/div[3]/div[2]/div/div[1]/input'

#选择业务
select_target = '//*[@class="biz-select-target-main"]'



#侧边栏展开
footer_expand = '//span[@class="footer-icon-svg"]'

#插件配置
plugin_config = '//div[@style="top: 242px; height: 22px;"]/span/span'
plugin_config_2 = '//div[@style="top:242px;height:22px;"]/span/span'
# plugin_config = '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/div[6]/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/div[1]/div[4]/div[3]'
plugin_config_area= '//div[@class="view-lines monaco-mouse-cursor-text"]'
# plugin_config_input = "awk '(f==0) { i=1; while ( i<=NF) {n[i] = $i; i++ }; f=1; next} (f==1){ i=2; while ( i<=NF){ "+'printf "TcpExt_%s  %d\n",'+"n[i], $i; i++}; f=0}'  /proc/net/netstat"
plugin_config_input = 'aaaa'

#插件配置下一步
step_plugin_next = '//div[@class="step-plugin-item next-step"]/div[2]/button'

#调试机器选择
host_container = '//div[@class="host-container"]/div'
host_select = '//div[@class="bk-virtual-content"]/table/tbody/tr[1]'
debug_button = '//div[@class="opeartor-container"]/button[2]'



#debuging
debug_status = '//div[@class="opeartor-container"]/button[3]/div/span'

debug_save = '//div[@class="opeartor-container"]/button[4]'

#保存维度和指标
monitor_metric_save = '//div[@class="footer-btn mb10"]/button[1]'
set_metric_button = '//*[contains(text(),"设置指标&维度")]'
auto_metric = '//span[@class="auto-collect"]/div/input'
confirm_auto_metric = '//*[@class="header"][contains(text(),"此操作存在危险")]/../../div[5]/div/button[1]'
save_auto_metric = '//*[contains(text(),"返回插件定义")]/../../../button[1]/div/span'

finish_save_plugin = '//*[contains(text(),"重新调试")]/../../../button[4]/div'
#新建插件消息
message_title = '//h4[@class="message-title"]'

#数据采集切换
data_collect_tab = '//span[@class="nav-menu-item"][contains(text(),"数据采集")]'
#新增数据采集
new_data_collect = '//button[@class="mc-btn-add bk-primary bk-button-normal bk-button"]'
collection_name = '//div[@class="set-edit"]/div[2]/div[2]/div/div/div/input'
# collection_plugin = ''
collection_name_input = '进程采集测试1'
# collection_name_input = '进程采集插件'
# //*[@class="name"][contains(text(),"进程采集插件")]
#选择插件
collection_plugin_select = '//div[@class="set-edit"]/div[3]/div[2]/div/div'
#选择搜索出来的第一个插件
# collection_plugin_confirm = '//ul[@class="bk-options bk-options-single"]/li[1]/div/span'
collection_plugin_confirm = '//*[@class="name"][contains(text(),"进程采集插件1")]'
# collection_plugin_confirm = '//*[@class="name"][contains(text(),"testplugin1")]'
collection_plugin_search = '//input[@class="bk-select-search-input"]'
# collection_plugin_search_input = 'testplugin'
collection_plugin_search_input = '进程采集插件1'
# collection_plugin_search_input = 'testplugin1'


collect_next_step = '//*[contains(text(),"下一步")]'
#命令行匹配
common_match = '//*[@class="bk-radio-text"][contains(text(),"命令行匹配")]'
common_contain = '//*[@placeholder="进程关键字"][contains(text(),"")]/../../DIV[2]/input'
common_contain_input = 'agent'
#静态拓扑
static_topo = '//li[@data-name="static-topo"]'
top_label = '//span[@class="label"][contains(text(),"根节点")]'
all_ip = '//thead[@id="bkIPSelectorHostTableHead"]/tr/th/div[1]/label/span'

install_collections = '//div[@class="btn-container"]/button[2]'
install_force = '//*[@class="header"][contains(text(),"版本校验不通过")]/../../div[5]/div/button[1]'
install_finish = '//div[@class="footer"]/button'

install_message = '//div[@class="message-title"]'



#删除插件/删除数据采集
del_data_collect = '//span[@class="col-name-desc"][contains(text(),"进程采集测试1")]/../../../../td[8]/div/div/span[4]'
"""需要更改数据采集项的名字"""
del_data_button = '//span[@class="operator-group-btn"][contains(text(),"删除")]'
del_confirm = '//button[@class="del-btn bk-primary bk-button-normal bk-button"]/div'
del_finish = '//*[@class="del-btn bk-primary bk-button-normal bk-button"]/div'

del_plugin_option = '//*[@class="desc-category"][contains(text(),"testplugin1")]/../../../../../td[8]/div/div/span/i'
del_plugin_button = '//*[@class="operator-group-btn"][contains(text(),"删除")]'
del_plugin_confirm = '//*[@class="header"][contains(text(),"确认要删除？")]/../../div[5]/div/button[1]'

make_plugin_tab = '//*[@class="nav-menu-item"][contains(text(),"指标插件")]'


