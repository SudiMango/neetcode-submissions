# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res: ListNode | None = None
        curr: ListNode | None = None
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                if res == None:
                    res = ListNode(val=list1.val)
                    curr = res
                else:
                    curr.next = ListNode(val=list1.val)
                    curr = curr.next
                list1 = list1.next
            else:
                if res == None:
                    res = ListNode(val=list2.val)
                    curr = res
                else:
                    curr.next = ListNode(val=list2.val)
                    curr = curr.next
                list2 = list2.next

        while list1 is not None:
            if res == None:
                res = ListNode(val=list1.val)
                curr = res
            else:
                curr.next = ListNode(val=list1.val)
                curr = curr.next
            list1 = list1.next

        while list2 is not None:
            if res == None:
                res = ListNode(val=list2.val)
                curr = res
            else:
                curr.next = ListNode(val=list2.val)
                curr = curr.next
            list2 = list2.next

        return res