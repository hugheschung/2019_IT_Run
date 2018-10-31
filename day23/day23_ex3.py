"""
檔案名稱：day23_ex3
檔案用途：功能封裝，並加入會員刪除與會員更新
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

    def delete_data(self, mydelete):  #實作：會員刪除
        self.mydelete = mydelete
        self.mycol.delete_one(self.mydelete)

    def updata(self, myquery, new_values):  #實作：會員更新
        self.myquery = myquery
        self.new_values = new_values
        self.mycol.update_one(self.myquery, self.new_values)


# 定義一個新的myclass物件為b
b = myclass(mydb_Name="day21", collection="main")

#刪除功能
mydelete = { "user_id": "A7654321" }
b.delete_data(mydelete)

#更新功能
updata_value = { "name": "黑修斯" }
new_data = { "$set": { "name": "嘿嘿嘿" } }
b.updata(updata_value, new_data)

import pprint

pprint.pprint(b.get_data())
