'''
Merge Sort

@author: zhzh
'''
import unittest

def mergesort(arr):
    _mergesort(arr, 0, len(arr) - 1)
    return arr

def merge(arr, p, q, r):
    a1 = arr[p:q+1]
    a2 = arr[q+1:r+1]
    i = 0
    j = 0
    k = p
    while k < r:
        if a1[i] < a2[j]:
            arr[k] = a1[i]
            i += 1
        else:
            arr[k] = a2[j]
            j += 1
        k += 1
        if i == len(a1):
            while j < len(a2):
                arr[k] = a2[j]
                k += 1
                j += 1
        if j == len(a2):
            while i < len(a1):
                arr[k] = a1[i]
                k += 1
                i += 1

def _mergesort(arr, p, r):
    if p < r:
        q = (p + r) / 2
        _mergesort(arr, p, q)
        _mergesort(arr, q + 1, r)
        merge(arr, p, q, r)


class Test(unittest.TestCase):


    def testA(self):
        arr = [3,4,2,7,5,9,1,0,6,8]
        self.assertSequenceEqual(mergesort(arr), [0,1,2,3,4,5,6,7,8,9])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()