class Solution:

  def numSubarrayBoundedMax(self, A, L, R):
    # Write your code here
    curr, size, res = 0, len(A), 0
    while (curr < size):
      if L <= A[curr] <= R:
        st, fl = curr - 1, curr + 1
        while (st >= 0 and A[st] < A[curr]):
          st -= 1
        while (fl < size and A[fl] <= A[curr]):
          fl += 1
        res += (fl - curr) * (curr - st)
      curr += 1
    return res
