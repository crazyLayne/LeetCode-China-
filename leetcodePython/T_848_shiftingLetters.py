class Solution:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        shift = 0
        S = list(S)
        for i in range(len(shifts)-1, -1, -1):
            shift += shifts[i]
            S[i] = chr((ord(S[i])-97 + shift)%26 +97)
        return ''.join(S)

S = 'abc'
shifts = [3, 5, 9]
slt=Solution()
print(slt.shiftingLetters(S, shifts))
