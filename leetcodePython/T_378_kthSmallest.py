class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        l, r = matrix[0][0], matrix[-1][-1]
        while l<r:
            x = (l+r)//2
            count = 0
            for line in matrix:
                left, right = 0, n
                while left<right:       #找到第一个比x大的数字的下标，就是list中不大于x的数字的和
                    mid = (left+right)//2
                    val = line[mid]
                    if val<=x:
                        left = mid+1
                    else:
                        right = mid
                count+=left
                if count >= k or left==0:break
            if count>=k:
                r = x
            else:
                l = x+1
        return l

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
s = Solution()
print(s.kthSmallest(matrix, k))