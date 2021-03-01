class Solution:
    def reverse(self, x: int) -> int:
        max_int = 2**31
        is_negative = x<0
        x=abs(x)
        
        return_x = 0
        while x!=0:
            digit = x%10
            x//=10
            
            if (return_x>max_int//10) or ((return_x==max_int//10) and digit>7):
                return 0
            
            return_x = return_x*10+digit
        
        if is_negative:
            return (-1)*return_x
        return return_x
            
            
        
#         if x>2**31 or x<(-(2**31-1)):
#             return 0
        
#         is_negative = x<0
#         if is_negative:
#             x=x*(-1)
        
#         x = str(x)
#         x = list(x)
#         x = reversed(x)
#         x = "".join(x)
#         x = int(x)
#         if is_negative:
#             x=x*(-1)
#         return x