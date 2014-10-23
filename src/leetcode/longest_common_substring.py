'''
Given two strings, S of length m and T of length n, find the longest strings which are substrings of both S and T.

http://en.wikipedia.org/wiki/Longest_common_substring_problem

@author: zhzh
'''
import unittest

def lcsubstr(s, t):
    maxLen = 0
    pos = 0
    for i in range(len(s)):
        count = 0
        r = 0
        while r < len(t) and i + count < len(s):
            if t[r] == s[i + count]:
                count += 1
                r += 1
            else:
                if maxLen < count:
                    maxLen = count
                    pos = i
                count = 0
                r += 1
        if maxLen < count:
            maxLen = count
            pos = i
    return s[pos:pos + maxLen]


class Test(unittest.TestCase):

    def testA(self):
        self.assertEquals(lcsubstr("ABAB", "BABA"), "ABA")
        self.assertEquals(lcsubstr("ABABC", "BABCA"), "BABC")
        self.assertEquals(lcsubstr("abc", "abc"), "abc")
        self.assertEquals(lcsubstr("bcd", "abcef"), "bc")
        self.assertEquals(lcsubstr("abc", "def"), "")
        self.assertEquals(lcsubstr("abacdfgdcaba", "abacdgfdcaba"), "abacd")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()