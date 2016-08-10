# -*- coding: utf-8 -*-

# mysql

mysql = {'host': 'localhost', 'user': 'root', 'password': '123456', 'database': 'house'}

# headers
headers = {'Referer': 'http://www.baidu.com',
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',}
# sina
sina = {
    # 新浪宏观数据首页
    'mac_data_url': 'http://finance.sina.com.cn/mac/',
    # 大中城市房屋价格指数
    '70_cities_house_price_index': {
        'url': 'http://money.finance.sina.com.cn/mac/api/jsonp.php/SINAREMOTECALLCALLBACK%s/MacPage_Service.get_pagedata?cate=industry&event=3&from=0&num=31&condition={"date":%s,"query":["%s"]}&_=%s',
        'response_pattern': 'SINAREMOTECALLCALLBACK\d+\(\(\{config:\{all:(.*?),index:\d+,defaultItems:\[.*?\]\},count:"\d+",data:(.*?)}\)\)'
    }
}


