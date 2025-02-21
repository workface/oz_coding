money = True
if money :
    print("택시를 타고 가라")
else :
    print("걸어가라")

money = False
if money :
    print("택시를 타고 가라")
else :
    print("걸어가라")


#파이썬은 들여쓰기(indentation)을 해야하한다. 굉장히 중요하다.

x = 3
y = 2
print(x < y)

x = 3
y = 2
print(x != y)

#비교 연산자 종류는 <, >, ==, !=, >=, <= 가 있다. (!= 는 같지않다 라는 뜻이다.)
money = 2000
if money >= 3000 :
    print('택시를 타고 가라')
else :
    print('걸어가라')

money = 2000
card = True

# and, or, not가 있는데. 각 의미는 or는 둘중 하나만 참이면 참이고, and는 둘다 참이여야 참이다. not는 거짓일때 참이된다.
if money >= 3000 or card :
    print('택시를 타고 가라')
else :
    print('걸어가라')

money = 2000
card = True

if money >= 3000 or not card :
    print('택시를 타고 가라')
else :
    print('걸어가라')

#in, not in in은 리스트나 튜플, 문자열에 들어있을때 참이되고 not in 들어있지 않을때 참이 된다. in의 영어뜻 ~안에 를 생각하면 쉽다.
print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])

print('a' in ('a', 'f', 'w', 'q'))
print('a' not in ('a', 'f', 'w', 'q'))
print('a' in 'python')


# elif

pocket = ['paper', 'cellphone']
card = True

if 'money' in pocket :
    print('택시를 타고 가라')
else :
    if card :
        print('택시를 타고 가라')
    else :
        print('걸어가라')

pocket = ['paper', 'cellphone']
card = True

if 'money' in pocket :
    print('택시를 타고 가라')
elif card :
    print('택시를 타고 가라')
else :
    print('걸어가라')

