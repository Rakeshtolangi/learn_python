import class20

# module_name . member_name

# print(class20.x)
# print(class20.y)


# class20.f1()
# module_name.function_name


# from class20 import *
# print(y)
# f1()
# f2()

"""
code reuability
maintability is good
increase in internal performance
"""

# Module alacing
# import class20 as c 
# print(c.y)
# print(c.x)
"""
# print(class20.x) 
we can't use class20 becouse name is being change 
"""


# member alaicing

# from class20 import x

# print(x)

# from class20 import x as product_price

# print(product_price)
"""
print(x )
now we can't call member with x because name of meber is change to product_price
"""

# various possibilities of import 
"""
import module1
import module1,module2,module3
import module1 as m1
import module1 as m1, module2 as m2
from module1 import member1
from module1 import member1, member2,member2
from module1 import *
from module1 import member1 as m1
from module1 import member1 as m1, member2 as m2...

"""

# module naming conflict
# def f1():
#     print("hello from test module function one")

# print(__name__)

import class20
# print(class20.__name__)

class20.f1()
class20.f2()
class20.f3()
class20.f4()
