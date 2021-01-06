class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        occurrances = {}
        total_length = len(arr)
        for elem in arr:
            if elem in occurrances:
                occurrances[elem]+=1
            else:
                occurrances[elem]=1
        
        # we know the length of the array and the length of each repeated element
        # find the smallest combination of elements that reduces length to half
        
        #greedily, taking out the largest one first will work best
        sorted_occurrances=sorted(occurrances, key=occurrances.get)
        
        return_set=0
        half_length=total_length
        for a in reversed(sorted_occurrances):
            half_length-=occurrances[a]
            return_set+=1
            if half_length<=total_length/2:
                return return_set
