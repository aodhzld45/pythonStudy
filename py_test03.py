#문자열 포맷
name = 'seo'
str1 = 'my name is %s' % name
print(str1)

age = 20
str2 = 'My name is %s, I age %d' %(name, age)
print(str2)

str3 = '%10s' % 'hi'
print(str3)

str4 = '%-10s' % 'hello' # -를 붙이면 반대정렬 -> 오른쪽칸 10칸 확보
print(str4)

str5 = '%10.10f' % 3.1425925431231547423423523 # 소숫점 10자리 반환.
print(str5)

ver = 3.8
str6 = f'3.6 버전 이상부터 사용이 가능한 f문자열 포매팅 입니다. {ver - 0.3 }버전은 사용이 불가하다.'
print(str6)


 
