class Solution:
    def uniqueLetterString(self, S):        # 暴力超时
        """
        :type S: str
        :rtype: int
        """
        res = 0
        for i in range(len(S)):
            appear = set()
            unique = set()
            for j in range(i, len(S)):
                if S[j] in appear:
                    if S[j] in unique:
                        unique.remove(S[j])
                else:
                    appear.add(S[j])
                    unique.add(S[j])
                res += len(unique)
        return res
    
    def uniqueLetterString2(self, S):
        d = {}          # 表示每个字符：对应出现的所有位置
        p = {}          # 表示每个字符：对应下次访问的位置
        res = 0
        layer = 0       # 以S[i]结尾的unique个数
        for i in range(len(S)):     # 构造d，p字典
            if S[i] in d.keys():
                d[S[i]].append(i)
            else:
                p[S[i]] = 0
                d[S[i]] = [i]
        for i in range(len(S)):     #新增一个元素后
            if p[S[i]] == 0:        #第一次出现
                layer += (i+1)
            elif p[S[i]] == 1:      #出现两次
                layer += (i - d[S[i]][p[S[i]]-1])   # 第一二次之间加1
                layer -= d[S[i]][p[S[i]]-1]+1
            else:
                layer += (i - d[S[i]][p[S[i]]-1])   # 第一二次之间加1
                layer -= (d[S[i]][p[S[i]]-1] - d[S[i]][p[S[i]]-2])  #第二三次之间减1
            p[S[i]] += 1
            res += layer              
        return res

s = Solution()
print(s.uniqueLetterString2("ABC"))