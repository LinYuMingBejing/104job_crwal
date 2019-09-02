# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class Job104CrawlPipeline(object):
    def __init__(self):
        dbparams={
            'host' : '127.0.0.1',
            'port' : 3306,
            'user' : 'root',
            'password' : 'a828215362',
            'database' : '104job',
            'charset' : 'utf8'
        }
        self.conn = pymysql.connect(**dbparams)
        self.cursor = self.conn.cursor()
        self._sql = None
    def process_item(self, item, spider):
        params = (item['jobtitle'],item['companyName'],item['jobContent'],item['address'],item['jobtool'],item['jobrequirement'],item['graduaterequirement'],item['subjectrequirement'],item['updatetime'])
        self.cursor.execute(self.sql, params)
        self.conn.commit()
        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql="""
            insert into 104job(id, jobtitle, companyName, jobContent, address, jobtool, jobrequirement, graduaterequirement, subjectrequirement, updatetime)
            values(null, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            return self._sql
        return self._sql


