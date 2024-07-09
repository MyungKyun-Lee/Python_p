print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
print('-------------Quotes Inside Quotes-------------')

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print('-------------Multiline Strings-------------')

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
print('------------Multiline Strings--------------')

a = "Hello, World!"
print(a[1])
print('------------Strings are Arrays--------------')

for x in "banana":
  print(x)
print('------------Looping Through a String--------------')

txt = "The best things in life are free!"
print("free" in txt)
print()

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

print('------------Check String--------------')

txt = "The best things in life are free!"
print("expensive" not in txt)
print()

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
print('------------Check if NOT--------------')
