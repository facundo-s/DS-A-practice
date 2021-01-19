# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        top=head
        following = head.next
        top.next=None
        while following!=None:
            temp = following
            following=following.next
            temp.next = top
            top=temp
        
        base = 1
        decimal=0
        while top!=None:
            decimal+=top.val*base
            base*=2
            top=top.next
        return decimal
