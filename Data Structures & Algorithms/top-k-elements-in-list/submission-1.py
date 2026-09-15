class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracking_dict = {}
        for num in nums:
            if num not in tracking_dict:
                tracking_dict[num] = 0
            tracking_dict[num] += 1 
        
        res_val = sorted(list(tracking_dict.values()), reverse = True)[:k]

        matching_keys = [k for k, v in tracking_dict.items() if v in res_val]

        return matching_keys

        