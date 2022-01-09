class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        direction = 'N'
        directions = {'N' : ['W', 'E'], 'S' : ['E', 'W'], 'E' : ['N', 'S'],'W' : ['S', 'N']}
        positions = {'N' : [0, 1], 'S' : [0, -1], 'E' : [1, 0], 'W' : [-1, 0]}
        for instruction in instructions:
            if instruction == 'L':
                direction = directions[direction][0]
            elif instruction == 'R':
                direction = directions[direction][1]
            else:
                x += positions[direction][0]
                y += positions[direction][1]
        return direction != 'N' or x == y == 0
