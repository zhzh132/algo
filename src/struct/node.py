'''
Data Structure of Node

@author: zhzh
'''

class LinkedNode():
    def __init__(self):
        self.value = None
        self.next = None

    @staticmethod
    def generateLinkedList(values):
        nodes = []
        for v in values:
            node = LinkedNode()
            node.value = v
            nodes.append(node)
        i = 1
        while i < len(nodes):
            nodes[i-1].next = nodes[i]
            i += 1
        if len(nodes) > 0:
            return nodes[0]
