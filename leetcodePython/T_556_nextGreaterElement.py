class Solution:
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = list(str(n))
        i=0
        for i in range(len(s)-1, 0,-1):
            if s[i-1]<s[i]: break
        if s[i-1]>=s[i]:return -1    #全程非递减，没有更大的了
        mink = i
        for j in range(i+1, len(s)):
            if s[j]>s[i-1]: mink = j
            else: break
        s[i-1], s[mink] = s[mink], s[i-1]
        low = s[i:]
        s[i:] = sorted(low)
        res = int(''.join(s))
        return res if res< 2**31 else -1 
            
# s = Solution()
# print(s.nextGreaterElement(12443322))

