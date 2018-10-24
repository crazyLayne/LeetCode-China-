class Solution:
    def countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """
        if len(S)<=1: return len(S)
        dp = [[0]*len(S) for _ in range(len(S))]
        for i in range(len(S)-1, -1, -1):
            for j in range(i, len(S)):
                if i==j: dp[i][j]=1
                elif S[i]==S[j]:
                    l, r = i+1, j-1
                    while l<j and S[l]!=S[i]: l+=1
                    while r>i and S[r]!=S[i]: r-=1
                    if l==r: dp[i][j] = 2*dp[i+1][j-1] + 1
                    elif l<r: dp[i][j] = 2*dp[i+1][j-1] - dp[l+1][r-1]
                    else: dp[i][j] = 2*dp[i+1][j-1] + 2
                else:
                    dp[i][j] = dp[i+1][j]+dp[i][j-1]-dp[i+1][j-1]
        print(dp)
        return dp[0][-1]%(10**9+7)
S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
# S = 'bccb'
slt = Solution()
print(slt.countPalindromicSubsequences(S))



        

        