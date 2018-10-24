class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.minCutCount(s, 0, len(s)-1)-1
    def minCutCount(self, s, L, R):     #返回最小的回文数量
        if L>R: return 0        #为空
        if L==R: return 1       #只有一个字符
        left = self.leftFind(s, L, R)
        right = self.rightFind(s, L, R)
        return min(self.minCutCount(s, left+1, R), self.minCutCount(s, L, right-1))+1
    def leftFind(self, s, L, R):        #固定左边界，从右向左寻找最大的回文
        for i in range(R,L,-1):
            if(self.isPalind(s[L:i+1])): return i
        return L

    def rightFind(self, s, L, R):        #固定右边界，从左往右寻找最大的回文
        for i in range(L, R):
            if(self.isPalind(s[i:R+1])): return i
        return R
    def isPalind(self, s):
        for i in range(len(s)//2):
            if s[i]!=s[len(s)-1-i]:return False
        return True
################################################################################################
    def minCut2(self, s):
        dp = [[0]*len(s) for _ in range(len(s))]        #dp[i][j]=1表示s[i:j+1]是回文
        cut = [len(s)]*(len(s)+1)           #cut[i]表示从i到结尾的最小回文个数，cut[i]=min(1+cut[j]) (i<j<len(s) and dp[i][j]=1)
        cut[-1]=0
        for i in range(len(s)-1,-1,-1):
            for j in range(i, len(s)):
                if i==j or (s[i]==s[j] and (dp[i+1][j-1]==1 or i+1==j)):
                    dp[i][j]=1
                    cut[i] = min(cut[i], cut[j+1]+1)
        return cut[0]-1

slt = Solution()
s = "eegiicgaeadbcfacfhifdbiehbgejcaeggcgbahfcajfhjjdgj"
# s = "bb"
print(slt.minCut2(s))
print(slt.minCut(s))