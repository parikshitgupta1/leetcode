import itertools

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        lcs = [[0 for k in range(len(text2)+1)]for j in range(len(text1)+1)]
        result = 0
        for i in range(len(text1)+1):
            for j in range(len(text2)+1):
                if i==0 or j==0:
                    lcs[i][j] = 0
                elif text1[i-1] == text2[j-1]:
                    lcs[i][j] = lcs[i-1][j-1] + 1
                    result = max(result, lcs[i][j])
                else:
                    lcs[i][j] = max(lcs[i-1][j],lcs[i][j-1])
        return lcs[len(text1)][len(text2)]





if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonSubsequence("abcde","dce"))
