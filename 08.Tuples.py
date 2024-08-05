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
