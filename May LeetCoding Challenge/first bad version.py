# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        # Recursive divide-and-conquer helper function with the current upper n, lower n and n
        def helper(upper_n, lower_n, n):

            # Base case
            if n == upper_n and n == lower_n:
                return

            # If n is False and the next one is True, then n + 1 is the first bad version
            elif isBadVersion(n) == False and isBadVersion(n + 1) == True:
                return n + 1

            # If n is True and the one before is False, then n is the first bad version
            elif isBadVersion(n) == True and isBadVersion(n - 1) == False:
                return n

            # If n is False, then we have to look beyond n, so we set lower_n to n + 1 and
            # use (upper_n + n) // 2 to find the next middle index
            elif isBadVersion(n) == False:
                lower_n = n + 1
                return helper(upper_n, lower_n, ((upper_n + n) // 2))

            # If n is True, then we have to look before n, so we set upper_n to n - 1 and
            # use (upper_n + lower_n) // 2 to find the next middle index
            else:
                upper_n = n - 1
                return helper(upper_n, lower_n, ((upper_n + lower_n) // 2))

        # Initializing the helper function with the middle index n // 2
        return helper(n, 0, n // 2)
