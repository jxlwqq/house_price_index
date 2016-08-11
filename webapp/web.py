#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
import model

app = Flask(__name__)

@app.route('/')
def index():
    sql = "select time_index, data_value from house.house_index where data_key = '百度指数-二手房' and area_id = 18 order by time_index asc"
    res = model.query(sql)
    date = []
    data = []
    for val in res:
        date.append(int(val[0]))
        data.append(int(val[1]))

    return render_template('index.html', date=date, data=data, title=u'百度指数-二手房')


if __name__ == '__main__':
    app.run(debug=True)