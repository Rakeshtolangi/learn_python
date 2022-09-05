"""
argv is used in console application
it takes input in console or terminal

"""
from sys import argv
# print(type(argv))


print("The number of command line arguments", len(argv))
print("The number of command line arguments",argv)
print("The numbero of command line argumets one by one ")
for x in argv:
    print(x)

