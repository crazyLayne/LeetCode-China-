import collections
class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        def MCD(a, b):      #a<=b
            if a==0: return b
            else:
                c = b%a
                return MCD(min(c,a),max(c,a))
        d = collections.Counter(deck)
        v = list(set(d.values()))
        if len(v)<=1:
            if len(deck)>=2: return True
            else: return False
        for i in range(len(v)):
            for j in range(i+1, len(v)):
                if MCD(min(v[i],v[j]), max(v[i],v[j]))<=1: return False
        return True