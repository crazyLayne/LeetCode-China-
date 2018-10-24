class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        lenth = len(nums)
        a = set()
        for i in range(lenth):
            if t==0:
                if nums[i] in a:
                    return True
            else:
                for atem in a:
                    if abs(nums[i]-atem)<=t:
                        return True
            a.add(nums[i])
            if len(a) == k+1:
                a.remove(nums[i-k])
        return False