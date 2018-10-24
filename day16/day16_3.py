#檔案名稱：day16_3
#yield 使用


def yield_show():
    print ("我是1號")
    yield 1
    print ("我是8號")
    yield 8
    print ("我是5號")
    yield 5

for i in yield_show():
    print (i)
