class Solution:
	def buddyStrings(self, A: str, B: str) -> bool:
		if len(A) != len(B):
			return False

		if A == B and len(set(A)) < len(A):
			return True

		differences = []
		for i in range(len(A)):
			if A[i] != B[i]:
				differences.append((A[i], B[i]))

		if len(differences) == 2 and differences[0] == differences[-1][::-1]:
			return True

		return False
