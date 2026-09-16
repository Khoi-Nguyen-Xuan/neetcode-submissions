class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height)-1

        max_L = height[i]
        max_R = height[j]
        volume = 0 

        while(i<j):
            if(height[i]<height[j]):
                i += 1 
                volume += max_L - height[i] if (max_L - height[i]) > 0 else 0 
                if height[i] > max_L: max_L = height[i]

            else:
                j -= 1 
                volume += max_R - height[j] if (max_R - height[j]) > 0 else 0
                if height[j] > max_R: max_R = height[j]
                
        
        return volume


