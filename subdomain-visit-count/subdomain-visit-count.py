class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        sub_dom_dict={}
        for domain in cpdomains:
            number, domain = domain.split(" ")
            domain = domain.split(".")
            for i in range(len(domain)):
                sub_dom=".".join(domain[i:])
                if sub_dom in sub_dom_dict:
                    sub_dom_dict[sub_dom]+=int(number)
                else:
                    sub_dom_dict[sub_dom]=int(number)
        output_list = []
        for key in sub_dom_dict.keys():
            output_list+=[str(sub_dom_dict[key])+" "+key]
        
        return output_list
