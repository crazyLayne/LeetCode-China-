import collections
class Solution:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        S = list(S)
        d = collections.Counter(S)
        L0, L1, R0, R1 = 0, 0, d['0'], d['1']
        res = R0
        for i in S:
            if i=='0':
                L0+=1
                R0-=1
            else:
                L1+=1
                R1-=1
            res = min(res, L1+R0)
        return res
        