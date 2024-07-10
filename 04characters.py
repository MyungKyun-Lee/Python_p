print('------------Escape Character--------------')
#txt = "We are the so-called "Vikings" from the north."
txt = "We are the so-called \"Vikings\" \nfrom the north."
print(txt)

#This example erases one character (backspace):
txt = "Hello \b(backspace)World!(backspace)"
print(txt) 
#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt)
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)

print('------------문자열 함수--------------')
txt = "hello, and welcome to my world. 첫글자 대문자로"
x = txt.capitalize()
print (x)
txt = "Hello, And Welcome To My World! 모두 소문자로"
x = txt.casefold()
print(x)
print(x.lower())

txt = "banana 중앙으로"
x = txt.center(20)
print(x)

txt = "My name is Ståle"
y=" <-특수문자 encode() Method"
x = txt.encode()
print(x)
print(y)
