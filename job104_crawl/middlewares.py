# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
from twisted.internet.defer import DeferredLock
class UserAgentDownloaderMiddleware(object):
    UserAgent=['Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    ]
    def process_request(self,request,spider):
        useragent = random.choice(self.UserAgent)
        request.headers['User-Agent'] = useragent

class IPProxyDownloaderMiddleware(object):
    PROXIES =['59.127.55.215:36773','60.250.243.228:3128','220.130.51.190:8080','106.104.12.180:80']
    def __init__(self):
        super(IPProxyDownloaderMiddleware,self).__init__()
        self.current_proxy = None
    def process_request(self,request,spider):
        proxy = random.choice(self.PROXIES)
        request.meta['proxy'] = 'http://%s'% proxy

    def process_response(self, request, response, spider):
        if response.status !=200 or 'captcha' in response.url: 
            print('%s這個ip被拉黑') % self.current_proxy
            proxy = random.choice(self.PROXIES)
            request.mata['proxy'] = 'http://%s'% proxy
            return request
        return response

