class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = {}
        for i in range(len(s1)):
            target[s1[i]] = 1 + target.get(s1[i], 0) 
        
        l=r=0
        window = {}

        while (r<len(s2)):
            while (s2[r] not in target): 
                if r == len(s2)-1: 
                    return s2[r] == s1 
                r+=1 
                

            l=r 
            
            while (r<len(s2) and s2[r] in target):
                window[s2[r]] = 1 + window.get(s2[r], 0)

                if window == target: 
                    return True 

                while window[s2[r]] > target[s2[r]] and l<=r:
                    window[s2[l]] -= 1 
                    l += 1

                r += 1
            
            window = {}
        
        
        return False 

            
                

                



                

            
            
            
            

            

        return False 

            


