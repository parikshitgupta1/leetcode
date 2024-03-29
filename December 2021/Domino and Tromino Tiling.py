class Solution:
    """
    @param N: a integer
    @return: return a integer
    """
    def numTilings(self, N):
        if N < 3:
            return N
        
        MOD = 1000000007
        
        f = [[0, 0, 0] for i in range(N + 1)]
        f[0][0] = f[1][0] = f[1][1] = f[1][2] = 1
        for i in range(2, N + 1):
            f[i][0] = (f[i - 1][0] + f[i - 2][0] + f[i - 2][1] + f[i - 2][2]) % MOD;
            f[i][1] = (f[i - 1][0] + f[i - 1][2]) % MOD;
            f[i][2] = (f[i - 1][0] + f[i - 1][1]) % MOD;
        
        return f[N][0]
