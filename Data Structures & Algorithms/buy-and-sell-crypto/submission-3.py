class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = []
        min_left = prices[0] 
        for i in range(len(prices)):
            min_left = min(min_left, prices[i])
            left.append(min_left) 

        right = [0]*len(prices)
        max_right = 0
        for i in range(len(prices)-1, -1, -1):
            max_right = max(max_right, prices[i])
            right[i] = max_right 
        
        res = [right[i] - left[i] for i in range(len(right))] 

        return max(res)

            
            


        