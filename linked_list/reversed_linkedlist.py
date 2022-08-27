# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        helper = None
        header = head
        while (head is not None):
            nextt = head.next
            head.next = head
            helper = head
            head = nextt

        return helper