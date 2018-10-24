import functools
class Solution:
    def cmp(self, x, y):
        if x[0]==y[0]:return y[1]-x[1]
        else: return x[0]-y[0]
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        # 按照行排序号，寻找最长递增子序列，注意不能重复
        nums = sorted(envelopes, key=functools.cmp_to_key(self.cmp))
        print(nums)
        return self.lengthOfLIS(nums)
    def lengthOfLIS(self, nums):   #维系一个递增队列
        if len(nums)<=1:return len(nums)
        q = []
        for n in nums:
            if len(q)==0 or n>q[-1]: q.append(n)
            else: q[self.halfSearch(q, n, 0, len(q)-1)] = n
        return len(q)
    
    def halfSearch(self, q, target, L, R):   #找第一个比target大的位置
        if L>R or L==R: return L
        mid = (L+R)//2
        if q[mid]>target: return self.halfSearch(q, target, L, mid)
        elif q[mid]==target: return mid
        else: return self.halfSearch(q, target, mid+1, R)
    
    def maxEnvelopes2(self, envelopes):             #超时
        if len(envelopes)<=1:return len(envelopes)
        nums = sorted(envelopes, key=lambda x:x[0])
        dp = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i][1]>nums[j][1] and nums[i][0]>nums[j][0]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

envelopes = [[5,4],[6,4],[6,7],[2,3]]
envelopes = [[4,5],[4,6],[6,7],[2,3],[1,1]]
envelopes = [[30,50],[12,2],[3,4],[12,15]]
envelopes = [[4,5],[4,6],[6,7],[2,3],[1,1],[1,1]]
envelopes = [[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]]
envelopes = [[5,4],[6,4],[6,7],[2,3]]
envelopes = [[15,8],[2,20],[2,14],[4,17],[8,19],[8,9],[5,7],[11,19],[8,11],[13,11],[2,13],[11,19],[8,11],[13,11],[2,13],[11,19],[16,1],[18,13],[14,17],[18,19]]
s = Solution()
print(s.maxEnvelopes(envelopes))