class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0: return -1
        if len(nums)==1: return 0
        l,r = 0, sum(nums)-nums[0]
        if l==r: return 0 
        for i in range(len(nums)-1):
            l += nums[i]
            r -= nums[i+1]
            if l==r: return i+1
        return -1

