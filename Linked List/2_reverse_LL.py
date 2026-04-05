
# Reverse the Linked List

# Leetcode - 206

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        temp=head
        while temp:
            next_node=temp.next
            temp.next=prev
            prev=temp
            temp=next_node
        return prev