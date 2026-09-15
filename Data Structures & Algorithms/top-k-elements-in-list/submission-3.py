class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracking_dict = {}
        for num in nums:
            if num not in tracking_dict:
                tracking_dict[num] = 0
            tracking_dict[num] += 1 
        
        result_dict = dict(sorted(tracking_dict.items(), key=lambda item: item[1], reverse=True))
        result = list(result_dict.keys())[:k]

        return result 

        