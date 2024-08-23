from typing import List, Tuple, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr: ListNode = head
        tail: ListNode = ListNode()
        tail_head: ListNode = tail
        curr = head

        while True:
            if not curr.next:
                break
            if not curr.next.next:
                curr = curr.next
                break
            tmp = curr.next
            curr.next = curr.next.next
            tmp.next = None
            tail.next = tmp
            tail = tail.next
            curr = curr.next
        curr.next = tail_head.next

        return head
    
sol: Solution = Solution()

val:List[int] = [1,2,3,4,5]
head: ListNode = ListNode(val[0])
curr:ListNode = head

for item in val[1:]:
    curr.next = ListNode(item)
    curr = curr.next

print(sol.oddEvenList(head))

curr = head
for i in range(5):
    print(curr.val)
    curr = curr.next