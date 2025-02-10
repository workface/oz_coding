# 자료형의 값을 저장하는 공간, 변수

#변수

a = 1
b = "python"
c = [1, 2, 3]

#변수_이름 = 변수에_저장할_값

a = [1, 2, 3]
print(id(a))

a = [1, 2, 3]
b = a
print(b)
print(id(a))
print(id(b))

print(a is b)

a = [1, 2, 3]
b = a
a[1] = 4
print(a)
print(b)

a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a)
print(b)

a = [1, 2, 3]
b = a[0]
a[0] = 4
print(a)
print(b)

#변수를 만드는 여러가지 방법

a = 'life'
b = 'pyrhon'
print(a)
print(b)
print(type(a))
(a, b) = 'life', 'python'
print(a)
print(b)
print(type(a))
a, b = 'life', 'python'
print(a)
print(b)
print(type(a))
(a, b) = ('life', 'python')
print(a)
print(b)
print(type(a))
# 전부 같다.. 튜플..

a = 'python'
b = 'python'
print(a)
print(b)
a = b = 'python'
print(a)
print(b)

# 값 바꾸기

a = 3
b = 5

a,b = b,a
print(a)
print(b)