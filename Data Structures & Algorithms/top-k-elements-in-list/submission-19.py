class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        
        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        freq_array = [[] for i in range(len(nums)+1)]

        for key, value in count.items():
            freq_array[value].append(key) 

        #Wrong because can have the same frequency 
        result = []
        for i in range(len(freq_array)-1,0,-1):
            for num in freq_array[i]:
                result.append(num)
                if(len(result)==k): 
                    return result
            
        return result

        