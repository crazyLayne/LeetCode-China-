# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def findMin(root, first):
            if root==None: return -1
            if root.val==first:
                left = findMin(root.left, first)
                right = findMin(root.right, first)
                if left==-1:return right
                if right==-1:return left
                else: return min(left, right)
            else:
                return root.val
        if root==None:return -1
        else: return findMin(root, root.val)