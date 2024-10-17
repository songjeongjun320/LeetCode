from typing import List, Tuple, Optional

class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        tail: ListNode = ListNode()

        while head:
            print(head.val)
            if not head.next:
                break
            tmp = head
            head = head.next
            tmp.next = tail
            tail = tmp
        head.next = tail
        curr = head
        while True:
            if not curr.next.next:
                curr.next = None
                break
            curr = curr.next
        
        return head

tmp: List[int] = [1,2,3]
head: ListNode = ListNode(tmp[0])
curr = head
for item in tmp[1:]:
    curr.next = ListNode(item)
    curr = curr.next

sol: Solution = Solution()
head = sol.reverseList(head)


curr = head
while curr:
    print(curr.val)
    curr = curr.next







        