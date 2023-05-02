def f01():
    print('f01 함수입니다.')
print(f01, type(f01))

class c01:
    firstname = 'hello'
    
print(c01, type(c01))

c01.lastname = 'kim'
obj = [f01, c01]

print(obj, type(obj))
print(type(list), type(tuple), type(dict), type(set))
print(type(int), type(str), type(tuple), type(bool))
obj[0]()
print(obj[1]().firstname, obj[1]().lastname, obj[1]().lastname)





