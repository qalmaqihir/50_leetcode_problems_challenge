# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def even_odd(self, head: ListNode) -> ListNode:
        if  not head:
            return head
        odd = head
        even =head.next
        evenlist=even
        while(even and evenlist):
            odd.next=even
            odd = odd.next

            even.next=odd.next
            even = even.next
        odd.next=evenlist
        return head
    