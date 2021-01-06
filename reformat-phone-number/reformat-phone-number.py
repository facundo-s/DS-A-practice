class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        clean_number = number.replace(" ", "")
        clean_number = clean_number.replace("-", "")
        
        number_list=[]
        while len(clean_number)//3>0 and len(clean_number)>4:
            number_list.append(clean_number[:3])
            clean_number=clean_number[3:]
        
        #at this point clean_number is either 4,3 or 2 elements
        remainder_length = len(clean_number)
        if remainder_length==4:
            number_list.append(clean_number[:2])
            number_list.append(clean_number[2:])
        elif remainder_length==3 or remainder_length==2:
            number_list.append(clean_number)
            
        return "-".join(number_list)
        
        
            
