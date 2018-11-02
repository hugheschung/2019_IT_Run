"""
檔案名稱：day24_ex2
檔案用途：server程式碼 與 myclass 合併，並實作基礎websocket 通訊。
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-






import tornado.ioloop
import tornado.web
import tornado.websocket  #day19_ex2新增的


class myclass():   #自訂類別，用於mongoDB的調用。
    """docstring for myclass."""
    def __init__(self,mydb_Name):
        #連接本地端mongoDB
        import pymongo
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        #設mydb繼承myclient[mydb_Name]的屬性。
        self.mydb = self.myclient[mydb_Name]
        #你的collection名稱

    def show_state(self):
        print("目前存在的DB有  ",myclient.list_database_names())
        print("目前存在的collection有  ",self.mydb.list_collection_names())

    def insert_data(self, collection, data): #新增功能
        #實作:新增功能
        self.mycol = self.mydb[collection]
        self.mydata = data
        self.mycol.insert_one(self.mydata)   #單筆插入資料指令
        print("資料單筆新增成功")

    def get_data(self, collection, myquery = {}, noquery={"_id": 0}):  #獲得資料
        self.mycol = self.mydb[collection]
        self.myquery = myquery  #要搜尋的資料 空白全部搜尋，填值搜尋特定值。
        self.noquery = noquery  #要排除的資料

        self.myfind = self.mycol.find(myquery)
        self.xx = list(self.myfind)
        return self.xx

    def delete_data(self, collection, mydelete):  #實作：會員刪除
        self.mycol = self.mydb[collection]
        self.mydelete = mydelete
        self.mycol.delete_one(self.mydelete)

    def updata(self, collection, myquery, new_values):  #實作：會員更新
        self.mycol = self.mydb[collection]
        self.myquery = myquery
        self.new_values = new_values
        self.mycol.update_one(self.myquery, self.new_values)




class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print("有人連線了")

class EntryHandler(tornado.web.RequestHandler):
    def get(self):
        print("entry頁面連線了")
        self.write("Hello 這裡是entry 頁面")

class IThelp_SocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):  #允許外網連入
        return True
    def open(self):  #開啟時的動作
        print("WebSocket opened")

#day24 中修改的----------------
    def on_message(self, message):  #當訊息進入時，"觸發"
        self.xx = message
        if (self.xx == "v1"):
            print("v1")
        elif (self.xx == "v2"):
            print("v2")
        self.write_message("你輸入的是 " +self.xx)

    def on_close(self):   #當連線中斷時，"觸發"
        print("WebSocket closed")

def my_app():  #url對映
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/entry", EntryHandler),
        (r"/image/jpg/(.*)",tornado.web.StaticFileHandler,{"path": "image/jpg"}),
        (r"/ws", IThelp_SocketHandler),
    ])

def main():
    global port
    port = 8888

    app = my_app()
    app.listen(port)
    print("歡迎使用tornado，您的連線port為:{0} ".format(port))
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
