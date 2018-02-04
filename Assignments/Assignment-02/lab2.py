import webbrowser
from random import choice
random_page_generator = ['https://www.google.com.eg/','https://www.facebook.com/','https://drive.google.com/drive/','https://stackoverflow.com/','https://github.com/']
webbrowser.open(choice(random_page_generator), new=2)

#Note:When a space is included in the path of the url(random_page_generator) ,the redirection fails
#The result of the above code:
#>>> import webbrowser
#>>> from random import choice
#>>>random_page_generator = ['https://www.google.com.eg/','https://www.facebook.com/','https://drive.google.com/drive/','https://stackoverflow.com/','https://github.com/']
#>>>webbrowser.open(choice(random_page_generator), new=2)#True
#>>>

#==========================
#salary Property: must be 1000 or more.
#- email Property: must be valid.
#- healthRate Property: must be between 0 to 100.
#- There is moods class variable which is tuple of happy, tired and lazy

#- Person Class:
#- attributes (name, money, mood, healthRate).
#- methods (sleep, eat, buy).

class Person:

    def __init__(self,name,money,mood,healthRate):
        self.name=name
        self.money=money
        self.mood=mood
        self.__healthRate=healthRate

    @property
    def healthRate(self):
        return self.__healthRate

    @healthRate.setter
    def healthRate(self,healthRate):
        if healthRate > 0:
            self.__healthRate = healthRate
        if healthRate <= 100:
            self.__healthRate =0

    def sleep(self,hours):
        print("sleep method from person class")

#eat (meals): - Method in Person Class (3 meals  100% hth , 2 meals 75% , 1 meal  50%)
    def eat(self,meals):
        print("eat method from person class")

#buy (items): - Method in Person Class (1 item  decrease money 10 L.E)
    def buy(self,items):
        print("buy method from person class")



#=======================
#Employee Class (is a Person):
#- attributes (id , car, email, salary, distanceToWork)
#- methods (work, drive, refuel, send_mail)
#---------------------
#- salary Property: must be 1000 or more.
#- email Property: must be valid. #You need to add this and validate emails in pthon.
class Employee(Person):
    moods=("happy","tired","lazy")
    def __init__(self,id,car,email,salary,distanceToWork):
        self.id=id
        self.car=car
        self.email=email
        self.__salary=salary
        self.distanceToWork=distanceToWork

        @property
        def salary(self):
            return self.__salary

        @salary.setter
        def salary(self,salary):
            if salary > 0:
                self.__salary = salary
            if salary <= 0:
                self.__salary =0

        def sleep(self,hours):
            if hours == 8:
                mood=moods[0]
            elif hours < 7:
                mood=moods[1]
            elif hours > 7:
                mood=moods[2]
            return mood

        def eat(self,meals):
            if meals == 3:
                healthRate =100;
            elif meals == 2:
                healthRate=75;
            elif meals ==1:
                healthRate=50;
            return healthRate

        def buy(self,items):
            for i in items:
                money-=10
            return money

        def work(self,hours):
            if hours == 8:
                mood=moods[0]
            elif hours > 8:
                mood=moods[1]
            elif hours < 8:
                mood=moods[2]
            return mood

#id,car,email,salary,distanceToWork

emp=Employee(1,'fiat','asmaaali2017@gmail.com',10000,200)
print(emp.distanceToWork)





#- Office Class:
#- attributes (name, employees)
#-methods (get_all_employees, get_employee, hire, fire, calculate_lateness,
#deduct, reward)

class Office:
    employeesNum=0;
    def __init__(self,name,employees):
        self.name=name
        self.employees=employees

    def get_all_employees():
        pass

    def get_employee(empId):
        pass

    def hire(Employee):
        pass
    def fire(empId):
        pass
    def deduct(empId, deduction):
        pass

    def reward(empId, reward):
        pass
    def check_lateness(empId, moveHour):
        pass
    def calculate_lateness(targetHour , moveHour, distance, velocity):
        pass
    












       #eat (meals): - Method in Person Class (3 meals  100% hth , 2 meals 75% , 1 meal  50%)



       #buy (items): - Method in Person Class (1 item  decrease money 10 L.E)


       #- work (hours): - Method in Employee Class (8 hourshappy, >8 hours  tired,<8 hours  Lazy










#- Car Class:
#- attributes (name, fuelRate, velocity)
#-methods (run, stop)
#- Velocity Property: must be between 0 to 200.
#- Fuel Rate Property: must be between 0 to 100.
class Car:
    def __init__(self,name, fuelRate, velocity):
        self.name=name
        self.__fuelRate=fuelRate
        self.__velocity=velocity

        @property
        def fuelRate(self):
            return self.__fuelRate

        @fuelRate.setter
        def fuelRate(self,fuelRate):
            if fuelRate > 0:
                self.__fuelRate = fuelRate
            if fuelRate <= 100:
                self.__fuelRate =0

        @property
        def velocity(self):
            return self.__velocity

        @velocity.setter
        def velocity(self,velocity):
            if velocity > 0:
                self.__velocity = velocity
            if velocity <= 200:
                self.__velocity =0

        def drive(self,distance=120):
            run(velocity, distance)

        def refuel(self,gasAmount = 100):
            fuelRate +=gasAmount
            return fuelRate

        def run(self,velocity, distance):
            fuelRate -=80
            chgVelocity=input("please enter the velocity you want: ")
            changedVelocity=int(chgVelocity)
            stop()
            return fuelRate

        def stop():
            velocity(self,0)
            print("Stop now method")
            print("The remaining distance is: ")
            print(distance)
            return distance

#(name, fuelRate, velocity)
carObj=Car('fiat',250,220)
print(carObj.name)
