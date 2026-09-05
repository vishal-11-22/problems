# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(node,val):
            if node.val<val:
                if node.right is None:
                    node.right=TreeNode(val)
                else:
                    search(node.right,val)
            else:
                if node.left is None:
                    node.left=TreeNode(val)
                else:
                    search(node.left,val)
        if root is None:
            return TreeNode(val)
        search(root,val)
        return root
        