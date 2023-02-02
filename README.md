# 框架介绍：

本框架使用了Requests+Pytest+Allure+Logging+Yagmail+PyYAML编写的接口自动化框架

主要优点是：测试人员将测试用例编写为YAML文件然后进行运行即可，框架会自动进行输出报告。

缺点：未集成Excel来进行读取用例，YAML文件格式必须准确不然会报错。

# 目录介绍：

下面是大致介绍：

![image-20230202140231457](https://raw.githubusercontent.com/1090146450/DepositImg/master/One_Pytest_Img/1.png)

# 流程介绍：

## 测试流程：

1、修改域名为测试环境还是正式环境（在Common中的Consts中修改即可）

2、根据测试用例，编写成yaml格式

3、运行run.py

可以在pytest.ini中修改是否使用多进程运行，本框架默认多进程运行（2个进程），默认测试文件在testCase模块中，默认失败重跑一次（注意：如果您使用的断言为pytest.assume则不会重跑而使用assert会）





