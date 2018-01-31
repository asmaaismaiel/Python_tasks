from lab1 import remove_vowels
from lab1 import remove_vowel
from lab1 import findCharOccurences
from lab1 import calcArea
#from lab1 import numberDouble
from lab1 import dictDisplay
from lab1 import numMul


import unittest

class TestAssignmentOne(unittest.TestCase):

    def test_remove_vowels(self):
        self.assertEqual(remove_vowels('mobile'), 'mbl')
        self.assertEqual(remove_vowels('MOBILE'), 'MBL')
        self.assertEqual(remove_vowels('MobIlE'), 'Mbl')

    #def test_remove_vowel(self):
    #    self.assertEqual(remove_vowel('mobile'), 'mbl')
    #    self.assertEqual(remove_vowel('MOBILE'), 'MBL')
    #    self.assertEqual(remove_vowel('MobIlE'), 'Mbl')

    def test_findCharOccurences(self):
        self.assertEqual(findCharOccurences('This is javaScript','i'), [2,5,15])

    def test_numMul(self):
        self.assertEqual(numMul(3), [[1],[2,4],[3,6,9]])

    #def test_numberDouble(self):
        #self.assertEqual(numberDouble(3), [[1],[2,4],[3,6,9]])

    def test_calcArea(self):
        print("Calling calcArea() function")

    def test_dictDisplay(self):
        self.assertEqual(dictDisplay(["Asmaa","Ibrahim","Aliaa"]),{'I': ['Ibrahim'], 'A': ['Aliaa', 'Asmaa']})


    def test_printPyramid(self):
        print("Printing a pyramid of *")





if __name__ == '__main__':
    unittest.main()
