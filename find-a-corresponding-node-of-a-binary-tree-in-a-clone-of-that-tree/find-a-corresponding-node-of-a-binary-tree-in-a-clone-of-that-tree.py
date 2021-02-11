# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        o_stack = []
        c_stack = []
        while original!=target:
            if original==None:
                if o_stack:
                    original=o_stack.pop()
                    cloned=c_stack.pop()
                continue
            o_stack.append(original.left)
            o_stack.append(original.right)
            c_stack.append(cloned.left)
            c_stack.append(cloned.right)
            
            cloned=c_stack.pop()
            original = o_stack.pop()
        return cloned
        