#主机搜索中输入内容
# index_host_search = '[placeholder="请输入IP或固资编号，多条数据请用逗号、分号或换行分隔"]'
# index_host_search = '//div[@data-test-id="index_comp_bkInput"]/div/textarea'
index_host_search = "[placeholder='请输入IP、管控区域和IP、固资编号进行搜索，使用 Shift + Enter 换行。']"
#在全文检索中输入内容
index_text_search = '[placeholder="请输入关键字，点击或回车搜索"]'
#点击全文检索
textsearch="div:nth-child(1).search-tab > span:nth-child(2).tab-item"
#搜索
index_button_search = '[data-test-id="index_button_search"]'
#点击蓝鲸业务进行跳转
click_business = '//div/ul/li[@title="蓝鲸"]'
#点击主机模型进行跳转
click_host_model = '//div/ul/li[@title="主机"]'
#点击蓝鲸业务下的主机
click_host = '//div/div[3]/ul/li'








