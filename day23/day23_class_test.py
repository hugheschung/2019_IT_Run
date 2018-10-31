'''
檔案名稱：day23_class_test
檔案用途：class 練習
'''




#使用單一引數
class test1(object):
    """docstring for test1."""
    def __init__(self, arg):
        super(test1, self).__init__()
        self.arg = arg

a = test1(arg="單一參數")
print(a.arg)

#使用多個引數
class test2(object):
    """docstring for test2."""
    def __init__(self, arg, name, user_id):
        super(test2, self).__init__()
        self.arg = arg
        self.name = name
        self.user_id = user_id

b = test2(arg="多個參數", name="黑修斯", user_id="123456")
print("這是{0} 的範例，{1} 你好!! 您的帳號為 {2}".format(b.arg, b.name, b.user_id))


class tes3(object):
    """docstring for tes3."""
    def __init__(self, arg):
        super(tes3, self).__init__()
        self.arg = arg
