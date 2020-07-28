class Solution(object):
    def leastInterval(self, tasks, n):
        frequencies = {} 
        output = 0
        if n == 0:
            return len(tasks)
        for k in tasks:
            frequencies[k] = frequencies.get(k,0)+1
            
        max_value = max(frequencies.values())

        max_value_occurrences = 0
        for value in frequencies.values():
            if value == max_value:
                max_value_occurrences += 1
                
        
        return max((max_value-1)*(n+1)+max_value_occurrences, len(tasks))
