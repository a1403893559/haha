import pymongo


client = pymongo.MongoClient('127.0.0.1',27017)
db=client['jishi']


def ch():
    collections = db['chxinwen']
    shuru = int(input('输入页码'))
    a = list(collections.find().skip(shuru*20).limit(20))
    print(a)


def haolai():

    collections = db['haolaiwu']
    shuru = int(input('输入页码'))
    a = list(collections.find().skip(shuru * 20).limit(20))
    print(a)

def dianying():
    shuru = input('输入名字')
    collections = db['haolaiwu']
    a = collections.find({'title':shuru})
    print(list(a))



def main():
    a = int(input('输入操作，1为查看中国新闻,2为好莱坞新闻,3为查看预告片'))
    if a == 1:
        ch()
    elif a ==2:
        haolai()
    elif a ==3:
        dianying()


if __name__ == '__main__':
    main()