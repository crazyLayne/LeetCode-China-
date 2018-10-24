class Solution:
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        # 起始位置猫：2 老鼠：1 洞：0；老鼠先走
        # 如果猫和老鼠占据相同的结点，猫获胜。
        # 如果老鼠躲入洞里，老鼠获胜。
        # 如果某一位置重复出现（即，玩家们的位置和移动顺序都与上一个回合相同），游戏平局
        # 状态表示（Pc， Pm, turn）有三元组猫的位置，老鼠的位置和下一步谁走组成 turn=0 老鼠走； turn=1 猫走
        # 根据最终确定的状态去推初始状态
        n = len(graph)
        st = [[[0]*2 for _ in range(n)] for _ in range(n)]
        # 注意猫无法进洞，即st[0][j][t]不存在
        # target = [2, 1, 0]
        # 老鼠赢遍历，老鼠赢只能是下一步是猫走
        q = []
        for i in range(1, n):
            q.append([i, 0, 1])
        while len(q)>0:
            [i, j, t] = q[0]        #取出一个老鼠必赢的状态，逆推
            del q[0]
            if st[i][j][t]==0:      #考虑是否访问过了
                st[i][j][t]==1
                if i==1 and j==2 and t==0: return 1
                if t==0:            #这一步是老鼠走，则上一步是猫走,考虑上一步猫能走到i的所有情况
                    for k in graph[i]:
                        q.append([k, j, 1])
                else:
                    for k in graph[j]:
                        q.append([i, k, 0])
        # 猫赢，上一步猫走，且能走到和老鼠同一个位置，除了0
        for i in range(1, n):
            q.append([i, i, 0])
        while len(q)>0:
            [i, j, t] = q[0]        #取出一个猫必赢的状态，逆推
            del q[0]
            if st[i][j][t]==0:      #考虑是否访问过了
                st[i][j][t]==2
                if i==1 and j==2 and t==0: return 2
                if t==0:            #这一步是老鼠走，则上一步是猫走,考虑上一步猫能走到i的所有情况
                    for k in graph[i]:
                        q.append([k, j, 1])
                else:
                    for k in graph[j]:
                        q.append([i, k, 0])
        return 0

g = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
s = Solution()
print(s.catMouseGame(g))