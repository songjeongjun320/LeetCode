from typing import List, Tuple, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt: int = 0
        curr: Optional[ListNode] = head
        while curr:
            cnt += 1
            curr = curr.next
        if cnt == 1 or cnt == 0:
            return ListNode()

        middle:int = cnt // 2

        curr = head
        i: int = 0
        while curr:
            if i == middle - 1:
                curr.next = curr.next.next
            curr = curr.next
            i += 1

        return head


value: List[int] = [1,2,3,4,5]

head:ListNode = ListNode(value[0])
curr:ListNode = head

for val in value[1:]:
    curr.next = ListNode(val)
    curr = curr.next


sol:Solution = Solution()
result:ListNode = sol.deleteMiddle(head)

# while result:
#     print(result.val)
#     result = result.next
