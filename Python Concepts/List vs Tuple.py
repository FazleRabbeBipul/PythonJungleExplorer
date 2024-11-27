### Compare Memory and Time complexity of LIST and TUPLE


## Memory Complexity
import sys

list_ = ["Welcome", "to", "Python", "Juncle", 2024, True, 0, 1, 2]
tuple_ = ("Welcome", "to", "Python", "Juncle", 2024, True, 0, 1, 2)

print(sys.getsizeof(list_), "bytes")  # list 136 bytes
print(sys.getsizeof(tuple_), "bytes") # tuple 112 bytes



## Time COmplexity

import timeit
print(timeit.timeit(stmt = "list", number = 1000000))   # 0.06804665999516146
print(timeit.timeit(stmt = "tuple", number = 1000000))  # 0.06344158299907576


# Better Memory and Time using Tuple 