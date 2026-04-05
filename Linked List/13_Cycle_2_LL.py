# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Leetcode Q-142

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited={}
        temp=head
        while temp:
            if temp in visited:
                return temp
            visited[temp]=True
            temp=temp.next
        return None


# or 

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

            if slow==fast:
                break
        else:
            return None

        slow=head
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return slow