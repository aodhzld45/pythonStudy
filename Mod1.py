###########################
# Python Module 연습
def add(a,b):
    return a+b

def min(a,b):
    return a-b

def mulp(a,b):
    return a*b

print('Mod1의 __name__의 값 : ', __name__) #시작점

if __name__ == '__main__': # 함수 시작점. 자체적으로 실행하면 참이되지만 다른곳에서 import하여 사용시 false가 됨
    # __name__ 변수는 해당 모듈이 import 되었을 때는 모듈의 이름을 가지고 / 직접 실행되었을 때는 __main__의 이름을 가진다.
    print('mod1.py')
    print(add(1, 4))
    print(min(4, 2))