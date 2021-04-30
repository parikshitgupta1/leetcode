class Solution:
    def powerfulIntegers(self, x, y, bound):
        powerful = set()
        power_x = 1
        while power_x < bound:
            power_y = 1
            while power_y <= bound - power_x:
                if power_x + power_y not in powerful:
                    powerful.add(power_x + power_y)
                if y == 1:
                    break
                power_y *= y
            if x == 1:
                break
            power_x *= x
        return list(powerful)

a = Solution()
print(a.powerfulIntegers(2, 3, 10))
