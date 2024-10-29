print('------------Python Dictionaries-------------')
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("thisdict[brand] = "+thisdict["brand"])

print('------------Dictionaries 중복인경우-------------')
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
print("---- len(thisdict) 중복제거후 길이 -->"+str( len(thisdict) ))

print('------------Dictionaries 데이터유형 경우-------------')
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "year": 2020,
  "colors": ["red", "white", "blue"]
}
print(thisdict)

print('------------Dictionaries dict()생성자를 이용-------------')
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

print('------------Dictionaries Accessing Items-------------')
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
x = thisdict.get("model")
print(x)
x = thisdict.keys()
print(x)
print('------------Dictionaries Accessing Items2-------------')
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

x = thisdict.items()
print(x) #dict 목록의 뉴플로 반환
print('------------Dictionaries Accessing 키가 존재하는지 확인-------------')
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

print('------------Dictionaries Accessing 항목변경-------------')
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)

thisdict.update({"year": 2020})
print(thisdict)

print('------------Dictionaries Accessing 항목추가-------------')
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
thisdict.update({"color2": "red"})
print(thisdict)

print('------------Dictionaries Accessing 항목제거-------------')
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
print('------------ 마지막 입력 항목 삭제 ---------------------')
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
print('------------ 입력 항목 삭제 ---------------------')
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
print('------------ 전체  삭제 ---------------------')
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
#print(thisdict) #this will cause an error because "thisdict" no longer exists.
print('------------ 값만  삭제 ---------------------')
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
