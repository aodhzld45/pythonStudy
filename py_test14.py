
### Python의 예외처리
try: 
    f = open('aaaa.txt', 'r')
    a =[1,2]
    4/0
    print(a[3])

except ZeroDivisionError as e:
    print('0으로 나눌 수 없습니다.')
    print(e)
except IndexError as e:
    print('인덱싱 할 수 없습니다.')
    print(e)
except:
    print('기타 오류')
    
### 오류 일부러 발생 시키기 - 다형성 및 메서드 오버라이딩

# 다형성이란
# 1. 같은 모양의 코드가 다른 동작을 하는것.
# 2. 코드의 양을 줄이고, 여러 객체 타입을 하나의 타입으로 관리가 가능하여 유지 보수에 좋다.
# 3. 메서드 오버라이딩도 다형성의 예이다.

class Bird: # 부모 클래스
    def fly(self): # 부모 메서드 - 강제로 오류를 발생시킴
        raise NotImplementedError
    
class Eagle(Bird): # 자식 클래스
    # 메서드명을 동일하게 해서 같은 모양의 코드가 다른 동작을 하도록 하는 다형성 예 - 오버라이딩

    # #메서드 오버라이딩# 부모로 부터 물려받은 메서드(힘수)를 자식 클래스에서 재정의 하는것
    # 
    def fly(self): 
        print(' 재정의 된 메서드 fly - Eagle fly', type(Eagle), Eagle)
class Owl(Bird):
    def fly(self): 
        print(' 재정의 된 메서드 fly - Owl fly', type(Owl), Owl)
class Dove(Bird):
    def fly(self): 
        print(' 재정의 된 메서드 fly - Dove fly', type(Dove), Dove)
    

eagle = Eagle()
owl = Owl()
dove = Dove()

eagle.fly()
owl.fly()
dove.fly()

bird_child = [eagle, owl, dove] # 같은 이름의 메서드를 사용하기 때문에 반복이 가능.
for bird in bird_child:
    print('같은 이름의 메서드를 사용한 다형성 - 오버라이딩', bird.fly)
    
# 다형성 예제 2
# 클래스 명만 다르고 안에 있는 내용(메서드)이 같음 -> 관리가 매우 용이함.
class Paladin:
    def __init__(self, name) -> None:
        self.name = name
    
    def select(self):
        ('전문화 선택')

class Divinity:
    def __init__(self, name) -> None:
        self.name = name
    def select(self):
        print('신성')
        
class Punishment:
    def __init__(self, name) -> None:
        self.name = name
    def select(self):
        print('징벌')
        
class protect:
    def __init__(self, name) -> None:
        self.name = name
    def select(self):
        print('보호')  

paladin = Paladin('tttt')
divinity = Divinity('tttt')
ourteam = [paladin, divinity]
for user in ourteam:
   user.select()
   

### 에외 만들기
class myError(Exception):
    pass
def say_nick(nick):
    if nick == '바보':
        raise myError()
    print(nick)

try:
    say_nick('천사')
    say_nick('바보')

except myError:
    print('허용 되지 않는 별명입니다.')

        
    
