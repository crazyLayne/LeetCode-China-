class Solution:
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        def getCount(formula, mutiple, d):
            if formula == "": return
            i,j = 0,1
            while i<len(formula):
                while j<len(formula) and not (formula[j]>='A' and formula[j]<='Z'):     #不是大写字母
                    if formula[j]>='0' and formula[j]<='9':
                        break
                    j+=1
                atom = formula[i:j]
                c = 1
                i,j = j,j+1
                if i<len(formula) and formula[i]>='0' and formula[i]<='9':
                    while j<len(formula) and not (formula[j]>='A' and formula[j]<='Z'):     #不是大写字母
                        j+=1
                    c = int(formula[i:j]) 
                    i=j
                    j=i+1
                d[atom] = (d[atom]+c*mutiple) if atom in d else c*mutiple
        def split(formula, mutiple, d):     #将formula拆分成当前和几个括号内的迭代
            if formula!="":
                # 确定是否还有括号
                firstleft = left = formula.find('(')
                if firstleft != -1:
                    st = 1          #肯定有括号
                    right = left+1
                    while left<len(formula):
                        while right<len(formula):
                            if formula[right]=='(':
                                st += 1
                            elif formula[right]==')':
                                st -= 1
                            if st==0:
                                numend = right+1
                                while numend<len(formula) and formula[numend]>='0' and formula[numend]<='9': numend+=1
                                nextM = int(formula[right+1:numend]) if formula[right+1:numend] != "" else 1
                                split(formula[left+1:right], mutiple*nextM, d)
                                break
                            right+=1
                        nextleft = formula[numend:].find('(')
                        if nextleft==-1: 
                            getCount(formula[numend:], mutiple, d)
                            break
                        getCount(formula[numend:numend+nextleft], mutiple, d)
                        left, right, st = numend+nextleft, numend+nextleft+1, 1
                    
                    formula = formula[:firstleft]
                # 处理当前的部分，即没有括号的部分
                getCount(formula, mutiple, d)
                
        d = {}
        split(formula, 1, d)
        res = []
        keys = sorted(d.keys())
        for k in keys:
            res.append(k)
            if d[k]>1: res.append(str(d[k]))

        return "".join(res)

s = Solution()
# print(s.countOfAtoms("K4(ON(SO3)2)2"))
# print(s.countOfAtoms("((N42)24(H5)16)14"))
print(s.countOfAtoms("((N7Li31C7B10Be37B23H2H11Li40Be15)26(OBLi48B46N4)25(O48C22He)2N10O34N15B33Li39H34H26B15B23C31(C36N38O33Li38H15H46He21Be38B50)8)3"))