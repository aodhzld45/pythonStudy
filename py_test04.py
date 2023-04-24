# 문자열 관련 함수들

# 01. 문자열 개수 세기 Count
c = 'hobby'
test01 = c.count('b')
print(test01)

# 03. 문자열 삽입 join
name = '서현석'
age = 20
test03 = f'이름은 {name}이고, 나이는 {age}세 이다'
print(test03)
print(','.join('abcde'))
print('a','b','c','d','e', sep='-') # sep의 기본값은 공백 하나
print('a','b','c','d','e', sep=' ')

# replace을 사용한 예제 프로그래머스 옹알이

# babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
# 첫번째 케이스
def solution(babbling):
    print(babbling)

    answer = 0
    for msg in babbling: # 중괄호가 없다.
        msg = msg.replace('aya', '@', 1) #임의의 특수문자로 치환.
        msg = msg.replace('ye', '@', 1)
        msg = msg.replace('woo', '@', 1)
        msg = msg.replace('ma', '@', 1)
        msg = msg.replace('@', '')
        if(len(msg) == 0):
            answer += 1
            print(answer)

    return answer

# 두번째 케이스
def solution(babbling):
    count = 0
    babble = [ "aya", "ye", "woo", "ma" ]
    for a in babbling:
        for b in babble:
            if b * 2 not in a:
                a = a.replace(b, ' ')
        if a.strip()== '':
            count += 1
    return count









 