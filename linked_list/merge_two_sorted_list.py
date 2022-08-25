class ListNode:
    def __int__(self, val=0):
        self.val=val
        self.next = None


def merge_two_sorted_list(l1:ListNode,l2:ListNode)-> ListNode:
    cur = ListNode(0)
    ans = cur

    while (l1 and l2):
        if l1.val > l2.val:
            cur.next = l2
            l2 = l2.next
        else:
            cur.next = l1.val
            l1 = l1.next
        cur = cur.next
    while (l1):
        cur.next = l1
        l1 = l1.next
        cur = cur.next
    while (l2):
        cur.next = l2
        l2 = l2.next
        cur = cur.next
    return ans.next

