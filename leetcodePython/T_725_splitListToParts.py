class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        listLen = 0
        p = root
        while p!=None:
            listLen += 1
            p = p.next
        avg = listLen//k
        rem = listLen%k
        res = [[] for _ in range(k)]
        p = root
        for i in range(k):
            if p==None: break
            res[i] = p
            for _ in range((avg) if rem>0 else avg-1):
                p=p.next
            rem -= 1
            q, p = p, p.next
            q.next=None
        return res