'''
Bubble Sort

@author: zhzh
'''
import unittest

def bubblesort(arr):
    i = 0
    while i < len(arr):
        j = len(arr) - 1
        while j > i:
            if arr[j] < arr[j - 1]:
                tmp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = tmp
            j -= 1
        i += 1
    return arr

class Test(unittest.TestCase):


    def testA(self):
        arr = [3,4,2,7,5,9,1,0,6,8]
        self.assertSequenceEqual(bubblesort(arr), [0,1,2,3,4,5,6,7,8,9])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()