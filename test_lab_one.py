from lab1 import remove_vowels
from lab1 import remove_vowel
from lab1 import findCharOccurences
from lab1 import numMul
#from lab1 import numberDouble
from lab1 import dictDisplay
#from lab1 import task_five_enas
#from lab1 import task_five_haitham

import unittest

class TestAssignmentOne(unittest.TestCase):

    def remove_vowels(self):
        self.assertEqual(remove_vowels('mobile'), 'mbl')
        self.assertEqual(remove_vowels('MOBILE'), 'MBL')
        self.assertEqual(remove_vowels('MobIlE'), 'Mbl')

    def remove_vowel(self):
        self.assertEqual(remove_vowel('mobile'), 'mbl')
        self.assertEqual(remove_vowel('MOBILE'), 'MBL')
        self.assertEqual(remove_vowel('MobIlE'), 'Mbl')

    def findCharOccurences(self):
        self.assertEqual(findCharOccurences('This is javaScript','i'), [2,5,15])

    def numMul(self):
        self.assertEqual(numMul(3), [[1],[2,4],[3,6,9]])

    #def numberDouble(self):
    #    self.assertEqual(numberDouble(3), [[1],[2,4],[3,6,9]])

    def dictDisplay(self):
        self.assertEqual(dictDisplay(["Asmaa","Ibrahim","Aliaa"]),{'I': ['Ibrahim'], 'A': ['Aliaa', 'Asmaa']})
    # def test_task_five_enas(self):
    #     l1 = ["ahmed", "fatma", "ibrahim"]
    #     d1 = {'a':['ahmed'], 'f':['fatma'],'i':['ibrahim']}
    #     self.assertEqual(task_five_enas(l1), d1)


    #def test_task_five_haitham(self):
    #    l1 = ["ahmed", "fatma", "ibrahim"]
    #    d1 = {'a':['ahmed'], 'f':['fatma'],'i':['ibrahim']}
    #    self.assertEqual(task_five_enas(l1), d1)

if __name__ == '__main__':
    unittest.main()
