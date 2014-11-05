# -*- coding:utf-8 -*-
'''
输入 n个整数，输出其中最小的 k个。

@author: zhzh
'''
import unittest

def topK(arr, k):
    ret = []
    for a in arr:
        if len(ret) < k:
            ret.append(a)
        else:
            # find the max item in ret
            maxId = 0
            for i in range(k):
                if ret[i] > ret[maxId]:
                    maxId = i
            if a < ret[maxId]:
                ret[maxId] = a
    return ret


class Test(unittest.TestCase):

    def testA(self):
        arr = [1,2,3,4,5,6,7,8]
        self.assertSequenceEqual(topK(arr, 4), [1,2,3,4])

    def testB(self):
        arr = [8,7,6,5,4,3,2,1]
        self.assertSequenceEqual(topK(arr, 4), [4,3,2,1])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()