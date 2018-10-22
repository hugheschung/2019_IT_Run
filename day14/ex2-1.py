import pymongo

#連接本地端mongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#填入你的DB名稱
mydb_Name="HeartRate"

#設mydb繼承myclient[mydb_Name]的屬性。
mydb = myclient[mydb_Name]

#印出所有DB的名稱
print("目前存在的DB有  ",myclient.list_database_names())

#如果DB存在，則印出
dblist = myclient.list_database_names()
if mydb_Name in dblist:
  print("您的DB: {0}存在".format(mydb_Name))


#day13第二小節加入的地方-----------
#你的collection名稱
mycol = mydb["h1f001"]


print("目前存在的collection有  ",mydb.list_collection_names())

#如果collection存在，則印出
collist = mydb.list_collection_names()
if "h1f001" in collist:
  print("您的collection存在")


#day14 第2.1節加入的地方------刪除多筆
myquery = { "name": {"$regex": "^h"} }

x = mycol.delete_many(myquery)

print(x.deleted_count, " documents deleted.")
