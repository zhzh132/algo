# -*- coding: utf-8 -*-
'''
通过键盘输入一串小写字母(a~z)组成的字符串。请编写一个字符串压缩程序，将字符串中连续出席的重复字母进行压缩，并输出压缩后的字符串。
压缩规则：
    1、仅压缩连续重复出现的字符。比如字符串"abcbc"由于无连续重复字符，压缩后的字符串还是"abcbc"。
    2、压缩字段的格式为"字符重复的次数+字符"。例如：字符串"xxxyyyyyyz"压缩后就成为"3x6yz"。

stringZip(originalStr)

示例
    输入：“cccddecc”   输出：“3c2de2c”
    输入：“adef”     输出：“adef”
    输入：“pppppppp” 输出：“8p”

@author: zhzh
'''
import unittest
from cStringIO import StringIO

def stringZip(originalStr):
    if len(originalStr) < 1:
        return ""
    count = 1
    ch = originalStr[0]
    zipped = StringIO()
    idx = 1
    while idx < len(originalStr):
        if originalStr[idx] == ch:
            count += 1
        else:
            if count > 1:
                zipped.write(str(count))
                zipped.write(ch)
            else:
                zipped.write(ch)
            count = 1
            ch = originalStr[idx]
        idx += 1

    if count > 1:
        zipped.write(str(count))
        zipped.write(ch)
    else:
        zipped.write(ch)
    return zipped.getvalue()


class Test(unittest.TestCase):

    def testA(self):
        self.assertEqual(stringZip("cccddecc"), "3c2de2c")
        self.assertEqual(stringZip("adef"), "adef")
        self.assertEqual(stringZip("pppppppp"), "8p")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()