# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head2 = head
        cnt = 0
        while head2 != None:
            head2 = head2.next
            cnt += 1
        cnt = floor(cnt/2)
        for i in range(cnt):
            head = head.next
        return head