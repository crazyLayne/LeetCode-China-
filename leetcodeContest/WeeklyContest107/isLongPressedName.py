class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if len(name)>len(typed): return False
        i = j = 0
        while i < len(name) and j < len(typed):
            c1 = name[i]
            st1 = i
            while i < len(name) and name[i]==c1:
                i += 1
            c2 = typed[j]
            st2 = j
            while j < len(typed) and typed[j]==c2:
                j += 1
            if c1!=c2 or i-st1 > j-st2: return False
        if i==len(name) and j==len(typed): return True
        else: return False
            