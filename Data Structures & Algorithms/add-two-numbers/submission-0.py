# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1,n2 = "",""

        curr = l1

        while curr:
            n1 += str(curr.val)
            curr = curr.next
        
        curr = l2

        while curr:
            n2 += str(curr.val)
            curr = curr.next
        
        res = int(n1[::-1])+int(n2[::-1])
        res_lt = list(str(res))[::-1]
        # print(res_lt)
        curr = ListNode()
        new_head = curr
        ct = 0

        while ct != (len(res_lt) - 1):
            new_node = ListNode(res_lt[ct])
            curr.next = new_node
            curr = curr.next
            # print(curr.val)
            ct +=1

        new_node = ListNode(res_lt[ct])
        curr.next = new_node
        curr.next.next = None
        return new_head.next
