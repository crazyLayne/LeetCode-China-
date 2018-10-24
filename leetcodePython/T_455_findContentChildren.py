class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        j = 0
        res = 0
        for i in range(len(g)):
            while j<len(s) and g[i]>s[j]: j+=1
            if j>=len(s): break
            res += 1
            j+=1
        return res

