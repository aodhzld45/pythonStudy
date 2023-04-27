################################
# iterable의 작동 원리
################################

n = [10, 20, 30, 40, 50] # 리스트
n2 = (10, 20, 30, 40, 50) # 튜플
n3 = {10, 20, 30, 40, 50} # 집합
n4 = {1:10, 2:20, 3:30, 4:40, 5:50} #딕셔너리

print(n, type(n))
# print(dir(n))

n2 = n.__iter__()
print(n2, type(n2))

n3 = n2.__iter__() # n2와 같음
print(n3, type(n3))

print(n3.__next__())
print(n3.__next__())
print(n3.__next__())
print(n3.__next__())
print(n3.__next__())


