###  2 tuples : ordered, immutable, allows duplicates


## 2.1 tuple declaration
print(" 2.1 tuple declaration")
    # if items count 1, then must ',' at end.
    # () or nothing just use comma ','

mytuple = "hlo", 23, "python" 
mytuple = "hlo",   # tuple, must add ','
mytuple = "hlo"    # NOT tuple, it's STRING!

    # using ()
mytuple = ("hlo", 23, "python")
mytuple = ("hlo",)   # ',' must add
mytuple = ("hlo") # NOT tuple, String

print(type(mytuple)) 
print(mytuple)




## 2.2 Convertion,
    # tuple(list)
    # list(tuple)
print("2.2 Convertion")
mytuple = tuple([1, 2, 5, -3, "hi"]) # tuple <-- list
mylist = list(mytuple) # list <-- tuple
mytuple = tuple(mylist)



## 2.3  indexing
print("2.3  indexing")

mytuple = ("banana", "apple", "mango", -11, 'x')
item = mytuple[1] # apple
item = mytuple[-1] # 'X'


## 2.3 immutable 
print("2.3 immutable ")
    # can't do this assignment opration
    # invalid, no update
    # mytuple[1] = "apple2"


## 2.4 check anything in tuple
print("2.4 check anything in tuple")
if "apple" in mytuple:
    print("YES")
else:
    print("NO")
    

## 2.5 Travarsal 
print("2.5 Travarsal ")
for i in mytuple:
    print(i)
# banana
# apple
# mango
# -11
# x
    

## 2.6, Count items
print("2.6, Count items")

mytuple = ('a', 'b', 'a', 'e', 'd', 'e', 'e', 'o')

sz = len(mytuple) # size of mytuple
cnt = mytuple.count('e') # 3
idx = mytuple.index('b') # first occurence

print(sz)
print(cnt)
print(idx)


## 2.7 Interation 
print("## 2.7 Interation ")
mytuple = ('a', 'b', 'a', 'e', 'd', 'e', 'e', 'o')

newtuple = mytuple[:]     # 0 to end index
newtuple = mytuple[1:4]   # ('b', 'a', 'e')
newtuple = mytuple[: 4]   # start to (4-1)th indx
newtuple = mytuple[2:]    # indx 2 to end

print(mytuple[::2])    # i = i + 2 , increas indx by 2.
print(mytuple[::-2])   # i = i - 2, decrease indx by -2


## 2.8  Packing , Unpacking
print("2.8  Packing , Unpacking")
# 2.8.1 Unpack
print("# 2.8.1 Unpack")
    # tuple unpack, variable count and order matters. else error
myTuple = "Dhaka", 24, "Khulna"
city1, year, city2 = myTuple

print(city1) # "Dhaka"
print(year) # 24
print(city2) # "Khulna"


# 2.8.2 multple element unpack
print("# 2.8.2 multple element unpack")
    # only single * starred expressions 
    # every varibles represent one item, and *variable contains rest


myTuple = (0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
a, b, c, *d, e = myTuple

print(a)    # 0
print(b)    # 1
print(c)    # 2
print(tuple(d)) # (3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
print(e) # 13

