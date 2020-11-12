class Solution:
    def validSquare(self, p1, p2, p3, p4):
        if p1 == p2 == p3 == p4: return False

        p1,p2,p3,p4 = sorted([p1,p2,p3,p4])
        if p2[1] < p3[1]: p2,p3 = p3,p2

        return p3 == [p1[0] + (p2[1]-p1[1]), p1[1] - (p2[0]-p1[0])]\
           and p4 == [p2[0] + (p2[1]-p1[1]), p2[1] - (p2[0]-p1[0])] 
