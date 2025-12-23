

Executive_History = '//div[@data-test-id="navigation_executiveHistory"]'

Search_area = '//textarea[@placeholder="搜索任务ID，任务名称，执行方式，任务类型，任务状态，执行人..."]'

#任务名称
Task_name = '//tr[@class="search-suggest-menu-item active"]'
#第一条任务的ID
Task_Name_first = '//table[@class="bk-table-body"]/tbody/tr[1]/td[2]/div'

#搜索结果-操作第一个结果
Search_result_TaskName = '//table[@class="bk-table-body"]/tbody/tr[1]/td[2]/div'
# Search_result_Restart = '//td[@class="bk-table-2-column-14 is-left "]/div/button[2]'
# Search_result_Restart = '//div[@class="bk-table-body-wrapper is-scrolling-right"]/table/tbody/tr[1]/td[9]/div/button[2]/div'
Search_result_Restart = '//div[@class="bk-table-fixed-body-wrapper"]/table/tbody/tr[1]/td[9]/div/button[2]'
# Search_result_Details = '//td[@class="bk-table-2-column-14 is-left "]/div/button[1]'
Search_result_Details = '//div[@class="bk-table-fixed-body-wrapper"]/table/tbody/tr[1]/td[9]/div/button[1]'
# //div[@class="bk-table-body-wrapper is-scrolling-right"]/table/tbody/tr[1]/td[9]/div/button[1]/div'
#关闭搜索框
Search_ID = '//ul[@class="jb-bk-search-list-menu"]/li[1]'

#重做界面的按钮
Restart_page_button = '//button[@data-test-id="button_fastExecuteScriptSubmit"]'
Restart_status = '//div[@class="status"]/span[2]'

#详情界面
Detail_Step_Name = '//div[@class="step-name-text"]'
Detail_Title = '//div[@class="title-text"]'