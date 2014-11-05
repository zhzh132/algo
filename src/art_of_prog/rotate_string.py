# -*- coding: utf-8 -*-
'''
定义字符串的左旋转操作：把字符串前面的若干个字符移动到字符串的尾部，如把
字符串 abcdef 左旋转 2位得到字符串 cdefab。请实现字符串左旋转的
函数， 要求对长度为n的字符串操作的时间复杂度为O(n)， 空间复杂度为O(1)。

@author: zhzh
'''
import unittest

def rotate_str(s, n):
    arr = list(s)
    if len(arr) == 0:
        return ""
    n = n % len(arr)
    arr = revert_arr(arr, 0, n - 1)
    arr = revert_arr(arr, n, len(arr) - 1)
    arr = revert_arr(arr, 0, len(arr) - 1)
    return "".join(arr)

def revert_arr(arr, frm, to):
    while frm < to:
        tmp = arr[frm]
        arr[frm] = arr[to]
        arr[to] = tmp
        frm += 1
        to -= 1
    return arr

class Test(unittest.TestCase):

    def testA(self):
        self.assertEqual(rotate_str("abcdef", 2), "cdefab")
        self.assertEqual(rotate_str("abcdef", 8), "cdefab")
        self.assertEqual(rotate_str("", 2), "")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()