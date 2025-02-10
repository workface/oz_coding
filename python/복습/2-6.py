# 집합 자료형

# s1 = set([1, 2, 3])
# s1
# {1, 2, 3}
# 위와 같이 set()의 괄호 안에 리스트를 입력하여 만들거나 다음과 같이 문자열을 입력하여 만들 수도 있다.

# s2 = set("Hello")
# s2
# {'e', 'H', 'l', 'o'}
# 비어 있는 집합 자료형은 s = set()로 만들 수 있다.

# 집합자료의 특징
#중복을 허용하지 않는다.
#순서가 없다(Unordered).
#집합 자료형은 인덱싱 할 수 없다. 인덱싱 하려면 리스트자료형이나, 튜플로 변환하여 인덱싱해야 한다.

# s1 = set([1, 2, 3])
# l1 = list(s1)
# l1
# [1, 2, 3]
# l1[0]
# 1
# t1 = tuple(s1)
# t1
# (1, 2, 3)
# t1[0]
# 1

#교집합, 합집합, 차집합 구하기

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

#교집합
print(s1 & s2)
print(s1.intersection(s2))
#합집합
print(s1 | s2)
print(s1.union(s2))
#차집합
print(s1 - s2)
print(s1.difference(s2))
print(s2 - s1)
print(s2.difference(s1))
#값 1개 추가하기
s1 = set([1, 2, 3])
s1.add(4)
print(s1)
#값 여러개 추가하기
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)

#특정 값 제거하기
s1 = set([1, 2, 3])
s1.remove(2)
print(s1)

