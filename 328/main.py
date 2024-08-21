from typing import List, Tuple, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt: int = 0
        while head:
            if cnt % 2 == 0:
                head.next = head.next.next
            cnt += 1
            head = head.next
        
        return head
    

sol: Solution = Solution()

val:List[int] = [1,2,3,4,5]
head: ListNode = ListNode(val[0])
curr:ListNode = head
for item in val[1:]:
    curr.next = ListNode(item)
    curr = curr.next

print(sol.oddEvenList(head))

