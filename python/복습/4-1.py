#함수의 기본 구조
# def 함수_이름(매개변수):
#     수행할 문장1
#     수행할 문장2


def add(a, b):
    return a + b 

print(add(1, 2))


def add(a, b): # a, b는 매개변수
    return a + b

print(add(3, 4)) #3, 4 는 인수    

#일반적인 함수
# def 함수_이름(매개변수):
#     수행할 문장
#     return

def add(a, b):
    result = a + b
    return result
a= add(3, 4)
print(a)

#입력값이 없는 함수
def say():
    return 'Hi'

a = say()
print(a)

# Hi가 출력된다. 입력값은 없지만, 리턴값으로 Hi라는 문자열을 리턴한다. 즉 a = say()처럼 작성하면 a에 Hi라는 문자열이 a에 대입되는 것이다.

#리턴값이 없는 함수
def add(a ,b) :
    print('%d, %d의 합은 %d 입니다.' %(a, b, a+b))

a = add(3, 4)
print(a)

#3, 4의 합은 7입니다 라는 문장이 출력 되었지만 이는 프린트 문의 함수의 구성요소 증 하나인 수행할 문장에 해달하는 것일뿐 리턴값은 없다.
#리턴값은 오직 return 명령으로만 돌려 받을 수 있디.

#입력값도, 리턴값도 없는 함수

def say():
    print('Hi')
a = say()
print(a)



#매개변수를 지정하여 호출하기
def sub(a, b ):
    return a - b
result = sub(b=3, a=7)
print(result)

#sub(3, 7)을 입력하면 -4가 나왔겠지만 a와 b를 지정하여 값을 넣으주면 자리가 바뀌어도 7-3이 되에 4가 출력된다.

#입력값이 몇 개가 될지 모를 때

#def 함수이름(*매개변수):
#    수행할문장

#여러개의 입력값을 받는 함수 만들기
def add_many(*args):
    result = 0
    for i in args :
        result += i
    return result
print(add_many(1, 2, 3, 4, 5, 6))

def add_mul(choice, *args): 
    if choice == "add":   # 매개변수 choice에 "add"를 입력받았을 때
        result = 0 
        for i in args: 
            result = result + i 
    elif choice == "mul":   # 매개변수 choice에 "mul"을 입력받았을 때
        result = 1 
        for i in args: 
            result = result * i 
    return result

results = add_mul('add', 1, 2, 3, 4, 5)
result = add_mul('mul', 1, 2, 3, 4, 5)
print(results)
print(result)


#카워드 매개변수
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=1, b=2)

# 함수의 리턴값은 언제나 하나 이다.
def add_mul(a, b) :
    return a+b, a*b
print(add_mul(3, 4))

def add_mul(a, b) :
    return a+b
    return a*b
print(add_mul(3, 4))

# 함수에서 리턴을 만나면 함수가 종료 되버린다 따라서 return a+b를 만나 종료가 되버려 return a*b는 거치치 못한다.리턴값은 하나이다.
def say_nick(nick): 
    if nick == "바보": 
        return 
    print("나의 별명은 %s 입니다." % nick)

say_nick('바보')
say_nick('멍청이')
# 입력값으로 바보라는 값이 들어오면 문자열을 출력하지 않고 함수를 즉시 빠져나간다. 그러므로 출력되지 않는디.
# 이처럼 리턴값이 없는 함수에서 return으로 함수를 빠져나가는 방법은 실제 프로그래밍에서 자주 사용한다.

#매개변수에 초깃값 미리 설정하기

def say_myself(name, age, man=True): 
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % age) 
    if man: 
        print("남자입니다.")
    else: 
        print("여자입니다.")

say_myself('랄랄', 20, False)

#‘초깃값이 없는 매개변수(age)는 초깃값이 있는 매개변수(man) 뒤에 사용할 수 없다’라는 뜻이다. 
# 즉, 매개변수로 (name, age, man=True)는 되지만, (name, man=True, age)는 안 된다는 것이다. 
# 초기화하고 싶은 매개변수는 항상 뒤쪽에 놓아야 한다는 것을 잊지 말자.

# 함수 안에서 선언한 변수의 효력 범위
a = 1               #전역변수
def vartest(a):
    a = a +1        #지역변수

vartest(a)
print(a)
#vartest 함수에서 매개변수 a의 값에 1을 더했으므로 2가 출력될 것 같지만, 프로그램 소스를 작성해서 실행해 보면 결괏값은 1이 나온다. 
# 그 이유는 함수 안에서 사용하는 매개변수는 함수 안에서만 사용하는 ‘함수만의 변수’이기 때문이다. 
# 즉, def vartest(a)에서 입력값을 전달받는 매개변수 a는 함수 안에서만 사용하는 변수일 뿐, 함수 밖의 변수 a와는 전혀 상관없다는 뜻이다.

def vartest(a):
    a = a + 1

vartest(3)
print(a)

# print(a) 문장은 오류가 발생하게 된다. 그 이유는 print(a)에서 사용한 a 변수는 어디에도 선언되지 않았기 때문이다

#return 사용하기
a = 1 
def vartest(a): 
    a = a +1 
    return a

a = vartest(a) 
print(a)
#첫 번째 방법은 return을 사용하는 방법이다. 
# vartest 함수는 입력으로 들어온 값에 1을 더한 값을 리턴하도록 변경했다. 
# 따라서 a = vartest(a)라고 작성하면 a에는 vartest 함수의 리턴값이 대입된다.

#global 사용하기
a = 1 
def vartest(): 
    global a 
    a = a+1

vartest() 
print(a)
#global a 문장은 함수 안에서 함수 밖의 a 변수를 직접 사용하겠다는 뜻이다. 
# 하지만 프로그래밍을 할 때 global 명령어는 사용하지 않는 것이 좋다.
# 함수는 독립적으로 존재하는 것이 좋기 때문이다.


#lambda 예약어
a = [1, 2, 3] 
def vartest(a): 
    a = a.append(4) 
    return a

a = vartest(a) 
print(a)
# None이 나오는데 이유는 append는 리턴값이 없어서 리턴을 할 수 없다. 
# 아래 리턴을 적어도 a에는 아무것도 담기지 않고 전역변수에만 apppend되어 담긴다.

a = [1, 2, 3] 
def vartest(a): 
    a = a.pop() 
    return a

a = vartest(a) 
print(a)

# append 대신 pop을 사용하면 pop으로 튕겨저 나온 값이 a에 담겨 리턴되어 [3]출력된다.
# pop 에는 return이 존재 한다.

a = [1, 2, 3] 
def vartest(a): 
    a = a.append(4) 
    
vartest(a) 
print(a)

# [1, 2, 3, 4]가 출력되는데 append로 인해 전역변수에 4를 추가한 값으로 변하여 출력되어 그렇다.

a = [1, 2, 3] 
def vartest(a): 
    a = a.pop() 
    
vartest(a) 
print(a)

# [1, 2]이 출력된다. pop으로 3이 튕겨져 나가 전역변수인 a가 변하여 출력된다.

a = [1, 2, 3] 
def vartest(a): 
    a.append(4) 
    return a 
    
a = vartest(a) 
print(a)