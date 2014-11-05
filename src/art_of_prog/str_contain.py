# -*- coding: utf-8 -*-
'''
假设这有一个各种字母组成的字符串 A，和另外一个字符串 B，字符串里 B的字母数相对少一些。
什么方法能最快的查出所有小字符串 B 里的字母在大字符串 A 里都有？
比如，如果是下面两个字符串：
String 1: ABCDEFGHLMNOPQRS
String 2: DCGSRQPO
答案是 true，所有在 string2 里的字母 string1 也都有。
如果是下面两个字符串：
String 1: ABCDEFGHLMNOPQRS
String 2: DCGSRQPZ
答案是 false，因为第二个字符串里的 Z 字母不在第一个字符串里。

@author: zhzh
'''
import unittest

# using a map
def str_contain(s1, s2):
    mp = {}
    for c in s2:
        mp[c] = True
    for ch in s1:
        if len(mp) == 0:
            return True
        if mp.has_key(ch):
            del mp[ch]
    if len(mp) == 0:
        return True
    else:
        return False

# using an array (only capital letters)
def str_contain_2(s1, s2):
    arr = [0] * 26
    base = ord('A')
    for c in s1:
        arr[ord(c) - base] = 1
    for c in s2:
        if arr[ord(c) - base] == 0:
            return False
    return True

class Test(unittest.TestCase):

    def testA(self):
        self.assertTrue(str_contain("ABCDEFGHLMNOPQRS", "DCGSRQPO"))
        self.assertFalse(str_contain("ABCDEFGHLMNOPQRS", "DCGSRQPZ"))
        self.assertTrue(str_contain("ABCDE", "ABCDE"))

    def testB(self):
        self.assertTrue(str_contain_2("ABCDEFGHLMNOPQRS", "DCGSRQPO"))
        self.assertFalse(str_contain_2("ABCDEFGHLMNOPQRS", "DCGSRQPZ"))
        self.assertTrue(str_contain_2("ABCDE", "ABCDE"))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()