# python 自省 明天继续


a = [1, 2, 3]
b = {'a': 1, 'b': 2, 'c': 3}
c = True

print(type(a))
print(dir(a))
# print(getattr(a)) # 返回一个对象属性值
print(hasattr(a))
print(isinstance(a, list))
