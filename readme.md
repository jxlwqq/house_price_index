
# 房价走势相关指数
* 百度关键词指数 "地王" "二手房"
* 城市净流入人口
* 地铁里程数
* 高校毕业生人数
* 房天下价格指数
* 货币流通量
* 人均可支配收入
* CPI
* GDP
* 人民币汇率
* 相关垂直网站的流量 房天下 安居客 链家
* 沪深股指

基础项目地址: [longzhiwen888/fetch_baidu_index](https://github.com/longzhiwen888/fetch_baidu_index)

在上述项目上做了适当的调整,运行环境为 python2.7.*

# 运行步骤:
0. 安装 selenium的最新版本 ``` pip install -U selenium```，目前(20160809)为2.53.6。安装 [firefox 45](https://ftp.mozilla.org/pub/firefox/releases/45.0/) 版本，并禁止浏览器自动升级。
 
1. 修改config.py要启用的浏览器driver, 因为有些人PhantomJS配置可能有问题，默认使用Firefox(容易配置).
  具体参考selenium的浏览器环境配置

2. 修改config.py里面的百度账号跟密码

4. 修改task.txt，这是关键词的任务列表，一行一个。注意这里面的编码是utf-8的，最好也别带bom头，免得出问题

5. 执行 python run.py 开始爬取数据

6. 执行 webapp/web.py 可以运行一个web服务,显示一个基于 echarts 的图表



