# 딕셔너리 기본 구조 - {key1: Value1, key2: Value2, key3: Value3} 순서를 보장하지 않음.
# 리스트랑 호환성이 좋음.
lst1 = ['a', 'b', 'c']
dic1 = {0: 'apple', 1:'banana', 2:'carrot'}

print(lst1, type(lst1), lst1[0]) # -> 리스트는 번지로 접근
print(dic1, type(dic1), dic1[0]) # -> 딕셔너리는 번지가 아니고 key로 접근. / dic1[0] 0번째 키값을 리턴함.
print(dic1.keys(), type(dic1.keys())) #딕셔너리를 리스트로 변환.

# for lst in lst1:
#     print(lst)
    
for dic in dic1:
    print(dic)

print('++++++++++++++++++++++++++++++++++++++++++++')

lst2 = list(dic1.keys())
print(lst2, type(lst2))

# 딕셔너리의 value값 뽑아내기
for dic in dic1.values():
    print(dic)
    
# 딕셔너리의 key, value값 뽑아내기
for items in dic1.items():
    print(items)
    
# 딕셔너리의 key : value값 번지로 접근하여 반복하기
for k, v in dic1.items():
    print(k, v)
    
# 딕셔너리의 key로 value값 얻기 (get)
dic2 = {'kim':10, 'lee':20, 'seo':30 }

lst3 = ['kim', 'kim', 'park', 'lee', 'kim', 'choi', 'hong', 'lee', 'kang', 'jang', 'jang', 'kim']


for name in lst3:
    dic2[name] = dic2.get(name,0) + 1 
    print(dic2)
    
print('#################################################################')

count = lst3.count('kim')
print(count)

    
    
    

# 프로그래머스 최빈값 구하기 예제
# collections 라이브러리 
from collections import Counter

array = [1, 2, 3, 3, 3, 4]

def solution(array):
    count = list(dict(Counter(array)).items())
    count.sort(key=lambda x : x[1], reverse=True) # 람다식(예약어) 익명함수 :을 기준으로 왼쪽은 매개변수 / # x[1]
    if len(count) >= 2 and count[0][1] == count[1][1]:
        return -1
    return count[0][0]

# Counter 함수를 사용하여 리스트(array)의 각 요소의 등장 횟수를 계산합니다.
# 등장 횟수를 튜플의 형태로 바꾸고, 리스트(count)에 저장합니다.
# 리스트(count)를 등장 횟수가 많은 순서로 정렬합니다.
# 가장 많이 등장한 요소가 2개 이상이고, 그 등장 횟수가 같은 경우 -1을 반환합니다.
# 그렇지 않은 경우, 가장 많이 등장한 요소의 값(count[0][0])을 반환합니다.

    




