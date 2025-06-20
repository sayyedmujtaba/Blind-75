# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def valid(node, left_bound, right_bound):
            if not node:
                return True
            if node.val <= left_bound or node.val >= right_bound:
                return False
            return (valid(node.left, left_bound, node.val) and 
                    valid(node.right, node.val, right_bound))
        
        return valid(root, float("-inf"), float("inf"))