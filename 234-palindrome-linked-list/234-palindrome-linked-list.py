# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        li1 = []
        li2 = []
        head2 = head
        cnt = 1
        result = True
        
        while head2.next != None:
            li1.append(head2.val)
            head2 = head2.next
            cnt +=1 
        li1.append(head2.val)
        
        temp = li1[floor(cnt/2):]
        li1 = li1[:ceil(cnt/2)]
        
        for i in range(len(temp)-1, -1, -1):
            li2.append(temp[i])
        
        if li1 != li2:
            result = False
        return result