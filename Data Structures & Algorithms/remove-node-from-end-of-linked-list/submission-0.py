# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        #traversing the LL to identify length
        curr = head
        total_len = 0
        while curr:
            total_len += 1
            curr = curr.next

        n_tr = total_len - n
        curr = head
        ct = 0

        if n_tr == 0:
            return head.next
        
        while curr.next and ct !=n_tr - 1:
            curr = curr.next
            ct +=1

        if curr.next is None:
            return head

        curr.next = curr.next.next

        return head









