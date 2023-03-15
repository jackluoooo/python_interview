# 迭代器和生成器

# 切片
L = ['M', 'S', 'T', 'B', 'J']
print([L[0], L[1], L[2]])
print(L[0:3])
print(L[:3])
print(L[3:])
print(L[:-1])  # 包头不包尾
print(L[0::2])  # 每隔几个数取一个

# 迭代
# 首先判断一个对象是可迭代的对象
from collections.abc import Iterable

print(isinstance('abc', Iterable))
# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# 列表生成式
print([x * x for x in range(1, 11)])

# 把一个列表生成式中的[] 改成 (),就创建了一个 generator
# 可以利用next() 函数来获得参数 直到抛出 StopIteration

# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
