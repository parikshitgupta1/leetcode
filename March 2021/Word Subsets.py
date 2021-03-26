class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        lowlet = 'qwertyuiopasdfghjklzxcvbnm'
        fB = {c: 0 for c in lowlet}
        for w in B:
            fw = {c: 0 for c in lowlet}
            for c in w:
                fw[c] += 1
            for c in fw:
                fB[c] = max(fB[c], fw[c])
        res = []
        for w in A:
            fw = {c: 0 for c in lowlet}
            for c in w:
                fw[c] += 1
            if all(fw[c] >= fB[c] for c in lowlet):
                res.append(w)
        return res
