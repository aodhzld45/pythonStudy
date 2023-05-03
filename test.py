test1 = eval('1+2')
print(test1)

test2 = eval("'hi' + 'hello'")
print(test2)

print(int('f', 16))
print(int('10', 8))

class Person1: 
    pass
class Person2(Person1):
    pass

a = Person1()
b = Person2()

print(isinstance(b, Person1)) # isinstance는 부모 자식 관계도 체크가 가능하다.

import pickle
f = open('test.txt', 'wb')
data = {'aa': 'hello', 'bb':'world'}

pickle.dump(data, f)
f.close
f = open('test.txt', 'rb')
data = pickle.load(f)
print(data, type(data))


import random

result = []
while len(result) < 6:
    num = random.randint(1, 45)  # 1~45 사이의 숫자중 임의의 숫자 생성
    if num not in result:  # 중복 숫자 뽑기 방지
        result.append(num)

print(result)  # 무작위 생성된 6개의 숫자 출력