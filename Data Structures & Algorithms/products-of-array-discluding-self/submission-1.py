class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: 
        prefix, postfix = [1]*len(nums), [1]*len(nums)

        i = 0
        prod_pre = 1
        prod_post = 1
        
        for i in range(len(nums)):
            prod_pre *= nums[i] 
            prefix[i] = prod_pre
        
        for i in range(len(nums)-1, -1,-1):
            prod_post *= nums[i] 
            postfix[i] = prod_post

        
        output = [1]*len(nums) 
        for i in range(len(output)):
            if(i==0):
                output[i] *= postfix[i+1] 
            elif (i==len(output)-1):
                output[i] *= prefix[i-1] 
            else:
                output[i] = prefix[i-1] * postfix[i+1] 

        return output 
        
        


