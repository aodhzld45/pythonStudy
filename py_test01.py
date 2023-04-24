#참고 사이트 https://wikidocs.net/13

print('hello')
numArr = [1,2,3,4,5]

print(numArr)

print(sum(numArr))

bin8 = 0o177
bin16 = 0xABC

print(bin8, bin16)

pow = bin8 ** 2 # **시 제곱
print(pow)

SingleTest = "테스트 01 '작은 따옴표' 출력하기 " 
DoubleTest = '테스트 02 "큰 따옴표" 출력하기'

say = "\\'python's farvorite food is perl\\' test입니다." # \를 오른쪽에 사용시 특수문자의 특징을 삭제.

text01 = 'Life is too short \n You need Python'
text02 = """ 
         \n이 아닌 \"""을 이용한
         줄바꿈 테스트입니다. 
         """


print(say)
print(text01)
print(text02)
print(SingleTest)
print(DoubleTest)