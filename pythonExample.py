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
    
    
# 1-1 강사님의 답안 list

lotto = []

while len(lotto) < 7:
    num = random.randint(1, 45)
    if num not in lotto:
        lotto.append(num)
    lotto_1 = sorted(lotto[:6])
    lotto_2 = lotto[-1]
    
    print(lotto_1, "2등 보너스 번호는 :", lotto_2 )

# 1-2 강사님의 답안 set
lotto2 = set()
while len(lotto2) < 7:
    n = random.randint(1, 45)
    lotto2.add(n)
lotto2list = list(lotto2)

lotto_1 = sorted(lotto2list[:6])
lotto_2 = lotto2list[-1]

print(lotto_1, "2등 보너스 번호는 :", lotto_2 )

# 1-3 강사님의 답안 shuffle

lotto3 = list(range(1, 46))
random.shuffle(lotto3)
lotto_1 = sorted(lotto3[:6])
lotto_2 = lotto3[-1]

print(lotto_1, "2등 보너스 번호는 :", lotto_2 )

# 2. 가위 바위 보 게임 - 내가 한 풀이

RPS = ['가위', '바위', '보']
result = {0:'졌습니다.', 1:'비겼습니다.', 2: '이겼습니다.'}

computer = random.choice(RPS)
user = input('가위, 바위, 보 중 하나를 입력해주세요.')

print(f'사용자 ( {user} vs {computer} ) 컴퓨터')

if user == computer:
        state = 1
elif user == '가위' and computer == '보':
        state = 2
elif user == '바위' and computer == '가위':
        state = 2
elif user == '보' and computer == '바위':
        state = 2
else:
        state = 0
        
print(result[state])
###############################################################

# 2-1 가위 바위 보 게임 - 강사님의 답안

game = {0:'가위', 1:'바위', 2:'보'}
human = int(input('가위(0), 바위(1), 보(2) 중 하나를 입력해주세요.'))
com = random.randint(0,2)
result = human - com

print('human : ', game.get(human))
print('com : ', game.get(com))

'''
간격이 1일때는 큰 쪽이 승리
간력이 2일때는 작은 쪽이 승리
같으면 무승부
'''
# if human == com:
#     print("무승부 입니다.")
# elif human - com == 1 or human - com == -2:
#     print("이겼습니다.")
# else: 
#     print('졌습니다.')
    
if result == 0:
    print("무승부 입니다.")
elif result in [1, -2]:
    print("이겼습니다.")
else:
    print('졌습니다.')
    
# 2-2 가위 바위 보 게임 - 강사님의 답안

game = {0:'가위', 1:'바위', 2:'보'}
human = int(input('가위(0), 바위(1), 보(2) 중 하나를 입력해주세요.'))
com = random.randint(0,2)
result = [
    ['비김', '컴퓨터 승', '사람 승'],
    ['사람 승','비김', '컴퓨터 승'],
    ['컴승','사람 승', '비김']
]

print(f'사용자 ( {human} vs {com} ) 컴퓨터')
print(result[human][com])

# print('human : ', game.get(human))
# print('com : ', game.get(com))






















    
    
    