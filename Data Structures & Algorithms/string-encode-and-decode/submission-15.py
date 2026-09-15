class Solution:

    def encode(self, strs: List[str]) -> str:
        if(len(strs)==0): return ""
        
        res = []

        for s in strs:
            size = len(s)
            res.append(f"{size}#{s}")
        
        return "".join(res) 
        
    def decode(self, s: str)->List[str]:
        if(s == ""): return []
        res = []

        while(s!=""): 
            special_i = s.index("#")
            size = int(s[:special_i]) 
            s = s[special_i+1:]
            res.append(s[:size])
            s = s[size:] 

        return res 