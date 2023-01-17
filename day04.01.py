# chap 7 tuple

# 7-1-1 create tuple
# name = ()  # 요소가 비어있는 tuple 생성
# print(type(name))
# name = 'harry',  # 하나의 요소의 경우 ,를 붙여서 생성 즉, 'harry'의 요소 하나만 가지고 있는 상태
# print(name)
# name = ('hermione')  # string 즉, 하나의 문자열은 string, 2개 이상은 tuple이라 이해 하자.
# print(type(name))
# name = 'harry', 'ron'  # packing
# print(type(name))
# x, y = name  # tuple은 한 번에 여러 변수를 할당 할 수 있다. 단 요소와 변수의 개수가 같아야 한다. 두 번째 'harry', 의 경우 1개만 가지고 있다.
# print(y)


# password = 'swordfish'

# 7.1.2 create with tuple
# marx_list = ['Groucho', 'Chico', 'Harpo']
# print(type(tuple(marx_list)))

# 7.1.3 combine tuples by Using +
# ('Groucho',) + ('Chio', 'Harpo')

# 7.1.4 paste
# ('yada',) * 3

# 7.1.5 compare
# a = (7, 2)
# b = (7, 2, 9)
# print(a == b, a <= b, a < b, a >= b) # 대응하는 요소끼리만 비교한다.

# 7.1.6 for and in
# words = ('fresh', 'out', 'of', 'ideas')
# for word in words:
#     print(word) # 각 요소 별로 하나씩 순회해서 실행한다.

# 7.1.7 modipy
# name = ('Groucho',) + ('Chico', 'Harpo')
# print(name)

# 추가적으로 튜플의 경우 불변성 때문에 list로 변환 후 값을 변경하여 다시 tuple로 변환해서 저장한다.
# scores = ('B+', 'A+', 'C+')
# print(scores[1], scores[2])
# temp = list(scores)
# temp[1] = 'C+'
# temp[2] = 'A+'
# scores = tuple(temp)
# print(scores[1], scores[2])



# 7.2 list

# 7.2.1 create
# empty_list = []
# another_empty_list = list()
# years = [2000, 2001, 2002]

# 7.2.2 list()
# print(list('cat')) # 문자열 하나의 경우 문자 하나씩 나누고 튜플의 경우 리스트로 변환한다.

# 7.2.3 split()
# day ='21/04/2000'
# print(day.split('/')) # split()함수의 경우 괄호 안의 문자로 나누는 역할을 한다.

big_bang = ['GD', '태양', '탑', '대성', '승리']
exo = ['백현', '첸']
# 7.2.4 offset
# print(big_bang[2]) # []안의 인덱스에 따라 출력 음수도 사용가능하다.

# 7.2.5 slice
# print(big_bang[2:4])  # range(2,4)으로 이해하면 쉽다
# print(big_bang[-4:-1])
# print(big_bang[::2])  # 왼쪽부터 2칸당 하나씩 출력
# print(big_bang[::-2])
# big_bang.reverse()  #리스트 반대로 뒤집은 상태로 저장

# 7.2.6 append
# exo.append(big_bang)
# print(exo) # list안에 list가 들어간 형태

# 7.2.7 insert
# big_bang.insert(1, '인하')
# print(big_bang)

# 7.2.8 copy
# print(big_bang*2)
# 7.2.9 extend()
# exo.extend(big_bang)
# exo += big_bang
# exo = exo + big_bang   # 셋 다 같은 출력형태를 띔.
# print(exo)

# 7.2.10 offset
# big_bang[2] = '싸이'
# print(big_bang)

# 7.2.11 change by slice
# big_bang[1:4] = ['뷔', '장범준', '창모']
# print(big_bang)
# big_bang[1:3] = ['뷔', '장범준', '창모'] # 개수가 달라도 출력 가능
# print(big_bang)
# list의 특징은 순회가능한 타입 값은 모두 할당이 가능하다. str, tuple 등등 대부분 가능
# big_bang[1:3] = (12, 21, 23)
# print(big_bang)

# 7.2.12~15 pop, remove, del, clear
# exo.append(big_bang)
# print(exo.pop())  # 빅뱅 pop
# print(exo)

# exo.append(big_bang)
# print(exo[2].pop())  # 승리 pop

# exo[2].remove('태양')  # 2번째 리스트에서 태양 삭제
# print(exo)

# del exo[2][-1]  # 대성 delete
# print(exo)

# exo.clear()  # 전부 삭제
# print(exo)

# 7.2.16~19 index, in, count, join
# print(exo.index('첸'))  # 첸이란 문자열이 있는 첫번째 인덱스를 반환
# print('백현' in exo)  # 백현이란 문자열이 있는 지 확인하고 있으면 True 반환

# exo.append(big_bang)
# print('태양' in exo) # list 안의 big_bang이라는 list에서는 검색할 수 없음

