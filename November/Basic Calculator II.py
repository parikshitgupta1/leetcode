class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        priority = {'+': 0, '-': 0, '*': 1, '/': 1}
        
        def operate(n1, n2, operator) -> int:
            if operator == '+':
                return n1 + n2
            if operator == '-':
                return n1 - n2
            if operator == '*':
                return n1 * n2
            if operator == '/':
                return n1 // n2
        
        num_stack = []
        operator_stack = []
        operator_set = set(['+', '-', '*', '/'])
        digit_set = set([str(digit) for digit in range(0, 10)])
        valid_set = set(operator_set).union(set(digit_set))
        
        temp = ''
        for c in s:
            if c not in valid_set:
                continue
            if c in digit_set:
                temp += c
            if c in operator_set:
                num_stack.append(int(temp))
                temp = ''
                while len(operator_stack) and priority[c] <= priority[operator_stack[-1]]:
                    n2 = num_stack.pop()
                    n1 = num_stack.pop()
                    operator = operator_stack.pop()
                    num_stack.append(operate(n1, n2, operator))
                operator_stack.append(c)
        num_stack.append(int(temp))

        while len(num_stack) != 1 and operator_stack:
            n2 = num_stack.pop()
            n1 = num_stack.pop()
            operator = operator_stack.pop()
            num_stack.append(operate(n1, n2, operator))

        return num_stack[-1] 
