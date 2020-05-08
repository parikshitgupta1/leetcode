class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        length = len(coordinates)
        if length <= 2:
            count = True
        else:
            x1,y1 = coordinates[0]
            x2,y2 = coordinates[1]
            if x2-x1 == 0 or y2-y1 == 0:
                    slope = 0
            else:
                    slope = (y2-y1)/(x2-x1)

            for i in range(1,length-1):
                x1,y1 = coordinates[i]
                x2,y2 = coordinates[i+1]
                if x2-x1 == 0 or y2-y1 == 0:
                    s = 0
                else:
                    s = (y2-y1)/(x2-x1)

                if s == slope:
                    count = True
                else:
                    count = False
                    break
        return count
