
class Solution:
    def halfSearch(self, intervals, i, L, R):
        mid = (L+R)//2
        if i>=intervals[mid][0] and i<=intervals[mid][1]: return mid
        elif i<intervals[mid][0]: return self.halfSearch(intervals,i,L,mid-1)
        else: return self.halfSearch(intervals, i, mid+1, R)
    
    
    def sumSubarrayMins(self, A):
        # 先排序
        iA = list(enumerate(A))
        iA = sorted(iA, key=lambda item:item[1])
        ids = [x[0] for x in iA]
        n = len(A)
        intervals = [[0, n-1]]  #区间范围
        intVAL = [n*(n+1)//2] #区间个数        
        res = 0
        for i in ids:
            #在剩余区间中，不包含i的区间个数
            L, R = 0, len(intervals)-1
            intID = self.halfSearch(intervals, i, L, R)
            interval = intervals[intID]
            intLen = interval[1]-interval[0]+1
            if i==interval[0] and i==interval[1]:
                cut = 1
                del intervals[intID]
                del intVAL[intID]
            elif i==interval[0]:
                cut = intLen
                intervals[intID][0] = i+1
                intVAL[intID] -= cut
            elif i==interval[1]:
                cut = intLen
                intervals[intID][1] = i-1
                intVAL[intID] -= cut
            else:
                ori = intVAL[intID]
                lenL = i-interval[0]
                lenR = interval[1]-i
                valL = (lenL+1)*lenL//2
                valR = (lenR+1)*lenR//2
                cut = ori - ( valL + valR)
                intervals.insert(intID, interval.copy())
                intervals[intID][1], intervals[intID+1][0] = i-1, i+1
                intVAL[intID] = valR
                intVAL.insert(intID, valL)
            # cut是减少的数目，即剩余区间中包含i的区间个数
            res += cut*A[i]
        return res%(10**9 + 7)
            

# A=[3,1,2,4]
# s = Solution()
# print(s.sumSubarrayMins(A))