class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        my_dict = dict()
        
        for i in range(len(s)):
            if s[i] not in my_dict.keys():
                if t[i] not in my_dict.values():
                    my_dict[s[i]] = t[i]
                else:
                    return False  # Two chars cannot map to the same char
                
            else:
                if my_dict[s[i]] != t[i]:
                    return False  # If already mapped and chars are not the same
                
        return True    
