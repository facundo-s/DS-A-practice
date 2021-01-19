class Solution:
    def maximum69Number (self, num: int) -> int:
#         largest_digit=1
#         while num//largest_digit>9:
#             largest_digit*=10
        
#         while largest_digit>0.9 and num//largest_digit!=6:
#             print(num, largest_digit, num//largest_digit)
#             largest_digit/=10
        
#         if largest_digit==0:
#             return num
#         else:
#             return num-6*largest_digit+9*largest_digit
​
        num = str(num)
        for i, n in enumerate(num):
            if num[i]=="6":
                num=num[:i]+"9"+num[i+1:]
                break
        return int(num)
