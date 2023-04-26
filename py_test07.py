# 집합 자료형 set
# 집합 자료형의 특징
# 1. 중복을 허용하지 않는다.
# 2. 순서가 없다(Unordered) -> 인덱싱을 통해 자료형의 값을 얻을 수 없다.
s1 = set([1,2,3])
s2 = set("Hello") # set() 괄호 안에 리스트를 입력하여 만들 수 있음.

print(s1, type(s1))
print(s2, type(s2))

# 교집합, 합집합, 차집합 구하기
s3 = set([1,2,3,4,5,6])
s4 = set([4,5,6,7,8,9])

# 1. 교집합 - & 기호 사용
print(s3 & s4)

# 2. 합집합 - |(pipe) 사용 -> 중복된 값은 한 개씩만 표현된다.
# 2-1 - union 함수를 사용 
print(s3 | s4)
print(s3.union(s4), type(s3.union(s4)))

# 3. 차집합 - (-) 마이너스 기호 사용
# 3-1. difference 함수를 사용
print(s3 - s4)
print(s3.difference(s4))

##################################################
##################################################

# 집합 자료형 관련 함수들.

# 1. 값 1개 추가하기 - add()
add = set(['a','b','c','d','e'])
add.add('추가된 값')
print(add, type(add))

# 2. 값 여러개 추가하기 - update()
update = set(['h','e','l','l','o'])
update.update(['python'])
print(update,type(update))

# 3. 특정 값 제거하기 - remove()
remove = ([1,2,3,4,5, '삭제될 값'])
remove.remove(remove[5]
              )
# re_lst = list(remove)
# print(type(re_lst))

# remove.remove(re_lst[5])

print(remove)

