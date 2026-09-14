class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}

        for num in nums:
            if num not in my_dict:
                my_dict[num] = 0
            else:
                return True; 
        
        return False; 