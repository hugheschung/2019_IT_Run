# 檔案名稱：day17_ex1
#第一個非同步網站請求
#!/usr/bin/env python
# -*- coding: utf-8 -*-



import tornado.ioloop
import tornado.web
import tornado.httpclient

class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        http.fetch("https://ithelp.ithome.com.tw/",
                   callback=self.on_response)

    def on_response(self, response):
        if response.error:
            raise tornado.web.HTTPError(500)
        self.write(response.body)
        self.finish()


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
