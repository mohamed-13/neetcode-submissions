# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #Find Half
        slow,fast = head,head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        half = slow

        ## Reverse second Half
        second = slow.next
        slow.next = None
        prev,curr = None,second

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        ## Link first and second half alternatively
        first,second = head, prev
        ct = 0
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
            

        return 



