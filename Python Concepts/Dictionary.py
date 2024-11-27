### 3: Dictionary: Key-value pairs, Unordered, Mutable


## 3.1 Declaration
mydict = { 
    "name": "bipul", 
    "age":25, 
    "city":"dhaka" 
    }
print(mydict) 

mydict2 = dict(name = "bipul", age = 25, city = "dhaka")
print(mydict2)

## 3.2 Key, value
value = mydict["age"] # "age" is a key
print(value) # 25 is the valu for "age" key


## 3.3 New items adding  
mydict["email"] = "bipul15@cse.pstu.ac.bd"
print(mydict)


## 3.4 Deletion item
del mydict["name"]; #  key "name" deleted, including its value
print(mydict)

mydict.pop("age") # pop (key) delete "age" key
print(mydict)

mydict.popitem() # popitem() delete the last element from dictionary
print(mydict)


## 3.5 finding items in Dictionary 
if "name" in mydict:
    print(mydict["name"])

    ##3.5.1 try except , error handling
try:
    print(mydict["name"])
except:
    print("Error")

## 3.5 Dictionary travarsal
    
    #3.5.1 based on 'Key'
for i in mydict:
    print(i)
    
    #3.5.2 based on Keys()
for i in mydict.keys():
    print(i)

    #3.5.3 based on .values()
for i in mydict.values():
    print(i)

    #3.5.4 based on .items()
for key, val in mydict.items():
    print(key, val)


## 3.6 Dictionary Copy
    # can't assign, it also changes original dictionary if we change in copyDictionary
mydict_cpy = mydict # be carefull
print(mydict_cpy)

    ## Better way
mydict_cpy = mydict.copy()
mydict_cpy = dict(mydict)


## 3.7 Merge Two Dictionary
    # overwrite, update keys or add new key value from mydict2
mydict = { "name": "bipul", "age":25, "city":"dhaka" }
mydict2 = { "name": "bipul2","email": "rabbecse1677@gmail.com"}
mydict.update(mydict2) 
print(mydict)


## 3.8 Access with only Key
mydict = { 3: 9, 6: 36, 9:81}
print(mydict)
value = mydict[3] #key
print(value)

## 3.9 converstions
    # list --> dict , not possible
    # tuple --> dict, possible

mytuple = (8, 7)
mydict = {mytuple : 15}

print(mydict)

