# 파이썬의 기본객체 : str, list, int, float ...
# 파이썬에서도 Class는 객체(Object)로 취급

# 리스트 자료형 = 배열과 비슷
# 정수 리터럴 / 상수 리터럴
# 리스트 안에는 어떠한 자료형도 가능

str1 = 'hello'
test01 = [1,2,3,['a','b','c', str1,['d','e','f',str1]]] #리스트 안에 리스트 -> 다차원 배열 구현 가능 
# print(test01[3][3][0]) #삼중리스트 구현
print(test01[0],type(test01[0]))

print(id(test01),type(test01))
print(id(test01[0]), type(test01[0]))
print(id(test01[1]))
print(id(test01[2]))
print(id(test01[3]))

print(id(str1))
print(id(test01[3][3]))
print(id(test01[3][4][3]))

# print(id(test01), type(test01), dir(test01))

# print(str1)
# print(id(str1[0]),id(str1[1]),id(str1[2]),id(str1[3]),id(str1[4]))

# str1[2] ,str1[3]

# print(id(str1), type(str1), dir(str1))

# n1 = 10
# n2 = 3.14
# print(n1, n2, type(n1), type(n2))

# 리스트 관련 함수들

# 1. append - 리스트에 요소 추가
append = [1,2,3]
append.append(4)
print(append)

# 2. sort
sort = [5, 2, 3, 1, 4]
sort.sort() # 순서대로 정렬
print(sort)

# 3. reverse

# 4. index

# 5. insert

# 6. remove

# 7. pop

# 8. count

# 9. extend

# 10 



