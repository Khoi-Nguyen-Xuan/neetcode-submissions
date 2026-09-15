class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_dict = {}
        longest = 0

        for num in nums:
            my_dict[num] = 1 + my_dict.get(num,0)
        
        for num in nums:
            if (num-1) not in my_dict: 
                length = 0 
                while (num+length) in my_dict:
                    length += 1
                longest = max(length,longest)


        return longest 



            


        