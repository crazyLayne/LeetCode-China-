class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        res = []
        pre, st, i = '@', -1, 0
        while i <len(S):
            if S[i]!=pre:
                if i-st>=3:
                    res.append([st, i-1])
                pre, st = S[i], i
            i += 1
        if i-st>=3:
            res.append([st, i-1])
        return res
s = Solution()
print(s.largeGroupPositions("aaa"))
