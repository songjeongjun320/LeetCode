from typing import List, Tuple, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 != root2:
            return False
        return self.leafSimilar(root1.left, root2.right)


    def build_tree(self, index:int, root_list: List[int]) -> TreeNode:
        if index >= len(root_list) or root_list is None:
            return None

        root = TreeNode(root_list[index])
        root.left = self.build_tree(index * 2 + 1, root_list)
        root.right = self.build_tree(index * 2 + 2, root_list)

        return root

root1_list: List[int] = [3,5,1,6,2,9,8,None,None,7,4]
root2_list: List[int] = [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]

sol:Solution = Solution()
root1: TreeNode = sol.build_tree(0, root1_list)
root2: TreeNode = sol. build_tree(0, root2_list)
print(sol.leafSimilar(root1, root2))



