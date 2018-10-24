#檔案名稱：day16_1
from tornado.httpclient import HTTPClient
from tornado.httpclient import AsyncHTTPClient

#同步I/O操作展示
def synshow():
    http_client = HTTPClient()
    response = http_client.fetch("https://ithelp.ithome.com.tw/")
    #阻塞發生
    print (response)
    print ("hello，這是同步阻塞的狀況，我已經跟IT邦網站連線了")

#非同步展示
def asynshow():
    http_client = AsyncHTTPClient()
    http_client.fetch("https://ithelp.ithome.com.tw/",callback = test())
    print ("hello，這是非同步的狀況，我已經跟IT邦網站連線了")

def test():
    print("ok，你好，我是非同步")

#請自行註解 synshow 和 asynshow，個別比較差異

#synshow()

asynshow()
