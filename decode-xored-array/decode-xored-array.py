class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        # if a XOR b == c, a XOR c == b? I think yes
        arr=[None]*(len(encoded)+1)
        arr[0]=first
        for i in range(len(encoded)):
            arr[i+1]=arr[i]^encoded[i]
            
        return arr
        
