class Solution:
    def bitwiseComplement(self, N: int) -> int:
        b = bin(N)[2:]
        res = ''
        for i in b:
            if i == '0':
                res+='1'
            else:
                res+='0'
        return int(res,2)
