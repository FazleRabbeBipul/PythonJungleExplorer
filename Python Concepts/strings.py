# ## 5.:String: ordered, imutable, text represtation

## 5.1 String Declaration
myString = ''
# or,
myString = ""
myString = "hello world"
myString = "hello 'Bipul', how are you?" # hello 'Bipul', how are you?

myString = 'i am a programmer' 

#i'm a progranner
myString = 'i\'m a progranner' #\ use to ignore, next '

#i love "coding" ....
myString = "i love \"coding\" ...." #
print(myString)

myString = """Hello    
World""" ## for documentations



## 5.2 String index  , substring
myString = "hello world"
myString[0]   #  'h'
myString[-1]  #  'd'

substring = myString[1:7] 
print(substring) # "ello w"

substring = myString[:] # 0 to n-1
substring = myString[::-1] # reverse all
substring = myString[::+2] # 0, 2, 4 ... those index
substring = myString[1::2] # 1, 3, 5, .... those index


## 5.3 string concatenation
myString = "Hello"
name = "Jenny"
sentence = myString + " " + name
print(sentence)

# print every index
for i in sentence:
    print(i) 

# search by 'char' or substring 
if 'el' in sentence:
    print("YES") 



## 5.4 string strip()
myString = '    hello   world   '
newstring = myString.strip() ## removes blank space from front and end 
print(newstring) # "hello   world"


## 5.5 uppercase, lowercase
myString = "Hi this IS pYthon JungLe"
u = myString.upper()
l = myString.lower()
print("UpperCase: ",u, " && ", "LoweCase: ", l)

myString = "Hi this IS pYthon JungLe"
print(myString.startswith("Hi"))
#Case sensative , is my sting start with this "xx"?



## 5.6 finding positions of substring
myString = "Hi this IS pYthon JungLe"
print(len(myString)) # length of string, 24 length

idx = myString.find('x')
print(idx) # did't find, so return '-1' value.

idx = myString.find('i')
print(idx) # first occurence, '1' position

#substring search
idx = myString.find("Jun")
print(idx) # 18th position

#count occurances
cnt = myString.count("i")
print(cnt) # 2 times



## 5.7 replace, not in original
myString = "Hi this IS pYthon JungLe"
newString = myString.replace('this', ',')
print(newString) # "Hi , IS pYthon JungLe"
#Can't change in main string!


## 5.8 string split()
myString = "how are you doing"
mylist = myString.split(" ") # insert each word as list elements, separate through " "
print(mylist) #['how', 'are', 'you', 'doing']


#5.8.1  String join, gain make string
newString = ''.join(mylist)
print(newString) #howareyoudoing

newString = ','.join(mylist)
print(newString) #how,are,you,doing

newString = ' '.join(mylist)
print(newString) #how are you doing



## 5.9 timer, using join() faster prove
from timeit import default_timer as timer 
mylist = ['a'] * 6
print(mylist)

#1. bad approach
start = timer()
myString = ''
for i in mylist:
    myString += i
stop = timer()

print(myString, stop-start)


#2. good approach, faster
start = timer()
myString = ''.join(mylist)
stop = timer()
print(myString, stop-start)




## 5.10 String formating

# 5.10.1 , %
str = "Jenny"
myString = "Hi %s" % str
print(myString)

mark = 78
myString = "Maths Score %d " % mark
print(myString)

cgpa = 3.69
myString = "Final result %.2f." % cgpa # .2 means, 2 digit after  decimal
print(myString)



# 5.10.2  .format()
var  = 3.1234567
var2 = 9
myString = 'this variable is {:.2f} and {}'.format(var, var2) # into curly brack .2f means 2 digit after decimal point
print(myString)



# 5.10.3 f-string
var  = 3.1234567
var2 = 9
myString = f'this variable is {var:.2f} and {var2}' # into curly brack var:.2f means 2 digit after decimal point
print(myString)