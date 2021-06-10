class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __lt__(self, other):
        if self.start == other.start:
            return self.end < other.end 
        return self.start < other.start
        
class MyCalendar:

    def __init__(self):
        self.booked = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        new_node = Node(start, end-1)   # range inclusive [start, end-1]
        index = bisect.bisect_left(self.booked, new_node)
        if index > 0:
            left_node = self.booked[index - 1]
            if new_node.start <= left_node.end:
                return False
        if index < len(self.booked):
            right_node = self.booked[index]
            if new_node.end >= right_node.start:
                return False
        bisect.insort_left(self.booked, new_node)
        return True
