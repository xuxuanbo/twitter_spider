# -*- coding: utf-8 -*-
import scrapy
from twitter.items import TwitterItem
from scrapy.selector import Selector
from scrapy import log
from scrapy.http import Request,FormRequest
import MySQLdb
from twitter.items import TwitterItem
import json
import os

# import doubancomment.settings
class LessionSpider(scrapy.Spider):
    name = 'see'
    headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
}
    def start_requests(self):
        twitter_dict = self.get_twitter_id()
        for i in twitter_dict:
            for j in twitter_dict[i]:
                yield scrapy.Request(url="https://twitter.com/kawhileonard/status/"+j, callback=self.get_twitter,dont_filter = True,meta={ 'cookiejar':1 ,
                        'data': { 'user_id':i,'twitter_id':j
                        }
                    })
    def get_twitter(self,response):
        # print response.body
        text = response.xpath("//div[@class='tweet-text']").xpath('string(.)').extract_first()
        data  = response.meta['data']
        data.update({'text':text})
        yield TwitterItem(data)
    def get_twitter_id(self):
        spath = '/home/hadoopnew/下载/twisty/twisty-test/TwiSty-DE.json'
        fs = open(spath)
        jsObj = json.load(fs)
        twitter_dict = {}
        for i in jsObj:
            twitter_dict[i]=[]
            for j in jsObj[i]['other_tweet_ids']:
                twitter_dict[i].append(j)
            for j in jsObj[i]['confirmed_tweet_ids']:
                twitter_dict[i].append(j)
        fs.close()
        return twitter_dict