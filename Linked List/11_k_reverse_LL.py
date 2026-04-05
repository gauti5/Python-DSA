# Leetcode - 25

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count=0
        temp=head

        while temp:
            count+=1
            temp=temp.next
        
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy

        while count>=k:
            curr=prev.next
            next_node=curr.next

            for _ in range(1, k):
                curr.next=next_node.next
                next_node.next=prev.next
                prev.next=next_node
                next_node=curr.next
            prev=curr
            count-=k
        return dummy.next

