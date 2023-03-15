# python 里的拷贝
import copy

a = [1, 2, 3, 4, ['a', 'b']]
b = a
c = copy.copy(a)  #
d = copy.deepcopy(b)  # 完全是一个新的变量复制 和之前已经没有关系了

a.append(5)
a[4].append('c')

print('a = ', a)
print('b = ', b)
print('c = ', c)
print('d = ', d)

