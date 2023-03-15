# python 中单下划线 和 双下划线

class MyClass():
    def __init__(self):
        self.__superprivate = "Hello"
        self._semiprivate = ",world"


mc = MyClass()
print(mc._MyClass__superprivate)
print(mc._semiprivate)
print(mc.__dict__)

# 解释
# __x__: python 内部的变量名，用来区分其他用户自定义的名称，以防止冲突
# _x: 私有变量
# __x :通过对象名._类名__xxx这样的方式可以访问.
