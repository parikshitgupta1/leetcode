class Solution:

    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(n) for n in version1.split('.')]
        v2 = [int(n) for n in version2.split('.')]
        l1 = len(v1)
        l2 = len(v2)
        if l1 < l2:
            v1 = self.addZero(v1, l2)
        elif l1 > l2:
            v2 = self.addZero(v2, l1)
        i = 0
        l = len(v1)
        while i < l:
            if v1[i] > v2[i]:
                return 1
            if v1[i] < v2[i]:
                return -1
            i += 1
        return 0

    def addZero(self, v, l):
        while len(v) < l:
            v.append(0)
        return v
