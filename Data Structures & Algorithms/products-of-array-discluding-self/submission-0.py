class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array = []
        for i in range(len(nums)):
            array.append(1)
            if i== 0:
                array[i]*=1 
            else:
                array[i] = array[i-1]* nums[i-1]

        right = 1
        for j in range(len(nums)-1,-1,-1):
                array[j]*= right 
                right *= nums[j]
            
        return array

            
        
     
        
        
            
            
        

        