class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1: return 1
        if s== "": return 0 
        seen = {}
        i = 0
        j=1
        res = 0
        while(i<len(s)-1):
            if (i==j): j+=1 
            
            seen[s[i]] = i

            
            while s[j] not in seen:
                if j == len(s)-1:
                    break 
                seen[s[j]] = j
                j += 1
            
            if j != len(s)-1: 
                res = max(res, j-i)
                while (s[j] in seen):
                    del seen[s[i]] 
                    i += 1 
            else:
                if s[j] in seen: 
                    res = max(res, j-i)
                else:
                    res = max(res, j-i+1)
                break 

            
        return res
