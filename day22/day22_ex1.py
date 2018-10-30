# 檔案名稱：day22_ex1
# 檔案用途：實作：新增功能


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


#實作:新增功能
mydata = {
            "user_id": "A1234567",
            "password": "12345678",
            "name":"黑修斯",
            "性別":"男",
            "住址":"忠孝東路走九遍",
            "電話":"28825252" }  #資料

x = mycol.insert_one(mydata)   #單筆插入資料指令

print("資料單筆新增成功")
