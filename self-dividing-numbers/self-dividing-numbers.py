class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        output=[]
        for i in range(left, right+1, 1):
            passed=True
            for digit in str(i):
                if digit=="0":
                    passed=False
                    break
                digit=int(digit)
                if i%digit!=0:
                    passed=False
            if passed:
                output+=[i]
                
        return output
                
