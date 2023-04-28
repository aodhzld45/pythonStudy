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
print('return된 EvenAdd의 값 = ' , a.EvenAdd())

########################
'''
python의 생성자와 소멸자 
'''
########################

class ConCal:
    def __init__(self, first, second) -> None:
         self.first = first
         self.second = second         
    
         
         




         
         
         
         
         
         
         
         

            
