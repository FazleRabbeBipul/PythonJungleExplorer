### 6 Collections: Counter, namedtuple,OrderedDict, Defaultdict, deque

## 6.1 : Counter
from collections import Counter
a = "aaaaabbbbbbcccccc"
myCounter = Counter(a)

print(myCounter) # Counter({'b': 6, 'c': 6, 'a': 5})
print(myCounter.items()) #dict_items([('a', 5), ('b', 6), ('c', 6)])
print(myCounter.keys()) # dict_keys(['a', 'b', 'c'])
print(myCounter.values()) # dict_values([5, 6, 6])

print(myCounter.most_common(1)) #[('b', 6)] # 1 means,one common
print(myCounter.most_common(2)) #[('b', 6), ('c', 6)] # 2 means,two common


print(myCounter.most_common()[2][0]) #()[2nd][key] , 'a'
print(myCounter.most_common()[2][1]) #()[2nd][value] , '5' times

print(list(myCounter.elements())) # print all the elements



## 6.2 namedtuple

from collections import namedtuple
point = namedtuple('point', 'x,y') # (clasname, 'field1, field2')
pt = point(1, -4)

print(pt)
print(pt.x, pt.y)



## 6.3 OrderDict
from collections import OrderedDict

OrderedDict = OrderedDict()
OrderedDict['a'] = 1
OrderedDict['b'] = 2
OrderedDict['e'] = 3
OrderedDict['f'] = 4
OrderedDict['g'] = 5
OrderedDict['c'] = 6

print(OrderedDict)


## 6.4 Defaultdict
from collections import defaultdict
d = defaultdict(int)

d['a'] = 1
d['b'] = 2
print(d['c']) # default value 0 returns



## 6.5 Deque
from collections import deque
d = deque()

#6.5.1 add to right
d.append(1)
d.append(2)
d.append(3)
print(d)

#6.5.2 add to the front
d.appendleft(0) # append to the front 0
print(d)

#6.5.3 Remove 
d.pop() # removes from back
d.popleft() #removes from left
d.clear() # remove all elements

#6.5.4 Extends
d.extend([4, 5, 6]) # add those at right side
d.extendleft([10, 20, 30]) # frist 10, then 20, then 30
# deque([30, 20, 10, 4, 5, 6])


#6.5.5 Rotations
d.rotate(1) # rotate 1 right shift right
d.rotate(-1) # rotate 1 left shift
d.reverse() # reverse the deque

print(d) 