# #while

# treeHit = 0
# while treeHit < 10 :
#     treeHit = treeHit + 1
#     print('나무를 %d번 찍었습니다' % treeHit)
#     if treeHit == 10 :
#         print('나무가 넘어갑니다.')


# prompt = '''
#     1. Add
#     2. Del
#     3. List
#     4. Quit
#     Enter number:'''

# number = 0
# while number != 4 :
#     print(prompt)
#     number = int(input())



# whlie 문은 반복 실행되는데, break를 만나면 멈춘다.
# coffee = 10
# money = 300

# while money :
#     print('돈을 받았으니 커피를 줍니다')
#     coffee -= 1
#     print('남은 커피의 양은 %d입니다' %coffee)
#     if coffee == 0 :
#         print('커피가 다 떨아쟜습니다. 종료합니다.')
#         break


# coffee = 10

# while True :
#     money = int(input('돈을 넣어 주세요'))
#     if money == 300 :
#         print('커피를 줍니다')
#         coffee -= 1
#         print('남은 커피의 양은 %d개 입니다.' % coffee)
#     elif money > 300 :
#         print('커피를 주고 거스름돈 %d를 돌려 줍니다.' % (money - 300))
#         coffee -= 1
#         print('남은 커피의 양은 %d개 입니다.' % coffee)
#     else :
#         print('돈을 돌려줍니다. 커피는 주지 않습니다.')
#         print('남은 커피의 양은 %d개 입니다.' % coffee)
#     if coffee == 0 :
#         print('커피가 다 떨어졌습니다. 판매를 중지합니다.')
#         break

# while문은 continue를 만나면 다시 처음으로 돌아간다.

# a = 0
# while a < 10 :
#     a += 1
#     if a % 2 == 0 :
#         continue
#     print(a)

#1분코딩 문제 : 1부터 10까지의 숫자 중 3의 배수를 제외한 나머지 숫자가 출력되게 하여라
# a = 0
# while a < 10 :
#     a += 1
#     if a % 3 == 0 :
#         continue
#     print(a)
