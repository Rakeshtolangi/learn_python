# import class20

# from class20 import f1,y

# print(class20.y)

# class20.f1()


# this is member alacing 
# we can do module alacing also
# all of this to solve naming confilict


"""
# 1. 

from class20 import f1 as function1
from test import f1 as function2

function1()
function2()

"""



"""
# 2.

from class20 import *
from test import *

f1()


# f1() print the latest used function so test function will cass

"""



"""
# alieasing 
# 3.

from class20 import f1 as function1
from test import f1 as function2

function1()
function2()

"""



"""
# 4.

import class20 as c 
import test as t 

c.f1()
t.f1()

"""

"""
# any function added in runtime or while program is set to sleep will not be called while running.
from imp import reload
import imp
import class20
import time
from imp import reload

class20.add(10,20)
print("hello i am sleeping.")
time.sleep(30)
print("I am waking up.")

import class20
reload(class20)
class20.product(10,20)

"""



"""
# python added extra members for the ease of program
# 
import class20
print(dir(class20))

"""


"""
__doc__   hold the document file while calling help() funciton

"""


