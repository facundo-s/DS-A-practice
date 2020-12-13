class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        longest_time=-1
        longest_letter='zz'
        last_time=0
        for i in range(len(releaseTimes)):
            current_time = releaseTimes[i]-last_time
            last_time = releaseTimes[i]
            if current_time>longest_time:
                longest_time=current_time
                longest_letter = keysPressed[i]
            elif current_time==longest_time:
                longest_letter = max(longest_letter+keysPressed[i])
        return longest_letter
            
        
