class Solution:
    def originalDigits(self, s: str) -> str:
        count = Counter(s)
        print(count)
        digits = {'z':'0','w':'2','u':'4','x':'6','g':'8','h':'3','f':'5','v':'7','o':'1','i':'9'}
        words = {
            'z': 'zero',
            'w': 'two',
            'u': 'four',
            'x': 'six',
            'g': 'eight',
            'h': 'three',
            'f': 'five',
            'v': 'seven', 
            'o': 'one',
            'i': 'nine'
        }
        
        res = []
        for c in 'zwuxghfvoi':
            if c in count:
                res.append(count[c] * digits[c])
                f = count[c]
                for i in words[c]:
                    count[i] -= f
        
        return ''.join(sorted(res))
