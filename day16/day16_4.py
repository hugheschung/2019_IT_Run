#檔案名稱：day16_4
#yield 使用II


def yield_show():
    print ("我是1號")
    yield 1

    print ("我是8號")
    print ("等一下，我是day16_4的範例")
    yield 8

    print ("我是5號")
    yield 5

for i in yield_show():
    print (i)
