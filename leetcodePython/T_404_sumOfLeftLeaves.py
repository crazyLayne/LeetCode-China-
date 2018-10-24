# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.recur(root)
        
    def recur(self, root):
        if root==None:return 0
        left = 0
        if root.left!=None:     #存在左子树且左子树是叶子节点
            if root.left.left==None and root.left.right==None:
                left = root.left.val
            else:
                left = self.recur(root.left)
        return left + self.recur(root.right)
            
