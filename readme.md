# 数据来源:
* [tradingeconomics](http://www.tradingeconomics.com/)
* [百度指数](https://index.baidu.com/)
* [Google Trends](https://www.google.com/trends/)
* [中华人民共和国国家统计局](http://www.stats.gov.cn/)
* [中国宏观经济数据_新浪财经](http://finance.sina.com.cn/mac/)
* [房天下](http://fangjia.fang.com/)

# 相关库
* scikit-learn 机器学习,用于建立预测模型
* scrapy 爬取相关数据
* selenium 某些网站的数据以图片形式,需浏览器打开,并识别图片
* flask web框架

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


# 运行步骤:
0. 安装 selenium的最新版本 ``` pip install -U selenium```，目前(20160809)为2.53.6。安装 [firefox 45](https://ftp.mozilla.org/pub/firefox/releases/45.0/) 版本，并禁止浏览器自动升级。
 
1. 修改config.py要启用的浏览器driver, 因为有些人PhantomJS配置可能有问题，默认使用Firefox(容易配置).
  具体参考selenium的浏览器环境配置

2. 修改config.py里面的百度账号跟密码

4. 修改task.txt，这是关键词的任务列表，一行一个。注意这里面的编码是utf-8的，最好也别带bom头，免得出问题

5. 执行 python run.py 开始爬取数据

6. 执行 webapp/web.py 可以运行一个web服务,显示一个基于 echarts 的图表



