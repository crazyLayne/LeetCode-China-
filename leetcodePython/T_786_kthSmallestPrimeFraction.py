class Solution:
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        # A = [1, 2, 3, 5]
        # table = [1/2, 1/3, 1/5]
        #         [   , 2/3, 2/5]
        #         [   ,    , 3/5]
        # 从左往右递减，从下往上递减，数值范围在(0,1)之间
        N = len(A)
        l, r = 0, 1
        ri, rj = 0,0
        while l<r:
            m = (l+r)/2
            # 求比m小的数字个数count，并记录比m小的最大值maxf，当count=k时，maxf就是第k个值
            count = 0
            maxf = 0
            j = 1
            for i in range(N-1):
                while j<N and A[i]/A[j]>m:j+=1
                count += N-j
                if j==N:break       #从这一行开始已经找不到比m小的了，往下的都比这一行大，提前跳出
                if A[i]/A[j]>maxf:
                    maxf = A[i]/A[j]
                    ri = i
                    rj = j
            if count==K:
                break
            elif count>K:
                r = m
            else:
                l = m
        return [A[ri], A[rj]]

A = [1, 2, 3, 5]
K = 3
s = Solution()
print(s.kthSmallestPrimeFraction(A, K))