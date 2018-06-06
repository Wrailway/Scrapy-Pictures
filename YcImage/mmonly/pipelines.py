# -*- coding: utf-8 -*-
import requests
import sys
import threading
reload(sys)
sys.setdefaultencoding('utf-8')

class mmonlyPipeline(object):
    def process_item(self, item, spider):
        count = 0
        detailURL = item['detailURL']
        path = item['path']
        fileName = item['fileName']
        while True:
            try:
                print u'正在保存图片：', detailURL
                print u'图片路径：', path
                print u'文件：', fileName
                image = requests.get(detailURL)
                f = open(path, 'wb')
                f.write(image.content)
                f.close()
                return item
            except Exception, e:
                print fileName, 'other fault:', e
                count += 1
            else:
                print u'图片保存成功！'
                break
