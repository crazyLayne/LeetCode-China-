class Solution:
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        lenS = len(source)  #代码行数
        res = []
        i = 0
        while i<lenS:
            line = source[i]
            ncom1 = line.find('//')
            ncom2 = line.find('/*')
            if ncom1==-1 and ncom2==-1:         #两种注释都没有
                #do nothing
                res.append(source[i])
                i+=1
            elif ncom2 == -1 or (ncom1!=-1 and ncom1<ncom2):    #第二种注释没有，或者两种注释都有且第一种靠前
                if ncom1==0:        #删除这一行
                    i += 1  
                else:               #删除这行的部分内容
                    res.append(source[i][:ncom1])
                    i+=1
            else:                               #第一种注释没有，或者第二种注释靠前
                ncom3 = line[ncom2+2:].find('*/')
                if ncom3!=-1:       #结束标识在同一行内
                    newline = line[:ncom2]+line[ncom2+2+ncom3+2:]
                    if newline=="": #删除这一行
                        i+=1
                    else:
                        source[i] = newline
                else:              #在之后的行中寻找结束标识
                    if ncom2==0:        #删除这一行
                        i += 1  
                    else:               #删除这行的部分内容
                        res.append(source[i][:ncom2])
                        i+=1
                    line = source[i]
                    while i<lenS-1 and '*/' not in line: 
                        i += 1
                        line = source[i]
                    ncom3 = line.find('*/')
                    #找到最近的结束标识
                    newline = line[ncom3+2:]
                    if newline=='':
                        i+=1
                    else:
                        source[i] = res[-1]+newline
                        del res[-1]                        
        return res
        
# source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
source = ["a/*comment", "line", "more_comment*/b/*sdf*/c/*as","fsa*/d//sadf"]
s = Solution()
print(s.removeComments(source))

        