class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num,i])

        A.sort()

        i = 0
        j = len(nums)-1-i
        current_total = A[i][0] + A[j][0]

        while(current_total!=target):
            if current_total>target:
                j -= 1
            elif current_total<target:
                i += 1 

            current_total = A[i][0] + A[j][0]

        return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]

      




            

        

            
        