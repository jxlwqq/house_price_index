#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import traceback

import xlwt

from browser import BaiduBrowser
from utils.log import logger
import config
import model


def main(area_name, month):
    sql = "select a.id, c.area_code from house.area as a left JOIN house.area_code as c on (a.id = c.area_id) WHERE a.area_name = '%s' and c.code_type = 'baidu'" % area_name
    data = model.query(sql)
    area_id = data[0][0]
    area_code = data[0][1]
    logger.info(u'请确保你填写的账号密码能够成功登陆百度')

    s = BaiduBrowser()

    fp = open(config.keywords_task_file_path, 'rb')
    task_list = fp.readlines()
    fp.close()

    root = os.path.dirname(os.path.realpath(__file__))
    result_folder = os.path.join(root, config.out_file_path)
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)

    type_list = config.index_type_list
    for keyword in task_list:
        try:
            keyword = keyword.strip()
            if not keyword:
                continue
            keyword_unicode = keyword.decode('utf-8')
            for type_name in type_list:
                baidu_index_dict = s.get_baidu_index(
                    keyword_unicode, area_code, month, type_name
                )
                date_list = sorted(baidu_index_dict.keys())

                file_name = '%s_%s.xls' % (keyword, type_name)
                file_path = os.path.join(result_folder, file_name)

                data_list = []
                for date in date_list:
                    value = baidu_index_dict[date]
                    data_list.append((keyword, date, type_name, value))
                #write_excel(file_path, data_list)
                insert_data(area_id, data_list)
        except:
            print traceback.format_exc()

def insert_data(area_id, data_list):
    values = ''
    for item in data_list:
        time_type = 'day'
        time_index = str(item[1]).replace('-', '')
        data_key = '百度指数-%s' % item[0]
        data_value = item[3]
        values += "('%s', %s, %s, '%s', %s, now())," % (time_type, time_index, area_id, data_key, data_value)
    if values:
        sql = "insert into house.house_index(time_type, time_index, area_id, data_key, data_value, create_time) VALUES " + values.rstrip(',') + ' on duplicate key update data_value = values(data_value)'
        model.execute(sql)




def write_excel(excel_file, data_list):
    wb = xlwt.Workbook()
    ws = wb.add_sheet(u'工作表1')
    row = 0
    ws.write(row, 0, u'关键词')
    ws.write(row, 1, u'日期')
    ws.write(row, 2, u'类型')
    ws.write(row, 3, u'指数')
    row = 1
    for result in data_list:
        col = 0
        for item in result:
            ws.write(row, col, item)
            col += 1
        row += 1

    wb.save(excel_file)

if __name__ == '__main__':
    main()