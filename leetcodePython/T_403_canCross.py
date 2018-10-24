class Solution:
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        return self.DFS(stones, 0, 0)       #直接递归超时
    def DFS(self, stones, step, i):     #step表示上一步到达stones【i】的步伐，下一步可以走i+1(或i-1>0）步
        if i==len(stones)-1:return True
        st = i
        if step-1>0:
            while i<len(stones) and stones[i]<stones[st]+step-1: i+=1
            if i<len(stones) and stones[i]==stones[st]+step-1 and self.DFS(stones, step-1, i): return True
        if step>0:
            while i<len(stones) and stones[i]<stones[st]+step: i+=1
            if i<len(stones) and stones[i]==stones[st]+step and self.DFS(stones, step, i): return True
        while i<len(stones) and stones[i]<stones[st]+step+1: i+=1
        if i<len(stones) and stones[i]==stones[st]+step+1 and self.DFS(stones, step+1, i): return True
        return False
    
    def canCross2(self, stones):        #勉强通过
        #逆推计算每个节点可以到达最后终点的步数，步数不能超过当前索引i的最大步数i+1，最终若steps【0】中包含1则返回true
        steps = [None]*(len(stones)-1)
        print(steps)
        for i in range(len(stones)-2, -1, -1):  #逆推遍历
            cur = set()    #能走到终点的所有步数
            for j in range(i+1, min(len(stones)-1, 2*i+2)):
                dis = stones[j]-stones[i]
                if dis in steps[j] or dis-1 in steps[j] or dis+1 in steps[j]: cur.add(dis)
            #直接一步到达最后
            if i+1>=stones[-1]-stones[i]: cur.add(stones[-1]-stones[i])
            steps[i]=cur
        print(steps)
        if 1 in steps[0]:return True
        else: return False

    def canCross3(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        self.stones = stones
        self.len_s = len(stones)
        self.flag = 0
        if self.stones[1] != 1:
            return False
        return self.jump(1, 1)

    def jump(self, n, k):
        if self.flag:
            return False
        if n > 1 and self.stones[n+1] > ((n+1)*(n+2)/2):
            self.flag = 1
            return False
        now_count = self.stones[n] + k
        if self.stones[self.len_s-1] in [now_count-1, now_count, now_count+1]:
            return True
        if now_count-1 > self.stones[min(n+k+1, self.len_s-1)]:
            return False
        if now_count+1 < self.stones[n+1]:
            return False
        for i in range(min(n+k+1, self.len_s-1), n, -1):
            if self.stones[i] > now_count+1:
                continue
            elif self.stones[i] == now_count+1:
                if not self.jump(i, k+1):
                    continue
                else:
                    return True
            elif self.stones[i] == now_count:
                if not self.jump(i, k):
                    continue
                else:
                    return True
            elif self.stones[i] == now_count-1:
                return self.jump(i, k-1)
            else:
                return False
        return False
        
s = Solution()
stones=[0,1,3,5,6,8,12,17]
stones=[0,1,2,3,4,8,9,11]
stones=[0,1,3,6,10,15,21,28]
stones=[0,1,2,3,4,5,6,7]
print(s.canCross2(stones))
