### Dictionary: Key-value pairs, Unordered, Mutable


mydict = { "name": "bipul", "age":25, "city":"dhaka" }
print(mydict) 

mydict2 = dict(name = "bipul", age = 25, city = "dhaka")
print(mydict2)

value = mydict["age"] #keu , return value
print(value)

mydict["email"] = "bipul15@cse.pstu.ac.bd"
print(mydict)


del mydict["name"];
print(mydict)

mydict.pop("age")
print(mydict)

mydict.popitem()
print(mydict)


if "name" in mydict:
    print(mydict["name"])

try:
    print(mydict["name"])
except:
    print("Error")

for i in mydict:
    print(i)

for i in mydict.keys():
    print(i)

for i in mydict.values():
    print(i)

for key, val in mydict.items():
    print(key, val)


mydict_cpy = mydict
print(mydict_cpy)
#but changing also effect in originals
#assignment , versy carefull


mydict_cpy = mydict.copy()
mydict_cpy = dict(mydict)


#merge two dict

mydict = { "name": "bipul", "age":25, "city":"dhaka" }
mydict2 = { "name": "bipul2","email": "rabbecse1677@gmail.com"}

mydict.update(mydict2) 
# overwrite, update keys or add new key value from mydict2
print(mydict)


mydict = { 3: 9, 6: 36, 9:81}
print(mydict)

value = mydict[3] #key
print(value)

# list --> dict , not possible
# tuple --> dict, possible

mytuple = (8, 7)
mydict = {mytuple : 15}

print(mydict)

