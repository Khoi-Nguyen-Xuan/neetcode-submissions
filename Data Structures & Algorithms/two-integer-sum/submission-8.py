class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = [];
        for i in range(len(nums)-1):
            j = i+1; 
            while nums[i]+nums[j] != target and j<len(nums)-1:
                j += 1; 
            
            if nums[i]+nums[j]==target: 
                result.append(i)
                result.append(j)
                return result
            

        

            
        