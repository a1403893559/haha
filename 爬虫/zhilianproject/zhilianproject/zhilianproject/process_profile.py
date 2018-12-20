import json
import redis
import pymongo
import pymysql
def main():
    #print('哈哈')
    # 指定Redis数据库信息
    rediscli = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)

    # # 指定MongoDB数据库信息
    # mongocli = pymongo.MongoClient(host='localhost', port=27017)
    # # 创建数据库名
    # db = mongocli['suibian']
    # # 创建表名
    # sheet = db['suibian']
    #
    # while True:
    #     # FIFO模式为 blpop，LIFO模式为 brpop，获取键值
    #     source, data = rediscli.blpop("zhilian:items")
    #     data = data.decode('utf-8')
    #     item = json.loads(data)
    #     try:
    #         sheet.insert(dict(item))
    #         print ('插入成功')
    #     except KeyError:
    #         print ('插入失败')


    # 指定mysql数据库
    db = pymysql.connect('localhost', 'root', '139434', '爬虫', use_unicode=True, charset='utf8')

    while True:

        # FIFO模式为 blpop，LIFO模式为 brpop，获取键值
        source, data = rediscli.blpop("zhilian:items")
        print(source,data)
        data = data.decode('utf-8')
        item = json.loads(data)
        #item = json.loads(data.decode('utf-8'))
        print(item)
        try:
            # 使用cursor()方法获取操作游标
            cur = db.cursor()
            # 使用execute方法执行SQL INSERT语句
            sql = 'insert into suibian values(0,"%s")'%(item['address'])
            cur.execute(sql)
            # 提交sql事务
            db.commit()
            # 关闭本次操作
            cur.close()
            print("插入成功")
        except:
            print('插入失败')


if __name__ == '__main__':
    main()