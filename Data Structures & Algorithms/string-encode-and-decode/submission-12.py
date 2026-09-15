class Solution:

    def encode(self, strs: List[str]) -> str:
        if(len(strs)==0): return ""
        
        sizes, res = [], []

        for s in strs:
            sizes.append(len(s))
        for sz in sizes:
            res.append(str(sz))
            res.append(',')
        res.append('#')
        res.extend(strs)
        return ''.join(res)
        
    def decode(self, s: str)->List[str]:
        if(s == ""): return []

        index_special = s.index('#')
        sizes, strs = s[0:index_special], s[index_special+1:]

        sizes = sizes.split(",")
        sizes = sizes[:len(sizes)-1]
        
        res = []
        print(sizes)
        for size in sizes:
            res.append(strs[:int(size)])
            strs = strs[int(size):]

        return res 