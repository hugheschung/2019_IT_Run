'''
檔案名稱：test_server (源於day19_ex2)
檔案用途：用於測試使用，部分程式碼有修改。
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-






import tornado.ioloop
import tornado.web
import tornado.websocket  #day19_ex2新增的

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

    def on_message(self, message):  #當訊息進入時，"觸發"
        print (message)
        self.write_message("你輸入的是 " + message)

    def on_close(self):   #當連線中斷時，"觸發"
        print("WebSocket closed")

def my_app():  #url對映
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/entry", EntryHandler),
        (r"/image/jpg/(.*)",tornado.web.StaticFileHandler,{"path": "assets/img"}),
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
