class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        #assume that by reversing you can achieve any ordering
        if len(target)!=len(arr):
            return False
        for element in arr:
            if element not in target:
                return False
            target.remove(element)
        return True
        