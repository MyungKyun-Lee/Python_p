print('------------Tuple--------------')
thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

print('------------   --------------')
thistuple = ("apple",)   #콤마 있으면
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

print('------------   --------------')
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

print('------------Access Tuple Items--------------')
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

print('------------Range of Indexes--------------')
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple)
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[2:])
print(thistuple[-4:-1])

print('------------Check if Item Exists--------------')
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

print('------------Update Tuples--------------')
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

print('------------Add Items--------------')
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

print('------------ 다른 방법 --------------')
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

print('------------Remove Items--------------')
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

print('------------ 다른 방법 에러 --------------')
thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) #this will raise an error because the tuple no longer exists

print('------------Unpack Tuples--------------')
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

print('------------Using Asterisk* --------------')
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits  #*변수 이름에 을 추가하면 값이 목록으로 변수에 할당

print(green)
print(yellow)
print(red)

print('------------Using Asterisk* --------------')
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

print('------------Loop Tuples--------------')
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

print('------------Loop Tuples--------------')
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

print('------------Using a While Loop--------------')
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

print('------------Join Tuples--------------')
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

print('------------ --------------')
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
