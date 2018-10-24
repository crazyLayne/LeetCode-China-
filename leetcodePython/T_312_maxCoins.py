class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.insert(0,1)
        nums.append(1)
        print(nums)
        dp = [[0]*len(nums) for _ in range(len(nums))]
        for i in range(n,0,-1):     #从n到1
            for j in range(i, n+1):     #从i到n
                for k in range(i, j+1):     #从i到j当中选择最后戳破的气球k
                    dp[i][j] = max(dp[i][j], dp[i][k-1] + nums[i-1]*nums[k]*nums[j+1] + dp[k+1][j])
        return dp[1][n]
nums = [3,1,5,8]
s = Solution()
print(s.maxCoins(nums))