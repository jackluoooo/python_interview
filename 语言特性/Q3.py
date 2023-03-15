# 静态方法和类方法 staticmethod 和 classmethod
def foo(x):
    print("executing foo(%s)" % (x))


class A(object):
    def foo(self, x):  # 实例方法的调用离不开实例
        print("executing foo(%s,%s)" % (self, x))

    @classmethod
    def class_foo(cls, x):  # 它传递的是类而不是实例
        print("executing class_foo(%s,%s)" % (cls, x))

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)


a = A()
a.foo(1)
a.class_foo(1)
a.static_foo(1)

A.class_foo(2)
A.static_foo(2)
A.foo(2)
