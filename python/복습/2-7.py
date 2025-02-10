# 불 자료형


a = True #맨 앞은 대문자
b = False #맨 앞은 대문자

print(type(a))
#<class 'bool'>
print(type(b))
#<class 'bool'>

print(1 == 1)

print(2 > 1)

print(2 < 1)

# 값	참 or 거짓
# "python"	참
# ""	거짓
# [1, 2, 3]	참
# []	거짓
# (1, 2, 3)	참
# ()	거짓
# {'a': 1}	참
# {}	거짓
# 1	참
# 0	거짓
# None	거짓

a = [1, 2, 3, 4]
while a:   # a가 참인 동안  
    print(a.pop()) #리스트의 마지막 요소를 하나씩 꺼낸다.

# while 조건문:
#     수행할_문장

# a가 참인 경우, a.pop()를 계속 실행하여 출력하라는 의미이다. a.pop() 함수는 리스트 a의 마지막 요소를 끄집어 내는 함수이므로 리스트 안에 요소가 존재하는 한(a가 참인 동안) 마지막 요소를 계속 끄집어 낼 것이다. 
# 결국 더 이상 끄집어 낼 것이 없으면 a가 빈 리스트([])가 되어 거짓이 된다. 따라서 while 문에서 조건문이 거짓이 되므로 while 문을 빠져나가게 된다. 이는 파이썬 프로그래밍에서 매우 자주 사용하는 기법 중 하나이다.


if []:
    print("참")
else:
    print("거짓")


if [1, 2, 3]:
    print("참")
else:
    print("거짓")


print(bool('python'))
# True
print(bool(''))
# False

