# Python 변수 - 자료형의 값을 저장하는 공간, 변수
a = 10
print(a, type(a))  

a = 'hello' # 변수의 값 재할당 -> 자료형 str로 변경
print(a, type(a))  

# 리스트를 복사하고자 할 때
arrayTest = [1,2,3]
b = arrayTest[:]
arrayTest[0] = 999
print(arrayTest)

p , l = ('python', 'life')
print(p+l)

(p, l) = 'python', 'life'
print(p, l)

[p,l] = ['python', 'life']
print(p, l)

p = l = 'python'
print(l)

p = 10
l= 5
p, l = l, p

print(p, l)
*p , l, t = 10, 20, 30, 40, 50 ,60, 70, 80, 90, 100
print(p,l,t)

############################################################################################################
############################################################################################################

# 조건문 
test01 = 10
test02 = 'test'
if test01 == test02:
    print("type이 같습니다.")
else:
    print('type이 같지 않습니다.')
    
# 다양한 조건을 판단하는 elif
pocket = ['paper,' 'handphone']
card = True
if 'money' in pocket:
    print('택시 가능')
else:
    if card:
        print('택시 가능')
    else: 
        print("택시 불가")
        
############################################################################################################
############################################################################################################

# while 문
# treeHit = 0
# while treeHit < 10:
#     treeHit = treeHit + 1
#     print('나무를 %d번 찍었습니다.' % treeHit)
#     if treeHit == 10:
#         print('10번 찍어도 안넘어감')

# break 
# coffee = 10 # 커피 재고
# money = 300 # 현재 money 값
# while money:
#     coffee = coffee -1
#     print('돈 받음 커피 재고 -1', coffee)

#     print("남은 커피의 양은 %d개 " % coffee)
#     if coffee == 0:
#         print('커피 재고 0')
#         break 
    
############################################################################################################

# for문
for i in ['a', 'b', 'c', 'd', 'e']:
    print(i, end=' ')
    
a = range(1, 10)    
print(a, type(a))

#############################################
a = ['a', 'b', 'c', 'd', 'e']
for i in range(len(a)):
    print(i , a[i])
##############################################

for i, v in enumerate(a):
    print(i, v)


# 1부터 10까지의 짝수, 홀수 합.
add = 0
for i in range(1, 11, 2): # 홀수 반복
    add += i # 홀수들의 합
    print(i, end=' ')
    print('홀수들의 합 = ' , add)
    
#######################################################

add = 0
for i in range(1,11):
    add += i
    
print(i, end=' ')
print('짝수들의 합 = ', add )

#######################################################
a = [1,2,3,4]
result = []
for num in a:
    result.append(num * 3)
print(result)

result2 = [num * 3  for num in a if num % 2 == 0] # 리스트 내포 방식
print(result2)

