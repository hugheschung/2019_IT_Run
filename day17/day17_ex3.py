# 檔案名稱：day17_ex3
#第一個同步網站請求  小作業
#!/usr/bin/env python
# -*- coding: utf-8 -*-



#!/usr/bin/env python
# -*- coding: utf-8 -*-



import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print("有人連線了")
        self.write("Hello tornado,歡迎你")

def my_app():
    return tornado.web.Application([
        (r"/", MainHandler),
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
