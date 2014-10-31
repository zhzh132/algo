'''
Given a string S, find the longest palindromic substring in S.

http://leetcode.com/2011/11/longest-palindromic-substring-part-i.html

@author: zhzh
'''
import unittest

def longestPalindrome_lcs(s):
    t = s[::-1]   #reverse the string
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
                if maxLen < count and r - count + 1 == i:
                    maxLen = count
                    pos = i
                count = 0
                r += 1
        if maxLen < count and r - count + 1 == i:
            maxLen = count
            pos = i
    return s[pos:pos + maxLen]


def longestPalindrome_expand(s):
    start = -1
    maxLen = 0
    pos = 0

    while pos < len(s):
        #center is s[pos]
        step = 1
        while pos - step >= 0 and pos + step < len(s):
            if s[pos - step] != s[pos + step]:
                break
            step += 1
        step -= 1
        if step > 0:
            currLen = step * 2 + 1
            if currLen > maxLen:
                maxLen = currLen
                start = pos - step

        #center between s[pos] and s[pos+1]
        step = 1
        while pos - step + 1 >= 0 and pos + step < len(s):
            if s[pos - step + 1] != s[pos + step]:
                break
            step += 1
        step -= 1
        if step > 0:
            currLen = step * 2
            if currLen > maxLen:
                maxLen = currLen
                start = pos - step + 1

        pos += 1

    if start < 0:
        return ""
    else:
        return s[start : start + maxLen]

class Test(unittest.TestCase):
    def testExpA(self):
        s = "abcd"
        self.assertEquals(longestPalindrome_expand(s), "")

    def testExpB(self):
        s = "caba"
        self.assertEquals(longestPalindrome_expand(s), "aba")

    def testExpC(self):
        s = "abacdfgdcaba"
        self.assertEquals(longestPalindrome_expand(s), "aba")

    def testExpD(self):
        s = "cabbac"
        self.assertEquals(longestPalindrome_expand(s), "cabbac")

    def testExpE(self):
        s = ""
        self.assertEquals(longestPalindrome_expand(s), "")


#     def testA(self):
#         s = "caba"
#         self.assertEquals(longestPalindrome_lcs(s), "aba")
#
#     def testB(self):
#         s = "abacdfgdcaba"
#         self.assertEquals(longestPalindrome_lcs(s), "aba")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()