import copy # from 키워드는 모듈안에서 특정한 기능만 골라서 사용이 가능.
# a = [10,20,30,40]
a = [10, 20, [31, 32, [331,332,333]], 40, 50]

dic1 = {'key1': 0, 'key2': 1, 'key3': 2, 'lst1' :[1,2,3,4,5]}

dc = copy.deepcopy(dic1)

print('첫번째 딕셔너리', dic1, id(dic1), type(dic1))
print('dc', dc, id(dc))

a[0] = 100
a[1] = ['p', 'y', 't', 'h', 'o', 'n']

b = a
c = a[:]
d = copy.copy(a)
e = copy.deepcopy(a)

# print("a = ", a, id(a))
# print("a[] 번지의 id값 = ", id(a[2]))
# print('b[] 번지의 id값  = ', id(b[2]))
# print('c[] 번지의 id값  = ', id(c[2]))
# print('d[] 번지의 id값  = ', id(d[2]))

# print('e[] 번지의 id값  = ', id(e[2])  ) # deepcopy

print('a[][] 번지의 id값 = ', id(a[2][2]))
print('d[][] 번지의 id값 = ', id(d[2][2]))
print('e[][] 번지의 id값 = ', id(e[2][2]))


# print('e[] 번지의 id값  = ', id(e[3])) # deepcopy

print("b = ", b, id(b))
print("c = ", c, id(c))
print("d = ", d, id(d))
print("e = ", e, id(e))

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




