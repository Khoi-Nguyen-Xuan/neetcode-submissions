class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=r=0
        res = 0
        track = [0]*26

        for r in range(len(s)):
            track[ord(s[r]) - ord("A")] += 1


            window_size = r-l+1
            gap = window_size-max(track) 


            while(gap > k): 
                track[ord(s[l]) - ord("A")] -= 1
                l += 1
                window_size = r-l+1
                gap = window_size-max(track)

            res = max(res, window_size) 

            

        return res 






        
        



        


        