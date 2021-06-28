class Solution:

    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n  # Every child must have atleast one candy

        # First pass -> Going from left to right to satisfy conditions
        for i in range(0, n-1):
            if ratings[i+1] > ratings[i]:
                candies[i+1] = max(1+candies[i], candies[i+1])

        # Second pass -> Going from right to left to satisfy conditions
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(1+candies[i+1], candies[i])

        print(candies)
        return sum(candies)
