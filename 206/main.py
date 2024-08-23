from typing import List, Tuple, Optional

class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr: ListNode = head

        if not curr:
            return head
        
        tail: ListNode = curr
        curr = curr.next

        while curr:
            print(curr.val)
            tmp = curr
            curr = curr.next
            tmp.next = tail
            tmp = tail

        return head


tmp: List[int] = [1,2,3,4,5]
head: ListNode = ListNode(tmp[0])
curr = head
for item in tmp[1:]:
    curr.next = ListNode(item)
    curr = curr.next

sol: Solution = Solution()
print(sol.reverseList(head))


curr = head
while curr:
    print(curr.val)
    curr = curr.next







        