# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from papu.items import PapuItem

class PapuSpider(Spider):
    name = "test"
    allowed_domains = ["apunkabollywood.us"]
    start_urls = [
        "http://www.apunkabollywood.us/browser/category/view/8264/diljit-dosanjh---disco-singh-(apr-2014)"
    ]
        
    def parse(self, response):
        sel = Selector(response)
        songs = sel.xpath('//td[contains(small,"MB")]')
        for url in sel.xpath('//td[contains(small,"MB")]/a/@href').extract():
            return Request(url, callback=self.parse2)
            
        items = []
        for song in songs:
            item = PapuItem()
            item['songtitle'] = song.xpath('a/text()').extract()
            item['link'] = song.xpath('a/@href').extract()
            items.append(item)
        return items
    
    def parse2(self, response):
        print "HEYO!"