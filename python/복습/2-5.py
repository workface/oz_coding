#딕셔너리 자료형

# dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
# print(type(dic))
#딕트는 중괄호를 쓴다. key, value 형식으로 만든다.

# a = {1: 'hi'}
# print(a)

#value에 리스트 형식으로 넣을수 있다.
# a = {'a': [1, 2, 3]}
# print(a)

#딕셔너리 쌍 추가, 삭제하기
a = {1: 'a'}
a[2] = 'b'
# print(a)

a['name'] = 'pey'
# print(a)

#리스트 값을 가지는 딕셔너리 추가
a[3] = [1, 2, 3]
# print(a)

#삭제

# del a[1] # 키값이 1인 딕셔너리 삭제
# print(a)

#딕셔너리에서 Key를 사용해 Value 얻기
# grade = {'pey': 10, 'julliet': 99}
# print(grade['pey'])

# a = {'a': 1, 'b': 2}
# print(a['a'])

# print(a['b'])

# print(a['c'])  <<< key error 없는 값을 입력하면 키에러가 난다.

# 주의 사항 : key는 고유한 값이므로 중복되는 값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시된다는 점에 주의해야 한다.

# a = {1:'a', 1:'b'}
# print(a)

# =>{1:'a'}가 무시 된다.

# a = {[1, 2] : 'hi'}
# print(a)
#key에 리스트가 들어가 변형이가능하므로 TypeError가 나온다, 변형이 가능한건 쓸 수 없다.

# a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
# print(a.keys())
#keys = key들만 모아 리스트형태로 dict_keys객체를 리턴한다.

# a.values()
#key를 얻는것과 마찬가지 방법으로 value만 얻고 싶다면 values 함수를 사용하면 된다. values 함수를 호출하면 dict_values 객체를 리턴한다.

# a.items()
#items 함수는 Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 리턴한다.

# a.clear()
#clear 함수는 딕셔너리 안의 모든 요소를 삭제한다

# a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
# a.get('name')
# 'pey'
# a.get('phone')
# '010-9999-1234'
# get(x) 함수는 x라는 Key에 대응되는 Value를 리턴한다. 앞에서 살펴보았듯이 a.get('name')은 a['name']을 사용했을 때와 동일한 결괏값을 리턴한다.

# a = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
# print(a.get('nokey'))
# None
# print(a['nokey’])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'nokey'
# a['nokey']처럼 딕셔너리에 존재하지 않는 키로 값을 가져오려고 할 경우, a['nokey'] 방식은 오류를 발생시키고 a.get('nokey') 방식은 None을 리턴한다는 차이가 있다

# a.get('nokey', 'foo')
#'foo'
# 딕셔너리 a에는 'nokey'에 해당하는 Key가 없다. 따라서 디폴트 값인 'foo'를 리턴한다.

# a = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
# 'name' in a
# True
# 'email' in a
# False
# 'name' 문자열은 a 딕셔너리의 Key 중 하나이다. 따라서 'name' in a를 호출하면 참(True)을 리턴한다. 이와 반대로 'email'은 a 딕셔너리 안에 존재하지 않는 Key이므로 거짓(False)을 리턴한다.

