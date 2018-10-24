class Solution:
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def findMin(A, L, R):
            res = L
            for i in range(L,R+1):
                if A[i]<A[res]:
                    res = i
            return res
        # A【L,R】之间的sumSubarrayMins
        def rec(A, L, R):
            if L>R:return 0, 0
            if L==R:return 1, A[L]
            minI = findMin(A, L, R)
            Lcount, resL = rec(A, L, minI-1)
            Rcount, resR = rec(A, minI+1, R)
            n = R-L+1
            count = n*(n+1)//2
            return count, A[minI]*(count - Lcount - Rcount) + resL + resR
        _, res = rec(A, 0, len(A)-1)
        return res%(10**9+7)
    
    #改写成循环，从小到大排序后，依次遍历
    def sumSubarrayMins2(self, A):
        return 0


A = [3,1,2,4]
s = Solution()
print(s.sumSubarrayMins(A))