# 1.list (Done)
# 2.tuple
# 3.Dictonary
# 4.sets
# 5.strings
# 7. Intertools
# 8. lambda Functions
# 9. Exceptions and Errors
# 10. Logging
# 11. JSON
# 12. Random Numbers
# 13. Decorators
# 14. Generators
# 15. Threading vs Multiprocessing
# 16. Multithreading
# 18. Function Arguments
# 19. Shallow vs Deep copying
# 20. Asterick(*) Operator
# 21. Context Managers


### 1. list: Ordered, mutable, allows duplicate elements
mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist2 = list() #mylist2 = []
print(mylist2)

    ## 1.1 index in list: 
    # '-' neg index
    # -1 means last index, -n means 1st index
    # len(name), len returns size of list 
    #multiple data types allow 

mylist2 = ["apple", 1, 1.56, 'c']
sz = len(mylist2) # 4 LENGHTH

item = mylist2[2]
print(item) #1.56
    
item = mylist2[-1] 
print(item) # 'c'

item = mylist2[-4] 
print(item) # "apple"



## 1.2 LIST  interation: 
    # for-in, index value, 0-n-1,all elements
for i in mylist2:
    print(i) 
    


## 1.3 Check elements present or not
if "apple" in mylist2:
    print("YES")  # output "YES"
else:
    print("NO")
   


## 1.4  inserting in LIST:
mylist2.append("mango1")
mylist2.append("mango2")
print(mylist2) # ['apple', 1, 1.56, 'c', 'mango1', 'mango2']

    #idex insertion
    #in 2nd position, "blueberry"
    #['apple', 'blueberry', 1, 1.56, 'c', 'mango1', 'mango2']
mylist2.insert(1, "blueberry") 
print(mylist2) 




## 1.5 remove items in LIST:
mylist2 = ['apple', 'blueberry', 1, 1.56, 'c', 'mango1', 'mango2']

mylist2.pop() # remove last element
mylist2.remove("apple") # "apple" removed
mylist2.clear() #clear all, removed all elements





## 1.6 Sorting in LIST
mylist2 = [1,5, -3, 3, 19, 11]
mylist2.sort() # main list changed
print(mylist2)

newlist = sorted(mylist2) # main list dont changes, newlist updated 
print(newlist)




## 1.7 LIST decleartion
    # *= 5, concatenate list total 4 times
    # [1, 2] = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
    # concatanate , mylist + mylsit2
mylist2 = [1, 2] * 5 
print(mylist2)
mylist2.append(2)
mylist2 *= 2
print(mylist2)

mylist1 = [1, 2]
mylist2 = [3, 4]

concatMylist = mylist1 + mylist2
print(concatMylist)





## 1.8 list slicing 

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sublist = mylist[1:5] # [st:ed+1], [2, 3, 4, 5]
sublist = mylist[1:] # 1 indx to end
sublist = mylist[:5] # 0 to (5-1)indx
sublist = mylist[:] # 0 to all 
print(mylist)

sublist = mylist[0:9:2] # (0 to 8th indx),inc with 2, i+=2 
sublist = mylist[::-1] # (all value), decrement with i--, reverse
sublist = mylist[::-2] # i-=2
print(sublist)



## 1.9 List Copy

listOrg = [1, 2, 3, 4]
listCopy = listOrg # can't assign, changing in listcopy will also change in original

    #so better way
listCopy = listOrg.copy() #1, copy func 
listCopy = list(listOrg) #2, list argument
listCopy = listOrg[:] #slicing (beg to all)

    # more faster
listfaster = [i+i for i in listOrg] #for i in listor , returns (i)= items, and append to copy lsit
print(listOrg) # [1, 2, 3, 4]
print(listfaster) #[2, 4, 6, 8]


