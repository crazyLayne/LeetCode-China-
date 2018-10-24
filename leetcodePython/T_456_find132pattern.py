class Solution:
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l32 = []
        n2 = -2**32
        for n in nums[::-1]:
            if n < n2:return True
            else: 
                while len(l32)>0 and n>l32[-1]:     #维持一个非递增的栈
                    n2 = l32[-1]
                    del l32[-1]
            l32.append(n)
        return False
nums = [-2,1,2,-2,1,2]
s = Solution()
print(s.find132pattern(nums))            