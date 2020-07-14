class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_deg = (hour*30)%360 + (0.5)*minutes
        minute_deg = ((minutes/5)*30)%360
        
        if(abs(hour_deg-minute_deg)>180):
            return 360 - abs(hour_deg-minute_deg)
        
        else:
            return abs(hour_deg-minute_deg)
