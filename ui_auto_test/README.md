# 蓝鲸UI自动化测试


## UI自动化测试框架选用--seldom
基于 selenium 和 unittest 的 Web UI自动化测试框架。
    GitHub地址：https://github.com/SeldomQA/seldom

- python version: 3.10.11
- seldom version:3.11.0

  - 提供更加简单API编写自动化测试。
    - 提供脚手架，快速生成自动化测试项目。
    - 全局启动和关闭浏览器，减少浏览器的启动次数。
    - 支持用例参数化。
    - 支持用例失败/错误重跑。
    - 定制化HTML测试报告，用例失败/错误自动截图。
    - 支持XML测试报告
### 安装

``` 
> pip install seldom
```
### Quick Start
```
>seldom --project mypro
```
目录结构如下：

```
mypro/
├── test_dir/
│   ├── data.json
│   ├── test_sample.py
├── reports/
└── run.py
```
-  `test_dir/`  目录实现用例编写。
-  `reports/`  目录存放生成的测试报告。
-  `run.py`  文件运行测试用例。

**说明：** 
- 创建测试类必须继承  `seldom.TestCase` 。
- 测试用例文件命名必须以  `test`  开头。
- seldom的封装了 `assertTitle` 、 `assertUrl`  和  `assertText` 等断言方法。
### Run the test
```python
import seldom

seldom.main()  # 默认运行当前测试文件
seldom.main(path="./")  # 当前目录下的所有测试文件
seldom.main(path="./test_dir/")  # 指定目录下的所有测试文件
seldom.main(path="./test_dir/test_sample.py")  # 指定目录下的测试文件
```

##安装浏览器驱动
详细信息：https://github.com/SeldomQA/seldom/blob/master/docs/driver.md
###seldom框架附带下载浏览器驱动命令
```
>seldom -install chrome
```
seldom -install chrome之后会把`chromedriver`默认下载到当前的 `lib/`  目录下面。此时case仍无法正常运行。
解决办法1：手动将 `lib`  目录下的chromedriver(chrome浏览器驱动)移动到对应python解释器文件夹下。
注：windows 是把chromedriver移动到python安装的Script目录，linux 是把chromedriver移动到python安装路径的bin目录
解决办法2：在seldom中指定浏览器驱动文件目录的绝对路径。(不建议hardcode)
```python
import seldom
from seldom.driver import ChromeConfig

# ……
if __name__ == '__main__':
    ChromeConfig.executable_path = "D:\git\seldom\lib\chromedriver.exe"
    seldom.main(browser="chrome")
```
###手动下载驱动地址
geckodriver(Firefox):https://github.com/mozilla/geckodriver/releases 
Chromedriver(Chrome):https://sites.google.com/a/chromium.org/chromedriver/home 
IEDriverServer(IE):http://selenium-release.storage.googleapis.com/index.html 
operadriver(Opera):https://github.com/operasoftware/operachromiumdriver/releases 
MicrosoftWebDriver(Edge):https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver

## seldom 运行

seldom的给运行新手造成了困扰，强烈不建议你在 `pycharm` 里面运行。

>Window建议使用cmder, mac/linux使用自带终端。

### 运行说明

参考目录结构如下：

```shell
mypro/
├── test_dir/
│   ├── test_sample.py
├── reports/
└── run.py
```
seldom要运行的测试是由 `main()` 方法决定的，创建  `run.py`  文件

```python
import seldom

seldom.main(path="./")
```
在cmder/终端下面运行  `run.py`  文件
```
> python run.py
```
或者：
```
> seldom -r run.py
```
**要运行的用例由  `path`  参数控制** 

-  `"./"`  : 表示 `run.py` 文件所在目录下的所有以 `test` 开头的测试文件。
-  `"./test_dir/"`  : 指定 `test_dir/` 目录下所有以 `test` 开头的测试文件。
-  `"./test_dir/test_sample.py"`  : 指定 `test_dir/` 目录下的 `test_samplepy` 测试文件.
-  `"test_sample.py"`  : 指定当前目录下的 `test_sample.py` 测试文件。