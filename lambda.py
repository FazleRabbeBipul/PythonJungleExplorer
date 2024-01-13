### lambda arguments : expression


add10 = lambda x : x + 10
# func = func input : return func
# so we can call this func

ans  = add10(5)
print(ans)


# input a,b , output a*b
prod = lambda a,b : a*b
print(prod(2, 3))


def sort_by_y(x):
    return x[1]

a= [(1, 2), (15, 1), (5, -1), (10, 4)]
# default sort by first value

b = sorted(a, key = lambda x : x[0] + x[1]) # sorted as sum
b = sorted(a, key = lambda x : x[1]) # sorted by second value

print(b)



## map 

a = [1, 2, 3, 4, 5]
b = map(lambda x : x*2, a)
print(list(b))

#another way list comprehension
c = [x*2 for x in a]
print(c)


# filter function ( func, seq)
c = [x for x in a if x%2 == 0]
print(c)

#reduce function
from functools import reduce 
prod = reduce(lambda x,y : x*y,a)
print(prod)
