#Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(None)
        pointer = ans

        carry = 0
        summ = 0

        while (l1 != None or l2 != None):
            summ = carry
            if (l1 != None):
                summ += l1.val
                l1 = l1.next
            if (l2 != None):
                summ += l2.val
                l2 = l2.val

            carry = int(summ / 10)
            pointer.next = ListNode(summ % 10)

            pointer = pointer.next

        if (carry > 0):
            pointer.next = ListNode(carry)

        return ans.next