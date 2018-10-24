class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        err = 0
        st = 0
        for s in S:
            if s == "(":
                st += 1
            else:
                if st==0:
                    err+=1
                else:
                    st -= 1
        err += st
        return err
