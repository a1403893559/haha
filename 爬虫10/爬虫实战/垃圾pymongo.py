# import pymongo
#
# client = pymongo.MongoClient('lochlhost',27017)
#
# db = client.run
#
# jh = db.collections
# print(jh)
# hh = db.mongo.find()
#
# print(hh)

# pip3 install pymongo
import pymongo

# 链接mongodb数据库
pymongo.MongoClient('localhost',27017)
pymongo.MongoClient('127.0.0.1',27017)

# 链接方式二
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

# 如何获取数据库
article_db = client.run
# 获取数据库下面的集合

articlenovel = article_db.mongo

# 查询所有的数据文档
results = articlenovel.find()
for dict in results:
    print(dict)

print(results)

# 获取第一条数据库
result = articlenovel.find_one()
print(result)

# 如果数据库存在就获取 如果不存在就创建
db = client.meinv
# # 如果集合存在就获取，如果不存在的创建
model = db.model

document = {
    'name':'sunwenxiang',
     'age':'21',
     'class':'201',
     'hight':173,
 }
document1 = {
    'name':'sunwenxiang1',
    'age':'21',
    'class':'202',
    'hight':174,
}
document2 = {
    'name':'sunwenxiang3',
    'age':'21',
    'class':'203',
    'hight':175,
}
document3 = {
    'name':'sunwenxiang',
    'age':'21',
    'class':'204',
    'hight':176,
}
#数据插入
result = model.insert(document)
# result = model.insert([document1,document2,document3])
# [objectID('5B29B76a9960d69f83ef894),]
print(result)
# 获取集合中的所有数据
results = model.find()
for dict in results:
    print(dict)
#获取一条数据
result = model.find_one()
#条件查询
result = model.find({'name':'sunwenxiang1'})
for dict in result:
    print(dict)
print(result)

#获取一条满足条件的数据
result = model.find_one({'name':'sunwenxiang1'})
print(result)


results = model.find().skip(1)
for dict in results:
    print(dict)

#跳过第一条数据，获取后2条的数据
results = model.find().skip(1).limit(2)
for dict in results:
    print(dict)
#更新数据
result = model.update({'name':'sunwenxiang1'},{'$set':{'hight':180}})
print(result)

#查看更新后的结果是否正确
result = model.find_one({'name':'sunwenxinag1'})
print(result)


#排序
#升序
results = model.find().sort('age',1)
#
results = model.find().sort('age',-1)

for dict in results:
    print(dict)
# seve跟update区别是什么? 如果update更新的内容（—id) 在集合中
