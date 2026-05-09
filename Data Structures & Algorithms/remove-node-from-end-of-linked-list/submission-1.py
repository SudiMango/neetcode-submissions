# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        curr = head
        displaced = head
        traverse_count = 1

        while traverse_count < n:
            displaced = displaced.next
            traverse_count += 1
        
        prev = None
        while displaced and displaced.next:
            displaced = displaced.next
            prev = curr
            curr = curr.next

        if prev:
            prev.next = curr.next
        else:
            head = curr.next
            curr.next = None

        return head
            

