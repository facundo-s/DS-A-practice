class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        last_day=0
        last_monday=0
        day_of_week=1
        total_money=0
        while n>0:
            if day_of_week>7:
                day_of_week=day_of_week%7
            if day_of_week==1:
                last_monday+=1
                last_day = last_monday
                total_money+=last_monday
                
            else:
                last_day+=1
                total_money+=last_day
​
            day_of_week+=1
            n-=1
        return total_money
        
        
