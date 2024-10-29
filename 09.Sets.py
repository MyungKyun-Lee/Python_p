#Python Collections (Arrays)
#There are four collection data types in the Python programming language:
#
#(List) is a collection which is ordered and changeable. Allows duplicate members.
#(Tuple) is a collection which is ordered and unchangeable. Allows duplicate members.
#(Set) is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#(Dictionary) is a collection which is ordered** and changeable. No duplicate me


print('------------Python Sets--------------')
thisset = {"apple", "banana", "cherry", "apple"} #집합은 중괄호로 작성
print(thisset)


thisset = {"apple", "banana", "cherry", True, 1, 2} #True and 1는 세트에서 동일한 값으로 간주되며 중복으로 처리
print(thisset)

print('------------Get the Length of a Set--------------')
#thisset = {"apple", "banana", "cherry"}
print(len(thisset))

print('------------Set Items - Data Types--------------')
set1 = {"apple", "banana", "cherry", True, 1, 2, 9, 11}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)

myset = {"apple", "banana", "cherry"}
print(type(myset))

print('------------The set() Constructor--------------')
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

print('------------Access Set Items--------------')
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
print('---------------------')
print("banana" in thisset)
print("banana" not in thisset)

print('------------Add Set Items--------------')
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

print('------------Remove Set Items--------------')
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
print('------------discard 사용시 에러 없음--------------')
thisset = {"apple", "banana", "cherry"}
thisset.discard("bananaa")
print(thisset)

print('------------pop 사용시 무작위로 항목이 제거--------------')
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
print('------------clear() 사용시 모두 제거--------------')
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
print('------------del 사용시 set 제거--------------')
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)
