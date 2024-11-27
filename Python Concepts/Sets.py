### 4, Sets: unordered, nutable, no duplicates

## 4.1
myset = {} # its a dictionary
myset = set() # it's a set
myset = {1, 2, 3, 4, 2}
print(myset) # {1, 2, 3, 4}

    #4.1.1 undordered, string, list as set
myset = set([1, 2, 3, 4, 2])
print(myset) #{1, 2, 3, 4}

myset = set("Hello")
print(myset) #{'H', 'e', 'o', 'l'} unordered

## 4.2 add elements
myset.add(1)
myset.add(2)
myset.add(3)
print(myset)


## 4.3 remove elemnets
myset.remove(3) #removed
#myset.remove(3) # Key error, 3 not present in set
myset.discard(3) # remove also, in this case no error
myset.pop() #remove arbitiory elements from set
myset.clear() # remove all elements


## 4.4 iterate
for i in myset:
    print(i)
myset = {1, 2, 3, 4, 2}

## 4.5 , find a element
if 2 in myset:
    print("YES")


## 4.6 Unions
odd = {1, 3, 5, 7, 9}
even = {2, 4, 6, 8}
prime = {2, 3, 5, 7}    

#4.6.1 Union: all the elements of both set
u = odd.union(even)
print(u)

#4.6.2 intersection
i = even.intersection(prime)
print(i) # 2: only 2 insersect



setA = {1, 2, 3, 4, 5, 6, 12}
setB = {1, 2, 3, 10, 11, 12}

## 4.7 difference (all number that diffrent from A, as indx)
diff = setA.difference(setB)
print(diff) #{4, 5, 6}


## 4.8 symmetric_difference (all elemnet that are not in both)
diff = setA.symmetric_difference(setB)
print(diff) #{4, 5, 6, 10, 11}



## 4.9 Set updates

#4.9.1
setA.intersection_update(setB)
print(setA) #{1, 2, 3, 12}, update with the common elements of setA and setB

#4.9.2
setA = {1, 2, 3, 4, 5, 6, 12}
setB = {1, 2, 3, 10, 11, 12}
setA.difference_update(setB)
print(setA)
#{4, 5, 6} removes the elements from setA those are found in another set, setB


#4.9.3
setA = {1, 2, 3, 4, 5, 6, 12}
setB = {1, 2, 3, 10, 11, 12}
setA.symmetric_difference_update(setB)
print(setA) #{4, 5, 6, 10, 11}
#remove elements those are found in both.


##4.10 superset
setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
print(setB.issubset(setA)) #True, all elements of setB is present in setA
print(setB.issuperset(setA)) #False, setB doesn't contains all the element of setA


##4.11 disjoint
setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
setC = {7, 8}


print(setA.isdisjoint(setB)); #false, they have same element
print(setA.isdisjoint(setC)); #false, no same elements





##4.12 Copying set
setA = {1, 2, 3, 4, 5, 6}

setB = setA # this will change also original set
setB = setA.copy() # valid
setB = set(setA) # valid


## 4.13 frozenset

a = frozenset([1,2 , 3, 4, 5])
a.remove(2) # error
a.add(10) # error
#its frozen , can't change 





