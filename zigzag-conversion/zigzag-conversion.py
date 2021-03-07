class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if (numRows == 1):
            return s
    
        shuffle = []#[None]*len(s)
        cycle = 2*numRows-2
        
        for i in range(numRows):
            for j in range(0,len(s)-i,cycle):
                shuffle.append(s[j+i])
                if (i!=0) and (i!=numRows-1) and (j+cycle-i<len(s)):
                    shuffle.append(s[j+cycle-i])
        
        return "".join(shuffle)
        
        
#         for i, c in enumerate(s):
#             # first n are in row
#             # n-2 are in diagonal
#             # next n are in row
            
#             location = (i//numRows)*(i%numRows)
            
#         for i in range(len(s)):
#             if i%numRows == 1:
#                 shuffle[i]= (2*numRows-2)*i//numRows # numrows+numrows-2
#             else if 
        """
        CASE 2:
        
        PAYPALI
        SHIRING
        
        CASE 3:
        PAY
         P
        ALI
         S
        HIR
         I 
        NG
        
        CASE 4:
        PAYP
          A
         L
        ISHI
          R
         I
        NG
    
        CASE 5:
        PAYPA
           L
          I
         S
        HIRIN
           G
        
        
        CASE 6:
        PAYPAL
            I
           S
          H
         I
        RING
        
        CASE 7
        PAYPALI
             S
            H
           I
          R
         I
        NG
        
        CASE 8:
        
        THERE ARE 14 CASES
        """
        