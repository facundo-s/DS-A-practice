class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        j=1
        for i in range(0, len(A),2):
            if A[i]%2==0:
                continue
            while j<len(A):
                if A[j]%2==0:
                    tmp=A[i]
                    A[i]=A[j]
                    A[j]=tmp
                    break
                j+=2
        return A