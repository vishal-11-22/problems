# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global_sum=float('-inf')
        if root.left is None and root.right is None:
            return root.val
        def path(c_sum,node):
            nonlocal global_sum
            if node is None:
                return 0
            # if node.left is None and node.right is None:
            #     return node.val
            
            left_sum=max(0,path(c_sum,node.left))
            right_sum=max(0,path(c_sum,node.right))
            cur_sum=left_sum+node.val+right_sum
            global_sum=max(global_sum,cur_sum)
            return node.val+max(left_sum,right_sum)
        path(0,root)
        return global_sum