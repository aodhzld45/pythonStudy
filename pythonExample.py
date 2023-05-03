import random

# 1. 로또번호 생성기 만들기 - 나의 풀이(중복 제거 실패)
lotto = []

while len(lotto) < 6:
    num = random.randrange(1, 45)
    num2  = random.randrange(1, 45)

    if num and num2 not in lotto:

        lotto.append(num)
    
    lotto_1 = sorted(lotto[:5])
    
    print(lotto_1, "###2등 보너스 번호는 :", num2)
    
    
# 1-1 강사님의 답안 -1 list

lotto = []

while len(lotto) < 7:
    num = random.randint(1, 45)
    if num not in lotto:
        lotto.append(num)
    lotto_1 = sorted(lotto[:6])
    lotto_2 = lotto[-1]
    
    print(lotto_1, "2등 보너스 번호는 :", lotto_2 )

# 1-2 강사님의 답안 -2 set
lotto2 = set()
while len(lotto2) < 7:
    n = random.randint(1, 45)
    lotto2.add(n)
lotto2list = list(lotto2)

lotto_1 = sorted(lotto2list[:6])
lotto_2 = lotto2list[-1]

print(lotto_1, "2등 보너스 번호는 :", lotto_2 )

# 1-3 강사님의 답안 -3 shuffle

lotto3 = list(range(1, 46))
random.shuffle(lotto3)
lotto_1 = sorted(lotto3[:6])
lotto_2 = lotto3[-1]

print(lotto_1, "2등 보너스 번호는 :", lotto_2 )

              
              





    
    
        

    
    


        
    

# 2. 가위 바위 보 게임
# RPS = ['가위', '바위', '보']
# result = {0:'졌습니다.', 1:'비겼습니다.', 2: '이겼습니다.'}

# computer = random.choice(RPS)
# user = input('가위, 바위, 보 중 하나를 입력해주세요.')

# print(f'사용자 ( {user} vs {computer} ) 컴퓨터')

# if user == computer:
#         state = 1
# elif user == '가위' and computer == '바위':
#         state = 2
# elif user == '바위' and computer == '보':
#         state = 2
# elif user == '보' and computer == '가위':
#         state = 2
# else:
#         state = 1
        
# print(result[state])
















    
    
    