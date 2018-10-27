# 檔案名稱：day19_ex1
#小作業 如何新增一個路由解析(url對映設定) 出現的是一張圖片
#!/usr/bin/env python
# -*- coding: utf-8 -*-






import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print("有人連線了")
        self.write("Hello tornado,歡迎你")

class EntryHandler(tornado.web.RequestHandler):
    def get(self):
        print("entry頁面連線了")
        self.write("Hello 這裡是entry 頁面")

def my_app():  #url對映
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/entry", EntryHandler),
        (r"/image/jpg/(.*)",tornado.web.StaticFileHandler,{"path": "assets/img"})
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
