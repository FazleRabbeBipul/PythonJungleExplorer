# ### Eroor and Exceptions

#
a = 5
my_dict = {'name': 'max'}
#my_dict['age'] #key error 


#
x = -5
if x < 0:
    raise Exception(' X should be positive')


## assert
assert(x >= 0), 'X is not positive' #AssertionError: X is not positive


a = 5 / 0 
# ZeroDivisionError: division by zero, and code stoped 


## try except,  # code will continue from here 
try:
    a = 5/0
except:
    print('an error happend')
   


## show error 
try:
    a = 5/0
except Exception as e:
    print(e) # show error : division by zero 


## Type error
try:
    a = 5/1
    b = a + '10'
except Exception as e:
    print(e)
    # show error : dunsupported operand type(s) for +: 'float' and 'str 
    # TypeError


try:
    a = 5/1
    # b = a + '10'
except Exception as e:
    print(e)
else:
    print("everything is fine") 
    # if no error



## finally : # no matter it will run
try:
    a = 5/1
    b = a + '10'
except Exception as e:
    print(e)
else:
    print("everything is fine")
finally: # no matter it will run
    print('Cleaning up...')


## exception class
class ValueToHighError(Exception):
    pass

# test func creation
def test_value(x):
    if(x > 100):
        raise  ValueToHighError('value is too High') #check exception
    
test_value(200)
# testing with input



## testing with input with try and except
class ValueToHighError(Exception):
    pass

def test_value(x):
    if(x > 100):
        raise  ValueToHighError('value is too High')
    

try:
    test_value(200)
except ValueToHighError as e:
    print(e)



## show error with message and value by error class

class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
     def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
     if x > 100:
          raise ValueTooHighError("Value is too High!!! ")
     if x<5:
          raise ValueTooSmallError("Value is too small!!!", x)
                                # message , value raising 
try:
     test_value(1)
except ValueTooHighError as e:
     print(e) # here get the exception given in raise
except ValueTooSmallError as e:
     print(e.message, e.value) 
     # here gets the expection with separate value


