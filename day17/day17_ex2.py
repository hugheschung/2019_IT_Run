# 檔案名稱：day17_ex2
#第一個同步網站請求
#!/usr/bin/env python
# -*- coding: utf-8 -*-



#!/usr/bin/env python
# -*- coding: utf-8 -*-



import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):

        self.write("Hello tornado,歡迎你")

def my_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

def main():

    app = my_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
