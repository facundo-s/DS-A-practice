class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        return_string = ""
        i=0
        while i<len(command):
            if command[i] == "G":
                return_string +="G"
                i+=1
                continue
            elif command[i]=="(":
                if command[i+1]=="a":
                    return_string+="al"
                    i+=4
                    continue
                else:
                    return_string+="o"
                    i+=2
                    continue
            #no catch here, but all cases have been covered
            
        return return_string
