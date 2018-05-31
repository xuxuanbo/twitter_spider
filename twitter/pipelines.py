# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class TwitterPipeline(object):
    def process_item(self, item, spider):
        save_path = '/home/hadoopnew/下载/twisty/twisty-resuslt/TwiSty-DE/'
        fs = open(save_path+item['user_id'].encode('utf-8')+'.json','a')
        json.dump({item['twitter_id']:item['text']},fs,indent=4)
        fs.write('\n')
        return item
