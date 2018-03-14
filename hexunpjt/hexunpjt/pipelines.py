# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

# class HexunpjtPipeline(object):
#     def __init__(self):
#         #先连接刚刚使用sql语句创建的数据库
#         self.conn = pymysql.connect(
#             host = '127.0.0.1',
#             user = 'root',
#             passwd = 'root',
#             db = 'hexun'
#             )
#
#     def process_item(self, item, spider):
#         #每个博文列表页包含多篇博文的信息，我们可以通过for循环一次处理各个博文的信息
#         for j in range(0,len(item['name'])):
#             #将获取到的name，url，hits，comment分别赋给各个变量
#             name = item['name'][j]
#             url = item['url'][j]
#             hits = item['hits'][j]
#             comment = item['comment'][j]
#             #将获取的对应数据插入到数据库的数据表中
#             sql1 = 'insert into myhexun(name,url,hits,comment) VALUES ('"+name+"','"+url+"','"+hits+"','"+comment+"')'
#             #执行sql语句
#             self.conn.query(sql1)
#         return item
#
#     def close_spider(self,spdier):
#         #关闭数据库的连接
#         self.conn.close()

class HexunpjtPipeline(object):

    def __init__(self):
        #刚开始时连接对应数据库
        self.conn=pymysql.connect(host="127.0.0.1", user="root", passwd="root", port=3306, db="hexun")

    def process_item(self, item, spider):
        #每一个博文列表页中包含多篇博文的信息，我们可以通过for循环一次处理各博文的信息
        for j in range(0, len(item["name"])):
            # 将获取到的name、url、hits、comment分别赋给各变量
            name=item["name"][j]
            url=item["url"][j]
            hits=item["hits"][j]
            comment=item["comment"][j]
            cur = self.conn.cursor()
            #构造对应的sql语句，实现将获取到的对应数据插入数据库中
            sql="insert into myhexun(name,url,hits,comment) VALUES('"+name+"','"+url+"','"+hits+"','"+comment+"')"
            #通过query实现执行对应的sql语句
            cur.execute(sql)
        return item


    def close_spider(self,spider):
        # 最后关闭数据库连接
        self.conn.close()

