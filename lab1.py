#========================Vowels Removal==========================
#TO test any code in python  Test yourself
#add the following in an exteranl file:
#from folder import file_name
#import unittest
#To test any placeholder
#class test+anyname(unittest.TestCase):

#def test_problem1(self):
#    self.assertEqual(file_name('mobile'),'mbl')


#if __name__=='__main__':
#    unittest.main()



#================
enteredString=input("Please enter your string: ");
def remove_vowels(word):
    newstring=""
    for i in word:
        if i not in "aeiouAEIOU":
            newstring=newstring+i
    word=newstring
    return word

#if __name__=='__main__':   #Add this when calling any function
removedChars=remove_vowels(enteredString);
print(removedChars);
#===============Vowels removal=====================
def remove_vowel(text):
    vowels = ['a', 'e', 'o', 'i', 'u', 'A', 'E', 'O', 'U', 'I']
    result = ''
    for char in text:
        if char not in vowels:
            result += char
    return result
removedChar=remove_vowel(enteredString)
print(removedChar)
#=========================Character Locator=================================================
string2=input("Please enter your string: ");
charRquired=input("Please enter the character that you want to search: ");
def findCharOccurences(text, charSearch):
    return [i for i, letter in enumerate(text) if letter == charSearch]


foundIndicies=findCharOccurences(string2, charRquired)
print(foundIndicies);

#Very important======================number multiply====================================================
#We add x and z by 1 as index in the list begins from zero
number=int(input("please enter a number: "));
def numMul(input):
    outList=[]
    for x in range(input):
        inList=[]
        x+=1
        for z in range(x):
            z+=1
            inList.append(x*z)
        outList.append(inList);
    print(outList)

res=numMul(number);
print(res);

#result in the terminal
#>>> numMul(number);
#[[1], [2, 4], [3, 6, 9], [4, 8, 12, 16], [5, 10, 15, 20, 25]]
#----------------------number multiply(another way) using step in range function------------------------------------------------
#number=int(input("please enter a number: "));
#def numberDouble(num):
#    list1 = []
#    list2 = []
#    for i in range(1,num+1):
#        for k in range(i, (i*i)+1, i):
#            list1.append(k)
#        list2.append(list1)
#    return list2

#res=numberDouble(number);
#print(res);
#=========================Calculate Area(Just add it to a funtion)==================================================================
def calcArea():
    shape = ("triangle","square","rectangle","circle")
    constants = (3.14)
    start_up = input("Do you want to calculate a shape's area?: ")

    while True:
        startup = None
        if startup not in ("yes", "no"):
            if startup is not None:
                print("Sorry but I don't understand what your saying")
            startup = input("Do you want to calculate a shape's area?: ")
            if startup == "no":
                print("Goodbye then!")
                input("Press enter to close")
                break;

            if start_up == "yes":
               target_shape = ((input("Choose your shape: ")).lower());

               if target_shape == shape[0]:
                  h = float(input("give the height: "))
                  b = float(input("give the base length: "))
                  area_triangle = h * 1/2 * b
                  print("the area of the %s is %.2f" % (shape[0],area_triangle))


               if target_shape == shape[1]:
                  l = float(input("give the length: "))
                  area_square = l ** 2
                  print("the area of the %s is %.2f" % (shape[1],area_square))

               if target_shape == shape[2]:
                  l = float(input("give the length: "))
                  w = float(input("give the width: "))
                  area_rectangle = l * w
                  print("the area of the %s is %.2f" % (shape[2],area_rectangle))

               if target_shape == shape[3]:
                  r = float(input("give the radius: "))
                  pi = constants
                  area_circle = 2 * pi * r
                  print("the area of the %s is %.2f" %(shape[3],area_circle))

calcArea()

#===========================The Dictionary====================================================
#Not sorted list
listName=["Aya","Hossam","Islam"]
def sortFun(listName):
    names={}
    for i in range(len(listName)):
        #if names[i][0] in names[listName[i]]:
            names[listName[i][0]]=[listName[i]]
    print(names)
#--------------------Another way(basic way)---------------
#sorted list

def dictDisplay(names):
    names.sort()
    result={}
    for name in names:
        if name[0] in result:
            result[name[0]].append(name)
        else:   #No elements beggining with this letter
            result[name[0]]=[name]
    return result

l1=["Asmaa","Ibrahim","Aliaa"]
dictionaryRes=dictDisplay(l1);
print(dictionaryRes)
#The result is:  {'I': ['Ibrahim'], 'A': ['Aliaa', 'Asmaa']}

#===========================The Dictionary:another way====================================================
#Not accurate solution(Wrong) as it only keeps the last one entered in a list
#l1=["ahmed","fatma","ibrahim"]
#l2=[x[0] for x in l1]
#d=zip(l2,l1)
#print(dict(d))
#The result{'a': 'ahmed', 'i': 'ibrahim', 'f': 'fatma'}


#===============Mario Pyramid===================================================
number=input("Enter a number: ");
def printAstric(number):
    rang=range(int(number))
    for i in rang:
        print(" "*(int(number)-1-i)+"*"*(i+1))

printAstric(number)
#=======================Mario Pyramid(basic)========================================================
loops=input("Please enter your number to display its pyramid of *: ");
numberLoops=int(loops);
def printPyramid(numberIter):
    for i in range(numberIter):
        print(" " * (numberIter - i) + "*" * (i + 1));


printPyramid(numberLoops);
#========================================================================
if __name__ == '__main__':
    pass

#=====



























#==========================================================================
#def find_Character(word,char1):
#    charList=[]
#    for i in word:
#        if i ==char1:
            #charList.append(i);
            #i=i+1;
    #return charList


#find_Character(string2,charRquired);



 #enteredString=input("Please enter your string: ");
 #""">>> enteredString=input("Please enter your string: ");
#Please enter your string: Mobile
#>>> enteredString
#'Mobile'
#>>>
#"""
