class Solution:
    """
    @param accounts: List[List[str]]
    @return: return a List[List[str]]
    """
    def accountsMerge(self, accounts):
        result = []
        self.father = dict()
        self.owner = dict()
        self.mp = dict()
        for account in accounts:
            n = len(account)
            for i in range(1,n):
                self.father[account[i]] = account[i]
                self.owner[account[i]] = account[0]\
        # union all the emails under the same account
        for account in accounts:
            n = len(account)
            for i in range(2,n):
            # let email1 be the root of all other emails under the same account
                self.connect(account[i], account[1])
        for account in accounts:
            n = len(account)
            for i in range(1,n):
                # account[1] <-> set of account[i]s
                tmp = self.find(account[i])
                if tmp not in self.mp:
                    self.mp[tmp] = []
                self.mp[tmp].append(account[i])
        for key in self.mp:
            record = []
            tmp = sorted(list(set(self.mp[key])))
            record.append(self.owner[key])
            record = record + tmp
            result.append(record)
        return result
    def find(self,s):
        if self.father[s] == s:
            return s
        # path compression
        self.father[s] = self.find(self.father[s])
        return self.father[s]
    def connect(self,a,b):
        fa,fb = self.find(a),self.find(b)
        if fa != fb:
            self.father[fa] = fb
