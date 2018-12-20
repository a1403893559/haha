import pymysql
db = pymysql.connect('localhost','root','139434','爬虫',use_unicode=True,charset='utf8')
kk = db.cursor()
def fenye():
    shuru = int(input('输入您的页码'))
    a = (shuru - 1)*15
    b = a + 15
    er = "select * from 分页 limit {0},{1}".format(a,b)
    kk.execute(er)
    o = kk.fetchall()
    print (o)
    db.commit()

fenye()