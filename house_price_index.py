#! usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import time
import datetime
import demjson
import re
import config
import model

def get_last_month():
    today = datetime.date.today()
    month = (str)(datetime.date(day=1, month=today.month, year=today.year) - datetime.timedelta(days=1))
    arr = month.split('-')
    return arr[0] + '-' + arr[1]


def time_format(time, type):
    arr = time.split('-')
    if type == '':
        return arr[0] + arr[1]
    elif type == '.':
        if arr[1][0] == '0':
            return arr[0] + type + arr[1][1]
        else:
            return arr[0] + type + arr[1]


def main(area_name, month):

    time_index = time_format(month, '')
    date_list = [time_format(month, '.')]

    print time_index, date_list

    sql = "select a.id, c.area_code from house.area as a left JOIN house.area_code as c on (a.id = c.area_id) WHERE a.area_name = '%s' and c.code_type = 'sina'" % area_name
    data = model.query(sql)
    area_id = data[0][0]
    area_code = data[0][1]
    res = requests.get(config.sina['mac_data_url'], headers=config.headers)
    cookies = res.cookies
    milli_time_func = lambda: int(round(time.time() * 1000))
    milli_time = milli_time_func()
    date_list = demjson.encode(date_list)
    url = config.sina['70_cities_house_price_index']['url'] % (milli_time, date_list, area_code, milli_time)
    print url
    res = requests.get(url, headers=config.headers, cookies=cookies)
    print res.text
    pattern = re.compile(config.sina['70_cities_house_price_index']['response_pattern'], re.S)
    result = re.findall(pattern, res.text)
    print result
    key = demjson.decode(result[0][0])
    value = demjson.decode(result[0][1])
    sql = "insert into house.house_index(time_type, time_index, area_id, data_key, data_value, create_time) VALUES "
    values = ''
    for item in value:
        i = 0
        for val in item:
            if i > 1:
                print key[i][1]
                if val == None:
                    val = 0
                values += "('month', %s, %s, '%s', %s, now())," % (time_index, area_id, key[i][1], val)
            i = i + 1

    sql = sql + values.rstrip(',') + " on duplicate key update data_value = values(data_value)"
    model.execute(sql)


