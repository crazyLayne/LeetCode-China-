class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i,v in enumerate(nums):
            if v in d and v*2 == target:
                return [d[v], i]
            else:
                d[v] = i
        for i in range(len(nums)):
            if target-nums[i]!=nums[i] and target-nums[i] in d:
                return [d[nums[i]], d[target-nums[i]]]


nums = [3, 2, 4]
target = 6
s = Solution()
print(s.twoSum(nums, target))
        
        