#! usr/bin/env python
# -*- coding: utf-8 -*-


from baidu_index import main
import house_price_index

if __name__ == '__main__':
    # 百度指数
    main.main('上海', '')
    # 大中城市房屋价格指数
    house_price_index.main('北京', '2016-05')