# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # get length
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        if length == 1 or length == 2:
            return 
        
        # find start of second list
        curr = head
        last = head
        displacement = length // 2
        while displacement != 0:
            last = last.next
            displacement -= 1

        while last.next:
            curr = curr.next
            last = last.next
        temp = curr.next
        curr.next = None
        curr = temp

        # reverse second list
        prev = curr
        if curr.next != None:
            curr = curr.next
            prev.next = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                if temp == None:
                    break
                else:
                    curr = temp

        # while head:
        #     print(head.val)
        #     head = head.next
        # print(" ")
        # while curr:
        #     print(curr.val)
        #     curr = curr.next

        # do final calc
        first = head
        second = curr
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2


