# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow = head.next
        if slow is None:
            return False
        fast = head.next.next
        if fast is None:
            return False
        while True:
            if slow.val == fast.val:
                return True
            if slow.next:
                slow = slow.next
            else:
                return False

            if fast.next and fast.next.next:
                fast =  fast.next.next
            else:
                return False