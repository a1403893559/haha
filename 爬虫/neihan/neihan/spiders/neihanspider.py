# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from neihan.items import NeihanItem

class NeihanspiderSpider(CrawlSpider):
    name = 'neihanspider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/']

    rules = (
        Rule(LinkExtractor(allow=r'/.*?/',restrict_xpaths='//div[@id="menu"]'), follow=True),  #匹配上面的大分类
        Rule(LinkExtractor(allow=r'/.*?/page/\d+/'), follow=True),                         #匹配上面的分页
        Rule(LinkExtractor(allow=r'/article/\d+'), callback='parse_item', follow=True),     #匹配 每一个文章的详情
    )

    def parse_item(self, response):
        item = NeihanItem()
        item['content'] = response.xpath('//div[@class="content"]/text()').extract_first('暂无')   #获取内容
        item['author'] = response.xpath('//h2/text()').extract_first('暂无')                      #获取作者
        item['laugh'] = response.css('span.stats-vote i::text').extract_first('暂无')           #获取好笑的个数
        item['talk'] = response.css('span.stats-comments i.number::text').extract_first('暂无')   #获取评论数量
        item['img'] = response.css('div.thumb img::attr(src)').extract_first('暂无')              #获取图片地址

        yield item

