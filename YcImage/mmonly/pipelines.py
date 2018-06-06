# -*- coding: utf-8 -*-
import requests
import datetime

class mmonlyPipeline(object):
    def process_item(self, item, spider):
        count = 0
        detailURL = item['detailURL']
        fileName = item['fileName']
        while True:
            try:
                print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), u'正在保存图片：', detailURL
                print u'文件：', fileName
                image = requests.get(detailURL)
                f = open(fileName, 'wb')
                f.write(image.content)
                f.close()
            except Exception, e:
                print fileName, 'other fault:', e
                count += 1
            else:
                print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), fileName, u'保存成功！'
                break
        return item
