# Last updated: 4/4/2025, 6:37:27 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        def dfs(node):
            if not node:
                return(None,0)

            left_node, left_height = dfs(node.left)
            right_node, right_height = dfs(node.right)

            if left_height == right_height:
                return node, left_height + 1
            elif left_height > right_height:
                return left_node, left_height + 1
            else:
                return right_node, 1 + right_height

        node, _ = dfs(root)
        return node