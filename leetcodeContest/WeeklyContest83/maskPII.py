class Solution:
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        def maskEmail(S):
            S = S.lower()
            return S[0] + "*****" + S[S.find("@")-1:]
        def maskPhoneNumbers(S):
            numbers = []
            for c in list(S):
                if c.isdigit(): numbers.append(c)
            if len(numbers)==10:
                return "***-***-" + "".join(numbers[-4:])
            else:
                return "+" + "*"*(len(numbers)-10) + "-***-***-" + "".join(numbers[-4:])
        return maskEmail(S) if '@' in S else maskPhoneNumbers(S)