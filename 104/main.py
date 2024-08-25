from typing import List, Tuple, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode])->int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        

root_list: List[int] = [3,9,20,None,None,15,7]

def build_tree(index: int, root_list: List[Optional[int]]) -> Optional[TreeNode]:
    if index >= len(root_list) or root_list[index] is None:
        return None

    node = TreeNode(root_list[index])
    node.left = build_tree(2 * index + 1, root_list)
    node.right = build_tree(2 * index + 2, root_list)
    
    return node

root:TreeNode = build_tree(0, root_list)
sol = Solution()
print(sol.maxDepth(root))

