"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        stack = [root]
        order=[]
        while stack:
            current = stack.pop()
            if current == None:
                continue
            order.append(current.val)
            for x in reversed(current.children):
                stack.append(x)
        return order