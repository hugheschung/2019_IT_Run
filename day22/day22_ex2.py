# 檔案名稱：day22_ex2
# 檔案用途：實作：查詢功能


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


#實作:查詢功能
myquery = {}  #要搜尋的資料 空白全部搜尋，填值搜尋特定值。
noquery = {"_id": 0}  #要排除的資料
import pprint
for x in mycol.find(myquery,noquery): #使用for印出全部
  pprint.pprint(x)


"""
#小作業：排除資料選項清空，得到的資料如何?  參考解答
#實作:查詢功能
myquery = {}  #要搜尋的資料 空白全部搜尋，填值搜尋特定值。
noquery = {}  #要排除的資料
import pprint
for x in mycol.find(myquery): #使用for印出全部
  pprint.pprint(x)
"""
