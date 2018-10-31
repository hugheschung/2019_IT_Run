# 檔案名稱：day23_test
# 檔案用途：用於單個功能實作測驗


import pymongo

#連接本地端mongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#填入你的DB名稱
mydb_Name="day21"

#設mydb繼承myclient[mydb_Name]的屬性。
mydb = myclient[mydb_Name]

#印出所有DB的名稱
print("目前存在的DB有  ",myclient.list_database_names())

#如果DB存在，則印出
dblist = myclient.list_database_names()
if mydb_Name in dblist:
  print("您的DB: {0}存在".format(mydb_Name))

#第二小節加入的地方-----------
#你的collection名稱
mycol = mydb["main"]


print("目前存在的collection有  ",mydb.list_collection_names())

#如果collection存在，則印出
collist = mydb.list_collection_names()
if mycol in collist:
  print("您的collection存在")



# 實作功能測試由下開始撰寫
#實作:查詢功能
myquery = {}  #要搜尋的資料 空白全部搜尋，填值搜尋特定值。
noquery = {"_id": 0}  #要排除的資料
import pprint
for x in mycol.find(myquery,noquery): #使用for印出全部
  pprint.pprint(x)
'''
#實作:會員刪除
myquery = { "user_id": "A7654321" }

mycol.delete_one(myquery)

print("刪除成立!!")
'''

#實作：會員更新
myquery = { "name": "黑修斯" }
new_values = { "$set": { "name": "嘿嘿嘿" } }

mycol.update_one(myquery, new_values)

print("更新成功-----------")

#實作:查詢功能
myquery = {}  #要搜尋的資料 空白全部搜尋，填值搜尋特定值。
noquery = {"_id": 0}  #要排除的資料
import pprint
for x in mycol.find(myquery,noquery): #使用for印出全部
  pprint.pprint(x)
