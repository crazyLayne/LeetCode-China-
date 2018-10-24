class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:return len(nums)
        dp = [1]*len(nums)
        for i in range(1,len(nums)):
            maxval = 1
            for j in range(i):
                if nums[j]<nums[i]: maxval = max(maxval, dp[j]+1)
            dp[i] = maxval
        return max(dp)
    
    def lengthOfLIS2(self, nums):   #维系一个递增队列
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

            

s = Solution()
nums = [10,9,2,5,3,7,101,18]
nums = [10,9,2,5,3,4]
print(s.lengthOfLIS2(nums))