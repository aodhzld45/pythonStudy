# 파이썬의 기본객체 : str, list, int, float ...
# 파이썬에서도 Class는 객체(Object)로 취급

# 리스트 자료형 = 배열과 비슷
# 정수 리터럴 / 상수 리터럴
# 리스트 안에는 어떠한 자료형도 가능

str1 = 'hello'
test01 = [1,2,3,['a','b','c', str1,['d','e','f',str1]]] #리스트 안에 리스트 -> 다차원 배열 구현 가능 
# print(test01[3][3][0]) #삼중리스트 구현
# print(test01[0],type(test01[0]))

# print(id(test01),type(test01))
# print(id(test01[0]), type(test01[0]))
# print(id(test01[1]))
# print(id(test01[2]))
# print(id(test01[3]))

# print(id(str1))
# print(id(test01[3][3]))
# print(id(test01[3][4][3]))

# print(id(test01), type(test01), dir(test01))

# print(str1)
# print(id(str1[0]),id(str1[1]),id(str1[2]),id(str1[3]),id(str1[4]))

# str1[2] ,str1[3]

# print(id(str1), type(str1), dir(str1))

# n1 = 10
# n2 = 3.14
# print(n1, n2, type(n1), type(n2))

lst1 = []
# print(type(lst1))
# print(dir(lst1))
lst2 = lst1 # lst1의 주소값 참조.

lst1.append(10)

# print('lst1', lst1)
# print('lst2', lst2)

lst3 = list()
print('list3 type : ', type(lst3))
lst3.append([10,2,3,4,5])
lst3.append('hello')
lst3.append(10)
lst3[0].append([10,'apple'])

print(lst3)
print(id(lst3))

for i in lst3:
    print(id(lst3[0][5][1]))
   

print("================================================================================")

# 리스트 관련 함수들

# 1. append - 리스트에 요소 추가
append = [1,2,3]
append.append(4)
print('append = ', append)

# 2. sort - 리스트 정렬
sort = [5, 2, 3, 1, 4]
sort.sort() # 순서대로 정렬
print('sort = ', sort)

# 3. reverse - 리스트 뒤집기 : 리스트를 역순으로 뒤집어줌 / 이 때 현재의 리스트를 그대로 거꾸로 뒤집는다. 정렬 X
reverse = ['a', 'c', 'b'] 
reverse.reverse()
print('reverse = ', reverse)

# 4. index - 리스트의 값을 리턴한다 / 숫자 1의 위치는 index[0]이므로 0를 리턴하고, 숫자2의 위치는 index[1]이므로 1을 리턴 
index = [1,2,3]
index.index(1)
print('index = ', index.index(1),index.index(2))

# 5. insert - 리스트에 요소 삽입 / insert[0]자리에 문자열 삽입
insert = ['a,b,c', 'd,e,f']
insert.insert(0, '문자 삽입')
print('index = ', insert)

# 6. remove(x) - 리스트에서 첫번째로 나오는 x를 삭제
remove = ['a,b,c', 'd,e,f', 'g,h,i']
remove.remove('a,b,c')
print('remove = ', remove)

# 7. pop - 리스트의 맨 마지막 요소를 리턴하고 그 요소를 삭제한다. / 맨 마지막 요소인 'test' 문자열을 삭제
pop = [1,2,3,5,6,7,'test']
pop.pop()
print('pop = ', pop)

# 8. count(x) - 리스트에 포함된 요소 x의 개수 세기
count = [11,15,16,17,9,4,5,1,7,1]
print('count = ', count.count(1))

# 9. extend - 리스트 확장 : extend(x)에서 리스트만 올 수 있으며 원래의 extend 리스트에 x 리스트를 더함
extend = ['e','x']
extend.extend(['t','e'])

x = ['n','d'] 
extend.extend(x)
print('extend = ', extend)