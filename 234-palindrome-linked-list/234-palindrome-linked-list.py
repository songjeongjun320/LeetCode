# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        storage = []
        while head:
            storage.append(head.val)
            head = head.next
        front = 0
        end = len(storage)-1
        while front < end:
            if storage[front] != storage[end]:
                return False
            front += 1
            end -= 1
        return True