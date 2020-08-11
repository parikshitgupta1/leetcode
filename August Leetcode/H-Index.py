class Solution:
    def hIndex(self, citations):

        citations.sort(reverse=True)
        for i, j in enumerate(citations):

            # find the first index where citation is smaller than or equal to array index
            if i >= j:
                return i

        return len(citations)


def main():
    h_arr = [3, 0, 6, 1, 5]
    solve = Solution()
    print(solve.hIndex(h_arr))


if __name__ == '__main__':
    main()
