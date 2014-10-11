'''
Given a node from a cyclic linked list which has been sorted,
write a function to insert a value into the list such that it
remains a cyclic sorted list. The given node can be any single
node in the list.

http://leetcode.com/2011/08/insert-into-a-cyclic-sorted-list.html

@author: zhzh
'''
import unittest
from struct.node import LinkedNode

def insert(node, x):
    newNode = LinkedNode()
    newNode.value = x

    curr = node.next
    prev = node
    while curr != node:
        if curr.value >= x and prev.value <= x:
            break
        prev = curr
        curr = curr.next
    prev.next = newNode
    newNode.next = curr



class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testA(self):
        node = LinkedNode.generateLinkedList([1,3,5])
        curr = node
        while curr.next:
            curr = curr.next
        curr.next = node

        insert(node, 4)
        self.assertEqual(node.value, 1)
        self.assertEqual(node.next.value, 3)
        self.assertEqual(node.next.next.value, 4)
        self.assertEqual(node.next.next.next.value, 5)
        self.assertEqual(node.next.next.next.next.value, 1)

    def testB(self):
        node = LinkedNode.generateLinkedList([1,1,1])
        curr = node
        while curr.next:
            curr = curr.next
        curr.next = node

        insert(node, 4)
        self.assertEqual(node.value, 1)
        self.assertEqual(node.next.value, 1)
        self.assertEqual(node.next.next.value, 1)
        self.assertEqual(node.next.next.next.value, 4)
        self.assertEqual(node.next.next.next.next.value, 1)

    def testC(self):
        node = LinkedNode.generateLinkedList([1,3,5])
        curr = node
        while curr.next:
            curr = curr.next
        curr.next = node

        insert(node, 7)
        self.assertEqual(node.value, 1)
        self.assertEqual(node.next.value, 3)
        self.assertEqual(node.next.next.value, 5)
        self.assertEqual(node.next.next.next.value, 7)
        self.assertEqual(node.next.next.next.next.value, 1)

    def testD(self):
        node = LinkedNode.generateLinkedList([1,3,5])
        curr = node
        while curr.next:
            curr = curr.next
        curr.next = node

        insert(node, 0)
        self.assertEqual(node.value, 1)
        self.assertEqual(node.next.value, 3)
        self.assertEqual(node.next.next.value, 5)
        self.assertEqual(node.next.next.next.value, 0)
        self.assertEqual(node.next.next.next.next.value, 1)

    def testE(self):
        node = LinkedNode.generateLinkedList([1,1,1])
        curr = node
        while curr.next:
            curr = curr.next
        curr.next = node

        insert(node, 1)
        self.assertEqual(node.value, 1)
        self.assertEqual(node.next.value, 1)
        self.assertEqual(node.next.next.value, 1)
        self.assertEqual(node.next.next.next.value, 1)
        self.assertEqual(node.next.next.next.next.value, 1)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()