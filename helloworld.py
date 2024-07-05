import sys

#This is a comment
print(sys.version)

print("Hello, World!")

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x)
print(y)
print(z)
print()


x = 5
y = "John"
print(type(x))
print(type(y))
print()

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
print()

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
print()

x = 5
y = 10
print(x + y)
print()

x = 5
y = "John <--숫자와 문자 덧셈은 모두 무자로 표시 출력"
print(x, y)
print()

x = "Global Variables"

def myfunc():
  print("Python : " + x)

myfunc()
print('--------------------------------------')

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x + ' <--지역변수 임')

myfunc()

print("Python is " + x)
print('--------------------------------------')

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x + ' <---글로벌 변수 선언으로 변경됨')
