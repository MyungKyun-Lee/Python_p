print('------------Slicing--------------')
b = "Hello, World!"
print(b[2:6])
print('------------Slice From the Start--------------')
b = "Hello, World!"
print(b[:6])
print('------------Slice To the End--------------')
b = "Hello, World!"
print(b[2:])
print('------------Negative Indexing--------------')
b = "Hello, World!"
print(b[-5:-1])

print('------------Upper Case--------------')
a = "Hello, World!"
print(a.upper())
print('------------Lower Case--------------')
a = "Hello, World!"
print(a.lower())
print('------------Remove Whitespace--------------')
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

print('------------Replace String--------------')
a = "Hello, World!"
print(a.replace("H", "J"))
print('------------Split String--------------')
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
print('------------String Concatenation--------------')
a = "Hello"
b = "World"
c = a + " " + b
print(c)
print('------------String Format--------------')
age = 36
txt = "My name is John, I am " + str(age)
print(txt) # return Err message
print('------------F-Strings--------------')
age = 36
txt = f"My name is John, I am {age}"
print(txt)
print('------------Placeholders and Modifiers--------------')
price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

