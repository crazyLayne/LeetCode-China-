class Solution:
    def doubleZero(self, nums):
        for i in range(len(nums)):
            if nums[i]==0 and i+1<len(nums) and nums[i+1]==0:
                return True
        return False
        
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k==0:return self.doubleZero(nums)
        L = len(nums)
        rem = [0]*L
        #构造初始的rem，从第一个元素开始
        sum = nums[0]%k
        rem = set()
        rem.add(sum)
        for i in range(1,L):
            sum = (sum+nums[i])%k
            if sum==0 or sum in rem:return True
            rem.add(sum)
        return False