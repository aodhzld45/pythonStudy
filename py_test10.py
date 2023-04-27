#Python에서의 함수(Function)
# 기본 구조 
""" 
파이썬(Python) 들여쓰기 중요
def 함수명(매개변수):
<수행할 문장1>
<수행할 문장2>    
"""

#함수 사용하기
def add(a,b):
    return a + b
a = 3
b = 4
c = add(a, b)
print(c)

# 매개변수(parameter)에 초깃값 미리 설정하기
def say_myself(name, age, man=True):
    print('나의 이름은 %s 입니다.' % name)
    print('나이는 %d살 입니다.' % age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
        
print(say_myself('서현석', 28))

###################################################
###################################################

#lambda 함수
"""
기본 구조

함수명 = lambda 매개변수1, 매개변수2, ... : 매개변수를 이용한 표현식

def f01(n1):
    return n1 + 10 이라는 함수 일 때
    
########## lamda로 변환하면 ###########
lambda n1: n1 + 10
lambda 매개변수 : 리턴값(실행할 내용)

"""
# 파이썬을 기본적으로 문자열 String으로 입력 받음
# a = input('숫자를 입력하세요 = ').split() # split가 list로 만들어줌
# for n in a:
#     print(a, type(a))

# print('a', a, type(a))

# b = int(a)
# print(type(b))  

##### python map 합수 기본 설명.
"""
    기본 구조
    map(function, iterable)
    첫번째 매개변수(parameter)에는 함수(Function)가 오고
    두번째 매개변수(parameter)에는 반복 가능한 자료형(리스트, 튜플 등)을 명시한다.
""" 

def int01(n):
    print('int01함수 실행 :', n, type(n))
    return int(n) % 2 == 1

# num = list(map(int01, input('숫자를 입력하세요.').split()))

# print(num, type(num))

# num = list(map(lambda n : int(n) + 1 , input('숫자를 입력하세요 = ').split()))

# filter() 함수는 입력된 리스트에서 조건을 만족하는 요소만 추출

num = list(filter(lambda n: int(n) % 2 == 1, input('숫자를 입력하세요: ').split()))

print(num, type(num))


