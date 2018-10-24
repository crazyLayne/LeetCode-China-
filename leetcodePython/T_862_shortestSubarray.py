class Solution(object):
    def shortestSubarray(self, A, K):       # O(n^2)超时
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        sum = [0]*len(A)
        minlen = len(A)+1
        for i in range(len(A)):
            sum[i] = sum[i-1]+A[i] if i>0 else A[i]
            if sum[i]>=K: minlen = min(minlen, i+1)
        for i in range(len(A)-1):
            for j in range(i+1,len(A)):
                if sum[j]-sum[i]>=K: minlen = min(minlen, j-i)
        return minlen if minlen<=len(A) else -1

    def shortestSubarray2(self, A, K):
        sum = [0]*len(A)
        minlen = len(A)+1
        for i in range(len(A)):
            sum[i] = sum[i-1]+A[i] if i>0 else A[i]
            if sum[i]>=K: minlen = min(minlen, i+1)
        q = []
        for i in range(len(A)):
            #遍历每个sum，sum(i,j)=sum[j]-sum[i],我们要使得sum（i,j)尽可能大，且j-i尽可能小
            val = sum[i]
            while len(q)>0 and sum[q[-1]]>val: del q[-1]     #删除q中比val大的值，保持q非递减
            q.append(i)
            if len(q)>0 and val - sum[q[0]] >= K:           #存在更新minlen的可能
                newst = self.halfSearch(sum, q, val, K, 0, len(q)-1)   #二分查找去找
                newlen = i - q[newst]
                minlen = min(minlen, newlen)
                del q[0:newst]      #删除
        return minlen if minlen<=len(A) else -1
    
    def halfSearch(self, sum, q, val, K, L, R):
        #寻找q中恰好使得val-q[i]>=k的值
        if L>R: return R
        mid = (L+R)//2
        if val - sum[q[mid]] >= K:
            return self.halfSearch(sum, q, val, K, mid+1, R)
        else: return self.halfSearch(sum, q, val, K, L, mid-1)

    def shortestSubarray3(self, A, K):
        sum = [0]
        minlen = len(A)+1
        for a in A:
            sum.append(sum[-1]+a)
        q = []
        for i,val in enumerate(sum):
            #遍历每个sum，sum(i,j)=sum[j]-sum[i],我们要使得sum（i,j)尽可能大，且j-i尽可能小
            while len(q)>0 and sum[q[-1]]>val: del q[-1]     #删除q中比val大的值，保持q非递减
            q.append(i)
            while len(q)>0 and val-sum[q[0]]>=K:
                minlen = min(minlen, i-q[0])
                del q[0]
        return minlen if minlen<=len(A) else -1
A = [17985,-36292,-23941,80618,20594,-6181,9181,65796,-25716,66593,-6873,34062,29878,852,-4767,-36415,11783,8085,-41063,-39940,74284,66272,82385,51634,-48550,9028,-30777,86509,44623,9413,-38369,-1822,46408,35217,72635,-16560,85373,52105,39477,3852,45974,-21593,15481,47280,73889,-42981,54978,95169,-19615,93133]
K = 387303
# A=[56,-21,56,35,-9]
# K=61
s = Solution()
print(s.shortestSubarray(A, K))
print(s.shortestSubarray2(A, K))
print(s.shortestSubarray3(A, K))