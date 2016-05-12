# -*- coding: utf-8 -*-

import json
import codecs


class DoubanPipeline(object):
    def __init__(self):
        self.file = codecs.open('douban_reviews.json', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n" + "\n"
        # print line
        self.file.write(line.decode("unicode_escape"))
        return item





    # Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# from scrapy import signals
# from scrapy.exporters import JsonLinesItemExporter
#
#
# class JsonExportPipeline(object):
#
#     def __init__(self):
#         self.files = {}
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         pipeline = cls()
#         crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
#         crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
#         return pipeline
#
#     def spider_opened(self, spider):
#         json_file = open('%s_products.json' % spider.name, 'w+b')
#         self.files[spider] = json_file
#         self.exporter = JsonLinesItemExporter(json_file)
#         self.exporter.start_exporting()
#
#     def spider_closed(self, spider):
#         self.exporter.finish_exporting()
#         json_file = self.files.pop(spider)
#         json_file.close()
#
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item

