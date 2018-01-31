class Mammal:
    def __init__(self):
        print ("From Mammal class")
    def eat(self):
        print("Mammal eats")

class Human(Mammal):
    def __init__(self):
        print ("From Human class")


class Employee(Human,Mammal):
        def __init__(self):
            super(Employee,self).__init__()
            print("That's multiple inheritance in pyhton");


emp=Employee()
emp.eat()
#=======================The result of the previous code===========================
#>>> class Mammal:
#...     def __init__(self):
#...         print ("From Mammal class")
#...     def eat(self):
#...         print("Mammal eats")
#...
#>>> class Human(Mammal):
#...     def __init__(self):
#...         print ("From Human class")
#...
#>>> class Employee(Human,Mammal):
#...         def __init__(self):
#...             super(Employee,self).__init__()
#...             print("That's multiple inheritance in pyhton");
#...
#>>> emp=Employee()
#From Human class
#That's multiple inheritance in pyhton
#>>> emp.eat()
#Mammal eats
#>>>

#============================The result of the previous code================
class Mammal:
    def __init__(self):
        print ("From Mammal class")
    def eat(self):
        print("Mammal eats")

class Human(Mammal):
    def __init__(self):
        print ("From Human class")
    def eat(self):
        print("Human eats")

class Employee(Human,Mammal):
        def __init__(self):
            super(Employee,self).__init__()
            print("That's multiple inheritance in pyhton");


emp=Employee()
emp.eat()
#============The result of the previous code===============
#>>> class Mammal:
#...     def __init__(self):
#...         print ("From Mammal class")
#...     def eat(self):
#...         print("Mammal eats")
#...
#>>> class Human(Mammal):
#...     def __init__(self):
#...         print ("From Human class")
#...     def eat(self):
#...         print("Human eats")
#...
#>>> class Employee(Human,Mammal):
#...         def __init__(self):
#...             super(Employee,self).__init__()
#...             print("That's multiple inheritance in pyhton");
#...
#>>>
#>>> emp=Employee()
#From Human class
#That's multiple inheritance in pyhton
#>>> emp.eat()
#Human eats

#===================================================
class Mammal:
    def __init__(self):
        print ("From Mammal class")
    def eat(self):
        print("Mammal eats")

class Human(Mammal):
    def __init__(self):
        print ("From Human class")
    def eat(self):
        print("Human eats")

class Employee(Human):
        def __init__(self):
            super(Employee,self).__init__()
            print("That's multiple inheritance in pyhton");


emp=Employee()
emp.eat()
#===========================The result of the previous code========
##>>> class Mammal:
#...     def __init__(self):
#...         print ("From Mammal class")
#...     def eat(self):
#...         print("Mammal eats")
#...
#>>> class Human(Mammal):
#...     def __init__(self):
#...         print ("From Human class")
#...     def eat(self):
#...         print("Human eats")
#...
#>>> class Employee(Human):
#...         def __init__(self):
#...             super(Employee,self).__init__()
#...             print("That's multiple inheritance in pyhton");
#...
#>>>
#>>> emp=Employee()
#From Human class
#That's multiple inheritance in pyhton
#>>> emp.eat()
#Human eats
#============================Another example====================
class Mammal:
    def __init__(self):
        print ("From Mammal class")
    def eat(self):
        print("Mammal eats")

class Human(Mammal):
    def __init__(self):
        print ("From Human class")


class Employee(Human):
        def __init__(self):
            super(Employee,self).__init__()
            print("That's multiple inheritance in pyhton");


emp=Employee()
emp.eat()
#===========================The result of the previous code========
#>>> class Mammal:
#...     def __init__(self):
#...         print ("From Mammal class")
#...     def eat(self):
#...         print("Mammal eats")
#...
#>>> class Human(Mammal):
#...     def __init__(self):
#...         print ("From Human class")
#...
#>>> class Employee(Human):
#...         def __init__(self):
#...             super(Employee,self).__init__()
#...             print("That's multiple inheritance in pyhton");
#...
#>>> emp=Employee()
#From Human class
#That's multiple inheritance in pyhton
#>>> emp.eat()
#Mammal eats
#==========================An example to produe an error(AttributeError)========================================================
#class Mammal:
#    def __init__(self):
#        print ("From Mammal class")


#class Human(Mammal):
#    def __init__(self):
#        print ("From Human class")


#class Employee(Human):
#        def __init__(self):
#            super(Employee,self).__init__()
#            print("That's multiple inheritance in pyhton");


#emp=Employee()
#emp.eat()
#=============The result of the previous code=============
#>>> class Mammal:
#...     def __init__(self):
#...         print ("From Mammal class")
#...
#>>> class Human(Mammal):
#...     def __init__(self):
#...         print ("From Human class")
#...
#>>> class Employee(Human):
#...         def __init__(self):
#...             super(Employee,self).__init__()
#...             print("That's multiple inheritance in pyhton");
#...
#>>> emp=Employee()
#From Human class
#That's multiple inheritance in pyhton
#>>> emp.eat()
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#AttributeError: 'Employee' object has no attribute 'eat'
#>>>




#============================================================
class First(object):
    def __init__(self):
        print "first"

class Second(First):
    def __init__(self):
        print "second"

class Third(First):
    def __init__(self):
        print "third"

class Fourth(Second, Third):
    def __init__(self):
        super(Fourth, self).__init__()
        print "that's it"

fourthObj=Fourth()


#=====================The result:===========================
#>>> class First(object):
#...     def __init__(self):
#...         print("first")
#...
#>>> class Second(First):
#...     def __init__(self):
#...         print("second")
#...
#>>> class Third(First):
#...     def __init__(self):
#...         print("third")
#...
#>>> class Fourth(Second, Third):
#...     def __init__(self):
#...         super(Fourth, self).__init__()
#...         print ("that's it")
#...
#>>> Fourth.__mro__
#(<class '__main__.Fourth'>, <class '__main__.Second'>, <class '__main__.Third'>, <class '__main__.First'>, <class 'object'>)
#>>> fourthObj=Fourth()
#second
#that's it
#>>>
