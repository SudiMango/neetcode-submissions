# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_stack = []
        l2_stack = []
        res_stack = []

        while l1:
            l1_stack.append(l1.val)
            l1 = l1.next

        while l2:
            l2_stack.append(l2.val)
            l2 = l2.next

        l1_finished = ""
        l2_finished = ""
        while bool(l1_stack):
            l = str(l1_stack.pop())
            l1_finished += l

        while bool(l2_stack):
            r = str(l2_stack.pop())
            l2_finished += r

        l1_finished = int(l1_finished)
        l2_finished = int(l2_finished)

        res = l1_finished + l2_finished
        res = str(res)

        for c in res:
            res_stack.append(int(c))
        
        ret = None
        curr = None
        while bool(res_stack):
            if ret == None:
                ret = ListNode(val=res_stack.pop())
                curr = ret
            else:
                curr.next = ListNode(val=res_stack.pop())
                curr = curr.next

        return ret

        
