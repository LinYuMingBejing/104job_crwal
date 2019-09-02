# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from job104_crawl.items import Job104CrawlItem

class Job104Spider(CrawlSpider):
    name = 'job104'
    allowed_domains = ['www.104.com.tw']
    start_urls = ['https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=python&order=14&asc=0&page=1&mode=s&jobsource=2018indexpoc']

    rules = (
        Rule(LinkExtractor(allow=r'.+keyword=python.+page=\d+\&mode=s.+'), follow=True),
        Rule(LinkExtractor(allow=r'.+/job/[a-z0-9]+\?jobsource=jolist_b_relevance'), follow=True,callback='parse_item'),
    )

    def parse_item(self, response):
        jobtitle = response.xpath('//div[@class="center"]/h1/text()').get().strip()
        companyName = response.xpath('//span[@class="company"]/a/text()').get()
        jobContent = response.xpath('//div[@class="content"]/p/text()').getall()
        jobContent="".join(jobContent).strip()
        jobContent=jobContent.replace('\r','')
        address = response.xpath('//dd[@class="addr"]/text()').get().strip()
        jobtool = response.xpath('//dd[@class="tool"]/a/text()').getall()
        jobrequirement = response.xpath('//section[2]/div[@class="content"]/dl/dd[2]/text()').get()
        graduaterequirement = response.xpath('//section[2]/div[@class="content"]/dl/dd[3]/text()').get()    
        subjectrequirement = response.xpath('//section[3]/div[@class="content"]/dl/dd[3]/text()').get()
        updatetime = response.xpath('//time[@class="update"]/text()').get()
        item=Job104CrawlItem(jobtitle=jobtitle,companyName=companyName,jobContent=jobContent,address=address,jobtool=jobtool,jobrequirement=jobrequirement,graduaterequirement=graduaterequirement,
            subjectrequirement=subjectrequirement,updatetime=updatetime)
        return item
