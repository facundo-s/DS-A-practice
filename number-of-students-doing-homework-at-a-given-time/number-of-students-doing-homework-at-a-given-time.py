class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum([startTime[i]<=queryTime and endTime[i]>=queryTime for i in range(len(startTime))]) 
    
    #[startTime[i]<=queryTime and endTime[i]>=queryTime for i in range(len(startTime))]
        