# exo = ['백현', '첸', '장첸']
# print(exo.count('첸')) # list 안의 첸이란 항목 검색, 정확한 글자만 확인함.

# sep = '*'
# joined = sep.join(big_bang)
# print(joined)
# separated = joined.split(sep)
# print(separated)
# print(big_bang == separated)  # split 함수가 쪼개는 거라면 joined 함수는 병합하는 함수다.

# 7.2.20~22 sort, sorted len, =
# mixed = [6, 4, 5, 'A', 7, '트와이스', 'B', 'b', '마마무'] #정렬 시엔 모두 같은 type 형태 여야 정상적으로 작동한다.
# mixed = ['6', '4', '5', 'A', '7', '트와이스', 'B', 'b', '마마무']
# mixed.sort()
# print(mixed)
# mixed.sort(reverse=True)
# print(mixed)

# len(mixed)

# primes =[2, 19, 3.0, 5, 7, 11]
# print(primes)
# primes.sort()
# print(primes)
# primes_sorted = sorted(primes) # s.ort()를 사용하면 영원히 변한다.
# print(primes_sorted)

# big_bang[0] = '10cm'
# print(big_bang)

# 7.2.23
import copy
a = [1, 2, [5, -9]]
b = copy.deepcopy(a) # deepcopy함수의 경우 새로 참조하지 않는다.
c = list(a) # mutable, deepcopy
d = a[:]
a[2][1] = 7  # mutable, b/c/d affects
a[1] = -77  # immutable
print(a, b, c, d)
# immutable 이면 복제해도 원소가 바뀌면 해당 객체만 바뀌지만,
# mutable 인 경우 모든 복제품이 바뀐다.

# a = [1, 2, 3]
# b = a.copy()
# c = list(a)
# d = a[:]
# a[2] = 'sw'
# print(a, b, c, d)


# primes = [2, 19, 3, 5, 7, 11]
# primes_cp = primes
# print(primes)
# print(primes_cp)
# primes[-1] = 'lunch time'
# print(primes)
# print(primes_cp)
# primes_cp[0] = 'morning coffee'
# print(primes)
# print(primes_cp)


# for row in range(1, 10):
#     for col in range(1, 10):
#         print(row, col)

# list comprehension
# odd_lists = [i for i in range(1, 11)if i % 2 ==1]
# print(odd_lists)
# tuples_lists = (i for i in range(1, 11)if i % 2 ==1)
# print(type(tuples_lists))

# odd_lists = []
# for i in range(1, 11):
#     if i % 2 == 1:
#         odd_lists.append(i)
# print(odd_lists)


# chap 8 dictionary and set
students = {'name': '김인하', 'age': 23, 'eyes': [0.8, 0.1]}
# print(students.values())
# for k in students.keys():
# for k in students:
# for k in students.values():
# for k, v in students.items():
#     print(k)
    # print(f'{k}: {v}')
# print(f'이름은 {students["name"]}, 나이는 {students["age"]}세', end=' ')
# print(f'시력은 좌:{students["eyes"][0]}, 우:{students["eyes"][0]}')

# alcohol_snack = {'맥주': '치킨', '소주': '골뱅이소면', '위스키': '치즈', '고량주': '짬뽕'}
alcohol_snack = dict(맥주='치킨', 소주='골뱅이 소면', 와인='치즈', 고량주='짱뽕')
alcohol_list = list(alcohol_snack) # extract keys
food_list = [food for food in alcohol_snack.values()]

# for food in enumerate(food_list): # tuple return
#     print(food[1])

# for i in range(len(food_list)):
#     print(food_list[i])

# for food in food_list:
#     print(food)


# import random
# while True:
#     alcohol = input(f'술을 선택 하세요 1){alcohol_list[0]} 2){alcohol_list[1]} 3){alcohol_list[2]} 4){alcohol_list[3]}
#     5)나가기 6) 아무거나')
#     if alcohol == '5':
#         print('다음에 또 오세요~')
#         break
#     elif alcohol == '1':
#         print(f'{alcohol_list[0]}에 어울리는 안주는 {alcohol_snack[alcohol_list[0]]}')
#         pass
#     elif alcohol == '2':
#         print(f'{alcohol_list[1]}에 어울리는 안주는 {alcohol_snack[alcohol_list[1]]}')
#         pass
#     elif alcohol == '3':
#         print(f'{alcohol_list[2]}에 어울리는 안주는 {alcohol_snack[alcohol_list[2]]}')
#         pass
#     elif alcohol == '4':
#         print(f'{alcohol_list[3]}에 어울리는 안주는 {alcohol_snack[alcohol_list[3]]}')
#         pass
#     elif alcohol == '6':
#         print(f'{random.choice(alcohol_list)}와 {random.choice(food_list)}는 어떠신가요?')
#         pass
#     else:
#         print('메뉴에서 골라 주세요.')

# first = {'a':'agony', 'b':'bliss'}
# second = {'b':'bagels', 'c':'candy'}
# print({**first, **second})


