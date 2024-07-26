print('------------Operator Precedence--------------')
thislist = ["apple", "banana", "cherry"]
print(thislist)

print(thislist[1])
print(thislist[-1])

print('------------Range of Indexes 2 3 4--------------')
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

print(thislist[:4])
print(thislist[2:])

print('------------Range of Negative Indexes--------------')
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

print('------------Check if Item Exists--------------')
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

print('------------Change Item Value--------------')
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

print('------------Change Item Value--------------')
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

print('------------Change Item Value--------------')
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

print('------------Insert Items--------------')
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

print('------------Add List Items--------------')
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

print('------------Insert Items--------------')
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

print('------------Extend List--------------')
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

print('------------Add Any Iterable--------------')
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

print('------------Remove Specified Item--------------')
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# banana 2개 있는 경우 1번만 삭제
thislist = ["apple", "banana", "cherry", "banana", "kiwi"] 
thislist.remove("banana")
print(thislist)

print('------------Remove Specified Index--------------')
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()    # 숫자 없으면 마지막 item 만 삭제
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]   # del 키워드로 삭제
print(thislist)

thislist = ["apple", "banana", "cherry"]
#del thislist      # 키워드 del는 목록을 완전히 삭제
#print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.clear()    # 해당 clear()메서드는 목록을 비웁니다.
print(thislist)

print('------------Loop Through a List--------------')
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

print('------------Loop Through the Index Numbers--------------')
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

print('------------Using a While Loop--------------')
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist) :
  print(thislist[i])
  i = i + 1

print('------------Looping Using List Comprehension--------------')
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

print('------------List Comprehension--------------')
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]     # 구문 [expression for item in iterable if condition == True]
print(newlist)
newlist2 = [x for x in fruits if x != "apple"]
print(newlist2)

print('------------Iterable--------------')
newlist = [x for x in range(10)]
print(newlist)
newlist = [x for x in range(10) if x < 5]
print(newlist)

print('------------Expression--------------')
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]     # 대문자로
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

print('------------Sort List Alphanumerically--------------')
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)     # Sort Descending
print(thislist)

print('------------Customize Sort Function--------------')
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

print('------------Case Insensitive Sort--------------')
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()       # 문자 배열은 대문자-> 소문자 정렬
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)    # 소문자로 변경우 정렬
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()    # 배열의 순서 역순으로 변경
print(thislist)

print('------------Copy a List--------------')
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)   # copy 다른 방법
print(mylist)

print('------------Join Two Lists--------------')
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
# -------------------------
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)   # list1에 LIST2를 합치는 것
print(list1)
# -------------------------
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
# -------------------------

