from typing import List, Tuple, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt: int = 0
        curr: ListNode = head
        tail: ListNode = head

        while curr:
            cnt += 1
            if not curr.next:
                tail = curr
            curr = curr.next


        curr = head
        i: int = 0
        while i < cnt:
            t = head
            print("i : ", i)
            for j in range(cnt):
                print(t.val)
                t = t.next


            print(tail.val)
            tail.next = curr.next
            tail = tail.next
            tail.next = None
            curr.next = curr.next.next
            cnt -= 1
            curr = curr.next
            i += 1

        return head
    
sol: Solution = Solution()

val:List[int] = [1,2,3,4,5]
head: ListNode = ListNode(val[0])
curr:ListNode = head

for item in val[1:]:
    curr.next = ListNode(item)
    curr = curr.next

print(sol.oddEvenList(head))