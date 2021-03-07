# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        list1_head = list1
        while a>1:
            list1=list1.next 
            a-=1
            b-=1
        #iteration stops at list1[a-1]
        
        list1_insertion = list1
        while b>-1:
            list1=list1.next
            b-=1
        #iteration stops at list1[b+1]
        
        #case: [0,1,2,3,4] a=1, b=2
        
        list1_continuation = list1
        
        list1_insertion.next = list2
        
        while list2.next != None:
            list2 = list2.next 
        # iteration ends at the last node of list2
        
        list2.next = list1_continuation
        
        # Runtime (b+m) where m is length of list2
        return list1_head
        
            
        
        
        
        