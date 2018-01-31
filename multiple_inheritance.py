class A:
    def __init__(self):
        print("Clasa A constructor")
    def say(self):
        print("I'm class A")


class B:
    def __init__(self):
        print("Clasa B constructor")
    def say(self):
        print("I'm class B")


class C(B,A):
    def __init__(self):
        B.__init__(self)
        A.__init__(self)



cObj=C()
cObj.say()
#=================Without using super()======================================
