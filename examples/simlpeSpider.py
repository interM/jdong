from jdong import KeyList
from jdong import Good
from pymongo import MongoClient

client = MongoClient()
db = client['jdong']
col = db['tea']

k = KeyList('茶叶')
for i in range(50):
    datas = k.get_relist(i)
    for i in datas:
        url = i['link']
        g = Good(url=url)
        for j in range(30):
            comments = g.get_comments(j)
            col.insert(comments)

