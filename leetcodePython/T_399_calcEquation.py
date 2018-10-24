class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        weights = {}    # {(a,b):1, (b,a):1,...} 存储边的权重
        ps = set()      #所有点集合
        zeros = set()      # 存储是零的点
        for i in range(len(equations)):
            a = equations[i][0]
            b = equations[i][1]
            v = values[i]
            ps.add(a); ps.add(b)
            if v == 0: 
                zeros.add(a)
                weights[(a,b)] = v
            else:
                weights[(a,b)] = v
                weights[(b,a)] = 1/v
        for k in ps:
            for i in ps:
                for j in ps:
                    if (i,j) not in weights.keys() and (i,k) in weights.keys() and weights[(i,k)] != 0 and (k,j) in weights:
                        weights[(i,j)] = weights[(i,k)] * weights[(k,j)]
        res = []
        for q in queries:
            a,b = q[0],q[1]
            if a not in ps or b not in ps: res.append(-1.0)     #存在未知点
            elif b in zeros or (a,b) not in weights.keys(): res.append(-1.0)       #分母为0
            elif a in zeros: res.append(0.0)        #分子为零
            elif a == b: res.append(1.0)           #自身除自身
            else: res.append(weights[(a,b)])
        return res