print('------------Boolean Values--------------')
print(10 > 9)
print(10 == 9)
print(10 < 9)
print('------------(a = 200 b = 33) if b > a: --------------')
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
print('------------Evaluate Values and Variables--------------')
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

print('------------EMost Values are True--------------')
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

print('-----------함수 리턴값이 0 이면 거짓---------------')
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

print('------------Functions can Return a Boolean--------------')
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
print('--------------------------')
x = 200
print(isinstance(x, int))
