import collections
class Solution:
    def threeEqualParts(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        def isSame(A, st1, ed1, st2, ed2):      #判断两个区间是否相同
            if st1 == -1: return st2 == -1
            if st2 == -1 or ed1-st1!= ed2-st2: return False
            for k in range(ed1-st1):
                if A[st1+k] != A[st2+k]:
                    return False
            return True
        def Less(A, st1, ed1, st2, ed2):        #判断前面区间是否小于后面区间
            if st1==-1: return st2!=-1
            if st2==-1: return False
            if ed1-st1 > ed2-st2: return False
            elif ed1-st1 < ed2-st2: return True
            else:
                for k in range(ed1-st1):
                    if A[st1+k]!=A[st2+k]:
                        if A[st1+k]==1: return False
                        else: return True
                return False

        d = collections.Counter(A)
        if d[1]%3!=0: return [-1, -1]
        i, j = 0, 2        #区间划分为[0,i],[i+1,j-1],[j,-1]
        L1 = M1 = R1 = -1   #表示第一个每个区间第一个1的下标，用于初步判断两个数是否相同，-1表示区间取值为零
        if A[0] == 1: L1 = 0
        if A[1] == 1: M1 = 1
        for k in range(j, len(A)):
            if A[k]==1:
                R1 = k
                break
        if isSame(A, L1, i+1, M1, j) and isSame(A, M1, j, R1, len(A)): return [i,j]
        while Less(A, M1, j, R1, len(A)) or Less(A, L1, i+1, R1, len(A)):   #如果左区间和中区间都大于等于右区间，则无解
            while Less(A, M1, j, R1, len(A)):  #保证中间区间大于等于右区间
                if M1==-1 and A[j]==1: M1=j #更新M1的下标
                if A[j]==1:         #找到下一个1
                    R1 += 1
                    while R1<len(A) and A[R1]!=1: R1+=1
                    if R1==len(A): R1 = -1  #右区间已经不存在1了
                j+=1
            if isSame(A, L1, i+1, M1, j) and isSame(A, M1, j, R1, len(A)): return [i,j]
            while Less(A, L1, i+1, M1, j):  #保证左区间大于等于中区间
                if L1==-1 and A[i+1]==1: L1=i+1 #更新L1的下标
                if A[i+1]==1:         #找到下一个1
                    M1 += 1
                    while M1<j and A[M1]!=1: M1+=1
                    if M1==j: M1 = -1  #中间区间已经不存在1了
                i+=1
            if isSame(A, L1, i+1, M1, j) and isSame(A, M1, j, R1, len(A)): return [i,j]
        return [-1, -1]

A = [0,1,0,1,1]
# A = [1,1,0,1,1]
s = Solution()
print(s.threeEqualParts(A))