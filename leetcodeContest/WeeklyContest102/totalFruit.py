class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        if len(tree)<=2:return len(tree)
        res = 2
        F1, F2, L1, L2 = 0,0,0,0
        C1, C2 = -1,-1
        for i,v in enumerate(tree):
            if C1==-1:
                C1 = v
                F1 = L1 = i
            elif v==C1:
                L1 = i
            elif C2==-1:
                C2 = v
                F2 = L2 = i
            elif v==C2:
                L2 = i
            else:
                if L2>L1:       #保留F2的最后连续片段
                    F1, L1 = L1+1, L2
                    F2 = L2 = i
                    C1, C2 = C2, v
                else:           #保留F1的最后连续片段
                    F1 = L2+1
                    F2 = L2 = i
                    C2 = v
            res = max(res, i-F1+1)
        return res
tree = [1,0,1,4,1,4,1,2,3]
s = Solution()
print(s.totalFruit(tree))