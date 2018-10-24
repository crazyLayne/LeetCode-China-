class Solution:
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def maxN(nums, k):
            if k==len(nums): return nums
            rem = len(nums)-k       #最多抛弃rem个数
            res = [None]*k
            cur = 0
            for n in nums:
                while rem>0 and cur>0 and res[cur-1]<n:
                    rem-=1
                    cur-=1
                if cur<k:
                    res[cur] = n
                    cur+=1
                else:
                    rem-=1
            return res
        def mergeMax(nums1, nums2):
            num = [None]*(len(nums1)+len(nums2))
            i = j = 0
            while i<len(nums1) and j<len(nums2):
                if nums1[i:]>nums2[j:]:
                    num[i+j] = nums1[i]
                    i+=1
                else:
                    num[i+j] = nums2[j]
                    j+=1
            while i<len(nums1):
                num[i+j] = nums1[i]
                i+=1
            while j<len(nums2):
                num[i+j] = nums2[j]
                j+=1
            return num
        if k>=len(nums1)+len(nums2): return mergeMax(nums1, nums2)
        maxV = [0]
        for a in range(min(k, len(nums1))+1):       #从nums1中取a个
            b = k-a
            if b>=0 and b<=len(nums2):              #从nums2中取b个
                arr1 = maxN(nums1, a)
                arr2 = maxN(nums2, b)
                maxV = max(maxV, mergeMax(arr1, arr2))
        return maxV




        