class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(reverse=True, key=lambda x:x[1])
        i=0
        total_units=0
        while truckSize>0:
            if boxTypes[i][0]==0:
                i+=1
            if i>=len(boxTypes):
                break
            total_units+=boxTypes[i][1]
            boxTypes[i][0]-=1
            truckSize-=1
        
        return total_units
                
