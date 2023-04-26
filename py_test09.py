import copy
# a = [10,20,30,40]
a = [10, 20, [31, 32, [331,332,333]], 40, 50 ]

a[0] = 100
a[1] = ['p', 'y', 't', 'h', 'o', 'n']

b = a
c = a[:]
d = copy.copy(a)
e = copy.deepcopy(a)

print(a, id(a))
print(b, id(b))
print(c, id(c))
print(d, id(d))
print(e, id(e))

#b = a
#print(b, id(b))

# b = a
# b = a[:]
# a[0] = 11
# c = b = a.copy()
# d = copy.copy(a)
# e = copy.deepcopy(a)

# print('a : ', a , id(a), id(a[0]), id(a[1]), id(a[2]), id(a[3]))
# print('b : ', b , id(b), id(b[0]), id(b[1]), id(b[2]), id(b[3]))
# print('c : ', c , id(c), id(c[0]), id(c[1]), id(c[2]), id(c[3]))
# print('d : ', d , id(d), id(d[0]), id(d[1]), id(d[2]), id(d[3]))
# print('e : ', e , id(e), id(e[0]), id(e[1]), id(e[2]), id(e[3]))




