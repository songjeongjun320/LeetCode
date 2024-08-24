from typing import List, Tuple, Optional
class ListNode:
    def __init__(self, val:int=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        tmp: List[int] = []
        curr: ListNode = head
        
        while curr:
            tmp.append(curr.val)
            curr = curr.next
        
        if not tmp:
            return None
        if len(tmp) == 1:
            return tmp[0]

        result: int = tmp[0] + tmp[-1]

        l, r = 0, len(tmp) - 1
        while l <= r:
            s: int = tmp[l] + tmp[r]
            if l == r:
                s = tmp[l]
            if s > result:
                result = s 
            l += 1
            r -= 1

        return result
    

head_list: List[int] = [5,4,2,1]

head: ListNode = ListNode(head_list[0])
curr: ListNode = head
for item in head_list[1:]:
    curr.next = ListNode(item)
    curr = curr.next

sol: Solution = Solution()
print(sol.pairSum(head))
    

