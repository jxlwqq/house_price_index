#! usr/bin/env python
# -*- coding: utf-8 -*-
import model

sql = '''
INSERT INTO house_index (time_type, area_id, time_index, data_key, data_value)
  SELECT
    'month',
    area_id,
    date_format(time_index, '%Y%m') AS time_index,
    data_key,
    sum(data_value)                 AS data_value
  FROM house_index
  WHERE time_type = 'day'
  GROUP BY area_id, data_key, date_format(time_index, '%Y%m')
ON DUPLICATE KEY UPDATE data_value = values(data_value)
'''
model.execute(sql)
