#### Python Class

class FourCal:
        def setdata(self, first:int, second:int) -> int: # -> None의 의미는 return이 없다는 의미. 
            self.first = int(input('첫번째 숫자를 입력하세요 = ')) # 다른 언어에서의 this -> 객체 자기 자신을 가르킴
            self.second = int(input('두번째 숫자를 입력하세요 = ')) # first, second는 인스턴스(instance)안에 존재하는 인스턴스 멤버 변수
            #인스턴스 변수에 접근하기 위한 self.변수로 사용 (this와 같은 의미.)
            
        def add(self):
            result = print('두 숫자의 합 =' , self.first + self.second)
            return result
        
        def EvenAdd(self):
            input_num = int(input('숫자를 입력해주세요.'))
            print(type(input_num))
            even_sum = 0

            for num in range(1, input_num+1): 
                if int(num) % 2 == 0:
                    even_sum += int(num)
            print("짝수의 합: ", even_sum)

            return even_sum
    
a = FourCal()
# a.setdata(10,20)
# print(a.first, a.second, type(a))
# print(a.add())
#print('return된 EvenAdd의 값 = ' , a.EvenAdd())

########################
'''
python의 생성자와 소멸자 
'''
########################

class ConCal:
    #추가된 생성자 __init__ 메서드 생성자 
    def __init__(self, first, second) -> None:
         self.first = first
         self.second = second    
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def setmin(self) :
        result = self.first - self.second
        return result
    def setmul(self) :
        result = self.first * self.second
        return result
    def setdiv(self) :
        result = self.first / self.second
        return result

######## 파이썬 클래스의 상속 ########
# 기본 구조
class MoreFourCal(ConCal):
    def pow(self):
        result = self.first ** self.second # 두 수의 거듭제곱
        return result

a = MoreFourCal(4,2)
print(type(a))
print(a.first)
print(a.second)

####### 클래스 변수 ########
class Family:
    lastname = 'kim'# 클래스 변수 선언
    def plus(self, a, b):
        print('plus 함수 값 : ', a+b)

a = Family() # Family 인스턴스 생성
b = Family() # Family 인스턴스 생성

# Family.lastname = 'lee' # 클래스 변수 재할당.
a.lastname = 'park' # 인스턴스 변수 할당
b.lastname = 'hong' 

a.plus(10, 20)

print('Family.lastname = ', Family.lastname)
print('a.lastname = ', a.lastname)
print('b.lastname = ', b.lastname)

### 클래스 변수와 인스턴스 변수
# 클래스 변수 - 모든 인스턴스 사이에 공유된 값을 가진 변수
print('Family Class 변수의 id값 =',  id(Family.lastname))

# 인스턴스 변수 - 각각의 인스턴스 마다 독립한 변수
print('a = Family()의 인스턴스 변수 a의 id 값 = ', id(a.lastname) )
print('b = Family()의 인스턴스 변수 b의 id 값 = ', id(b.lastname) )


