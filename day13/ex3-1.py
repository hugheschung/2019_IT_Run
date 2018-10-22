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


#第二小節加入的地方-----------
#你的collection名稱
mycol = mydb["h1f001"]


print("目前存在的collection有  ",mydb.list_collection_names())

#如果collection存在，則印出
collist = mydb.list_collection_names()
if "h1f001" in collist:
  print("您的collection存在")


#第三小節加入的地方---------多筆資料
  
mydict = { "name": "黑修斯", "says": "Hello 你好嗎?" }

mylist = [
  { "name": "黑修斯1", "says": "Hello 你好嗎?"},
  { "name": "黑修斯2", "says": "衷心感謝"},
  { "name": "黑修斯3", "says": "感謝有你"},
  { "name": "黑修斯4", "says": "接受我"},
  { "name": "黑修斯5", "says": "衷心感謝"},
  { "name": "黑修斯6", "says": "珍重相見"},
  { "name": "黑修斯7", "says": "期待再相逢"}
]

x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print("插入多筆資料成功 返回_id值 ",x.inserted_ids)
