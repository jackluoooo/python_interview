# __new__ 和 __init__ 的区别

#__new__是一个静态方法,而__init__是一个实例方法.
# __new__方法会返回一个创建的实例,而__init__什么都不返回.
# 只有在__new__返回一个cls的实例时后面的__init__才能被调用.
# 当创建一个新实例时调用__new__,初始化一个实例时用__init__.

class Test(object):
    _dict = dict()

    def __init__(self):
        print("开始init咯")
        Test._dict['key'] = self
        print("")

    def __new__(cls):
        if 'key' in Test._dict:
            print("已经存在咯")
            return Test._dict['key']
        else:
            print("NEW")
            return super(Test, cls).__new__(cls)


t1 = Test()
t2 = Test()
t3 = Test()
