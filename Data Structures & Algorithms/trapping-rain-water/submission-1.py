class Solution:
    def trap(self, height: List[int]) -> int:
        largest_l = []
        largest_r = [0]*len(height) 
        volume = 0

        max_left = 0
        for i in range(len(height)):
            if height[i] > max_left: max_left=height[i]
            largest_l.append(max_left)
        
        max_right = 0
        for i in range(len(height)-1, -1, -1):
            if height[i] > max_right: max_right=height[i]
            largest_r[i] = max_right 
        
        for i in range(len(height)): 
            each = min(largest_l[i], largest_r[i]) - height[i]

            volume += each if each > 0 else 0


        
        return volume 


