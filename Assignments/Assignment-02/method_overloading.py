#Python supports overloading but in a Pythonic way. Here’s an example:
def add(instanceOf, *args):
    if instanceOf == 'int':
        result = 0
    if instanceOf == 'str':
        result = ''
    for i in args:
        result = result + i
    return result

res=add('int', 3,4,5)
print(res)
outStr=add('str', 'I',' am',' in', ' Python')
print(outStr)
#print add('int', 3,4,5)
#print add('str', 'I',' am',' in', ' Python')


#===============================================
#def add(a,b):
    #return a+b

#def add(a,b,c):
#    return a+b+c

#res=add(4,5)
#print(res)


#The result of the previous code
#>>> print add(4,5)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: add() missing 1 required positional argument: 'c'

#The reason is:“TypeError: add() takes exactly 3 arguments (2 given)”.
#This is because, Python understands the latest definition of method add() which takes only two arguments.


#======================================
class Human:
    def __init__(self,age):
        self.__age=age
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        if age > 0:
            self.__age = age
        if age <= 0:
            self.__age =0


man = Human(23)
print(man.age)

man.age = -25
print(man.age)

#The result of the code of this file until now :
#asmaa@asmaa-Satellite-C850-C007:~/Documents$ python3 method_overloading.py
#23
#0
#=================================We conlude that there is not method overloading in python======
#So there is not method overloading in python
