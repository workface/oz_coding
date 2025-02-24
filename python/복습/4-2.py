# 사용자 입출력

# input 사용하기
a = input()
print(a)

#input은 사용자가 키보드로 입력한 모든 것을 문자열로 저장한다.

number = input("숫자를 입력하세요: ")
print (number)

#괄호 안에 입력한 문구가 프롬프트로 나타난다.
#‘숫자를 입력하세요’라는 프롬프트에 3을 입력하면 변수 number에 값 3이 대입된다
type(number)
#input은 입력되는 모든 것을 문자열로 취급하기 때문에 number는 숫자가 아닌 문자열이라는 것에 주의하자.

#print 자세히 알기
a = 123
print(a) #숫자 출력하기

a = "Python"
print(a)   #문자 출력하기

a = [1, 2, 3]
print(a)    # 리스트 출력하기


# print("life" "is" "too short")  # 1번
# >>>lifeistoo short
# print("life"+"is"+"too short")  # 2번
# >>>lifeistoo short

#같은 값이 나오는데 따옴표로 둘러싸인 문자열을 연속으로 쓰면 +연산을 한 것과 같다.

# print("life", "is", "too short")
# >>>life is too short

# 쉼표를 사용하면 문자열을 띄어줄 수 있다.

for i in range(10):
    print(i, end = " ")
# 기본적으로 print() 함수는 출력 후 자동으로 줄바꿈을 추가하는데, 이 줄바꿈 문자를 제어할 수 있게 해주는 것이 바로 end입니다.
# end의 초깃값은 줄바꿈 문자 \n입니다.
