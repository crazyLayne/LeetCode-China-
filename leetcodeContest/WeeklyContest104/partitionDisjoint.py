class Solution:
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A)<=1:return len(A)
        l2r = [[-1,-1]]         #从左到右升序
        r2l = [[10**6+1,len(A)]]        #从右到左降序
        for i in range(len(A)):
            if A[i]>l2r[-1][0]:
                l2r.append([A[i],i])
        for i in range(len(A)-1, -1, -1):
            if A[i]<r2l[0][0]:
                r2l.insert(0, [A[i],i])
        del l2r[0], r2l[-1]
        if l2r[0][0]==r2l[0][0]: return 1
        i,j=0,0
        # j先找到r2l[j][0]>=l2r[i][0], 保证A[r2l[j][1]:]>=A[:l2r[i][1]]
        # 中间A[l2r[i][1]:r2l[j][1]]无法确认
        # 我们再去挪动i，判断上述区间内的值满足条件，满足则直接return
        # 不满足，则我们继续挪动j，使得right继续增大
        while i<len(l2r) and j<len(r2l):
            while j<len(r2l) and r2l[j][0]<l2r[i][0]: j+=1
            while i<len(l2r) and l2r[i][1]<r2l[j-1][1]:
                if l2r[i][0]>r2l[j][0]: break
                i+=1
            if l2r[i][1]>=r2l[j-1][1]: return r2l[j-1][1]+1
