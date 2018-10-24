# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class CBTInserter:
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.leaf = list()
        self.root = root
        q = [root]
        while len(q)>0:
            node = q[0]
            del q[0]
            if node.left==None or node.right==None: self.leaf.append(node)
            if node.left!=None: q.append(node.left)
            if node.right!=None: q.append(node.right)

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        firstLeaf = self.leaf[0]
        newLeaf = TreeNode(v)
        if firstLeaf.left == None:
            firstLeaf.left = newLeaf
        else:
            del self.leaf[0]
            firstLeaf.right = newLeaf
        self.leaf.append(newLeaf)
        return firstLeaf.val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()