class Solution:
    def mergemail(self, emails):
        res = []
        for email in emails:
            #判断email与res中哪些集合有交集，记录下来坐标，合并后删除res中原始
            if len(res)==0: res.append(list(set(email)))
            else:
                crossid = []
                for i in range(len(res)):   #遍历res
                    for em in email:        #遍历email中每个元素
                        if em in res[i]:
                            crossid.append(i)
                            break
                #合并crossid中元素
                newemails = email.copy()
                for cid in crossid:
                    newemails += res[cid]
                newemails = set(newemails)
                for cid in reversed(crossid):
                    del res[cid]
                res.append(newemails)
        return res
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        dic = {}
        for account in accounts:
            name = account[0]
            myemails = account[1:]
            if name in dic:
                emails = dic[name]
            else:
                emails = []
            emails.append(myemails)
            dic[name] = emails
        res = []
        # 合并 同名下可能是同人的集合
        for name,emails in dic.items():
            emails = list(self.mergemail(emails))
            for email in emails:
                email = sorted(list(email))
                res.append([name]+email)
        return res
    


# accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# s = Solution()
# print(s.accountsMerge(accounts))
test = [0]*10
test[0]=1
print(test)