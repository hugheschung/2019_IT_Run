"""
檔案名稱：day23_ex2
檔案用途：功能封裝
"""

class myclass():
    """docstring for myclass."""
    def __init__(self,mydb_Name,collection):
        #連接本地端mongoDB
        import pymongo
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        #設mydb繼承myclient[mydb_Name]的屬性。
        self.mydb = myclient[mydb_Name]
        #你的collection名稱
        self.mycol = self.mydb[collection]

    def show_state(self):
        print("目前存在的DB有  ",myclient.list_database_names())
        print("目前存在的collection有  ",self.mydb.list_collection_names())

    def insert_data(self,data): #新增功能
        #實作:新增功能
        self.mydata = data
        self.mycol.insert_one(self.mydata)   #單筆插入資料指令
        print("資料單筆新增成功")

    def get_data(self, myquery = {}, noquery={"_id": 0}):  #獲得資料
        self.myquery = myquery  #要搜尋的資料 空白全部搜尋，填值搜尋特定值。
        self.noquery = noquery  #要排除的資料

        self.myfind = self.mycol.find(myquery)
        self.xx = list(self.myfind)
        return self.xx


b = myclass(mydb_Name="day21", collection="main")
data ={
"user_id": "A7654321",
"password": "12345678",
"name":"hughes",
"性別":"男",
"住址":"中山北路走七遍",
"電話":"52522882" }  #資料

b.insert_data(data)
print(b.get_data())

import pprint

pprint.pprint(b.get_data())
