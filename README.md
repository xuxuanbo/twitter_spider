# twitter_spider
using scrapy tp crawl the twitter according to the twitter id
使用方法：
1.下载twitter文件夹以及scrapy.cfg文件，打包在一个文件夹中，进入该文件夹，使用scrapy crawl see命令即可进行爬取。
2.twitter/twitter/spiders/spider.py文件中LessionSpider类的get_twitter_id方法中的spath存放的是存放六国twitter的路径，请根据实际情况修改路径。
3./twitter/twitter/pipelines.py文件中的TwitterPipeline类的process_item方法的save_path指向存储路径，请确保确实有该文件夹的存在。
