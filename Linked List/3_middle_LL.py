# find a middle value in a linked list

# leetcode - 876

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=0
        temp=head
        while temp:
            count+=1
            temp=temp.next
        mid_value=count//2
        temp=head
        for _ in range(mid_value):
            temp=temp.next
        return temp