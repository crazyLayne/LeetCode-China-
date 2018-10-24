import collections
import numpy as np
class Solution:
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        def count(d, i, j, k):
            d2 = collections.Counter([i, j, k])
            res = 1
            for k,v in d2.items():
                if d[k]>=v: res *= np.math.factorial(d[k])//np.math.factorial(v)//np.math.factorial(d[k]-v)
                else: return 0
            return res
        d = collections.Counter(A)
        ks = sorted(list(d.keys()))
        res = 0
        for i in range(len(ks)):
            for j in range(i, len(ks)):
                if target-ks[i]-ks[j]<ks[j]: break
                if target-ks[i]-ks[j] in d.keys():
                    print(ks[i], ks[j], target-ks[i]-ks[j])
                    res += count(d, ks[i], ks[j], target-ks[i]-ks[j])
        return res%(10**9 + 7)
# A = [1,1,2,2,3,3,4,4,5,5]
# target = 8
A = [1,1,2,2,2,2]
target = 5
s = Solution()
print(s.threeSumMulti(A, target))