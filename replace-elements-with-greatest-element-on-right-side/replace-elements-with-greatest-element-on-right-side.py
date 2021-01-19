class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest=arr[-1]
        for i,n in reversed(list(enumerate(arr))):
            arr[i]=greatest
            greatest=max(greatest,n)
        arr[-1]=-1 
        return arr
