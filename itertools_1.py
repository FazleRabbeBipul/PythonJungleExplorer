# # # ### 7 itertools: products

# # 7.1 # product two dict
from itertools import product 

a = [1, 3]
b = [2]

prod = product(a, b, repeat =2) # res1 * res1
print(list(prod))


# # 7.2 Perputations
from itertools import permutations
a = [1, 2, 3]
perm = permutations(a)
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
print(list(perm))

perm = permutations(a, 2) # (2nd perameter is the length)
print(list(perm))
#[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]


# # 7.2 Combinations
from itertools import combinations
a = [1, 2, 3]
comb = combinations(a, 2)
print(list(comb))
# [(1, 2), (1, 3), (2, 3)]


# #7.3
from itertools import combinations, combinations_with_replacement
a = [1, 2, 3,4]

comb = combinations(a, 2)
print(list(comb))

combWR = combinations_with_replacement(a, 2)
print(list(combWR)) #(1, 1)


# # 7.4
from itertools import accumulate
import operator

from itertools import accumulate
a = [1, 2, 3, 4]
acc = accumulate(a)
print(a)
print(list(acc)) # cumulative sum [1, 3, 6, 10]


a = [1, 2, 3, 4]
acc = accumulate(a, func = operator.mul)
print(a)
print(list(acc)) # cumulative multiplication [1, 2, 6, 24]


a = [1, 2, 5, 3, 4]
acc = accumulate(a, func = max)
print(a)
print(list(acc)) # max in each comparison, 0 to ed [1, 2, 5, 5, 5]




# 7.5 groupby

from itertools import groupby

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def fun(val):
    return val & 1

b = groupby(a, key = fun)
b = groupby(a, key = lambda val : val & 1) #lamda way

for key, value in b:
    print(key, list(value)) 


Person = [
    { 'name': 'Bipul', 'age': 25}, 
    { 'name': 'Anik', 'age': 25}, 
    { 'name': 'Niloy', 'age': 23}, 
    { 'name': 'Sumon', 'age': 27}, 
    { 'name': 'Sojib', 'age': 26}, 
]


PersonGroup = groupby(Person, key = lambda x : x['age'])
# group by Age, but note. its only compare with neighbour
for key, val in PersonGroup:
    print(key, list(val))




## 7.6  count, cycle, repeat

from itertools import count, cycle, repeat

for i in count(10): ## its infinite loop from 10 ....
    print(i)
    if i == 15:
        break 



a = [1, 2, 3]

for i in cycle(a): ## cycle print 1 2 3 ->  1 2 3.....
    print(i)

for i in repeat(2, 4): ## print 2, 2nd argument 4 means , 4 tiems print
    print(i) 