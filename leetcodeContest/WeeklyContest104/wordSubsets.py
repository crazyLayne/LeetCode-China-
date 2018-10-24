import collections
class Solution:
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        As = [collections.Counter(list(a)) for a in A]
        Bs = [collections.Counter(list(b)) for b in B]
        d = {}
        for b in Bs:
            for k,v in b.items():
                if k in d:
                    d[k] = max(d[k], v)
                else:
                    d[k] = v
        res = []
        for i,a in enumerate(As):
            flag = True
            for k,v in d.items():
                if k not in a.keys() or v>a[k]:
                    flag = False
                    break
            if flag: res.append(A[i])
        return res