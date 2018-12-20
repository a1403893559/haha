import pymongo
import redis

def main():
    mongoclient = pymongo.MongoClient('127.0.0.1',27017)
    rediscli = redis.StrictRedis('127.0.0.1',6379,0)


    db = mongoclient['hongniang']

    HN = db['HN']

    while True:
        source,data = rediscli.blpop(['HongNiang:items'])
        print(source,data)

if  __name__ ==  '__main__':
    main()