class Solution:
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        cur1 = cur2 = sum = 0
        m = -10**10     # m去找中间的正的最大的片段
        n = 10**10      # n去找中间的负的最厉害的片段
        for v in A:
            sum += v
            cur1 += v
            cur2 += v
            m = max(m, cur1)
            n = min(n, cur2)
            if cur1<0: cur1=0
            if cur2>0: cur2=0
        return max(m, -10**10 if sum-n==0 else sum-n)
A = [3,-2,2,-3]
# A = [-1,-2,-3]
S = Solution()
print(S.maxSubarraySumCircular(A))