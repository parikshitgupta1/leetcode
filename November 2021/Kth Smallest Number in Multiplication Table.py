class Solution:
    """
    @param m: a integer
    @param n: a integer
    @param k: a integer
    @return: return a integer
    """
    def count(self, v, m, n) :
        count = 0
        for i in range(1,m + 1) :
            temp = min(v // i , n)		#每次求出i行小于等于v的数字数量，求和即可
            count += temp
        return count
    def findKthNumber(self, m, n, k):
        # write your code here
        low , high = 1 , m * n + 1			#枚举答案上下边界
        while low < high :
            mid = low + (high - low) // 2
            c = self.count(mid, m ,n)
            if c >= k :
                high = mid
            else :
                low = mid + 1
        return high
