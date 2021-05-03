class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        
        
        courses.sort(key = lambda x: x[1])
        
       
        max_heap = []
        time = 0
        for duration,last_day in courses:
            heappush(max_heap, -duration)   
            time = time + duration
            if time > last_day:             
                taken = heappop(max_heap)
                time = time + taken
                
        return (len(max_heap))
