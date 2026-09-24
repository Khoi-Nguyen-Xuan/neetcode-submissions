class Solution:
    def binary_search(self, l: int, r: int, nums: List[int], target: int) -> int:
        while(l<=r):
            m = int((l+r)/2)
            if nums[m] == target: 
                return m 
            elif nums[m] > target:
                r = m-1 
            else:
                l = m+1 

        return -1 
    
    def search(self, nums: List[int], target:int) -> int:
        return self.binary_search(0, len(nums)-1, nums, target)