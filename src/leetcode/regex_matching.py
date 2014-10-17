# -*- coding: utf-8 -*-
"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true

http://leetcode.com/2011/09/regular-expression-matching.html

"""
import unittest

def isMatch(text, pattern):
    if len(pattern) == 0:
        return True
    if len(pattern) == 1:
        if pattern == ".":
            return len(text) == 1
        else:
            return text == pattern

    if len(pattern) > 1 and pattern[1] != "*":
        if pattern[0] == ".":
            return len(text) > 0 and isMatch(text[1:], pattern[1:])
        else:
            return (text[0] == pattern[0]) and isMatch(text[1:], pattern[1:])
    else:
        while (pattern[0] == text[0]) or (pattern[0] == "." and len(text) > 0):
            if isMatch(text, pattern[2:]):
                return True
            text = text[1:]
    return isMatch(text, pattern[2:])




class Test(unittest.TestCase):

    def testMatch1(self):
        self.assertFalse(isMatch("aa", "a"))

    def testMatch2(self):
        self.assertTrue(isMatch("aa", "aa"))

    def testMatch3(self):
        self.assertFalse(isMatch("aaa","aa"))

    def testMatch4(self):
        self.assertTrue(isMatch("aa", "a*"))

    def testMatch5(self):
        self.assertTrue(isMatch("aa", ".*"))

    def testMatch6(self):
        self.assertTrue(isMatch("ab", ".*"))

    def testMatch7(self):
        self.assertTrue(isMatch("aab", "c*a*b"))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()