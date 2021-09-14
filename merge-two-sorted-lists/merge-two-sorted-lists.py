# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1==None:
            return l2
        if l2==None:
            return l1
        if l1.val<l2.val:
            head=l1
            l1=l1.next
        else:
            head=l2
            l2=l2.next
        
        last = head
        while (l1!=None):
            # print("head: ")
            # print(head)
            # print("last: ")
            # print(last)
            # print("l1: ")
            # print(l1)
            # print("l2: ")
            # print(l2)
            # print(head, last, l1, l2)
            if l2==None:
                last.next=l1
                break
            if l1.val<l2.val:
                last.next=l1
                l1=l1.next
            else:
                last.next=l2
                l2=l2.next
            last=last.next
        
        #what happens if last is pointing to l1 and l1 is none
        if (l1==None and l2!=None):
            last.next = l2
        
        
        return head
        