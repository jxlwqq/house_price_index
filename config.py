#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

# 要启用的浏览器driver, 因为有些人PhantomJS配置可能有问题，默认使用Firefox(容易配置).
# 具体参考selenium的浏览器环境配置
browser_driver = 'Firefox'  # 可以替换为PhantomJS
# 百度用户名
user_name = '你的账号'
# 百度密码
password = '账号密码'
# 百度登陆链接
login_url = ('https://passport.baidu.com/v2/?login&tpl=mn&u='
             'http%3A%2F%2Fwww.baidu.com%2F')
# 一周
one_week_trend_url = ('http://index.baidu.com/?tpl=trend&type=0'
                      '&area={area_id}&time=12&word={word}')
# 区间
time_range_trend_url = ('http://index.baidu.com/?tpl=trend&type=0'
                        '&area={area_id}&time={start_date}|{end_date}&word={word}')
# api
all_index_url = ('http://index.baidu.com/Interface/Search/getAllIndex/'
                 '?res={res}&res2={res2}&startdate={start_date}'
                 '&enddate={end_date}')
# 图片信息的api
index_show_url = ('http://index.baidu.com/Interface/IndexShow/show/?res='
                  '{res}&res2={res2}&classType=1&res3[]={enc_index}'
                  '&className=view-value&{t}'
                  )
# 判断登陆状态的地址
user_center_url = 'http://i.baidu.com/'
# 判断登陆的标记
login_sign = 'http://passport.baidu.com/?logout'
# 线程数
num_of_threads = 40

# 输出的格式，暂时只支持excel
# extension = 'excel'
# 输出的文件夹路径，可以自定义
out_file_path = sys.path[0] + '/baidu_index/data/out'
# 关键词任务的文件路径，可以自定义
keywords_task_file_path = sys.path[0] + '/baidu_index/task.txt'

# 要获取趋势的类别，默认是三种趋势都获取。all代表整体趋势，pc代表PC趋势, wise代表移动趋势
# index_type_list = ['all', 'pc', 'wise']
index_type_list = ['all']

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
