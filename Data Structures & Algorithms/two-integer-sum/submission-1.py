class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            partner = target - n
            if partner in d:
                return [d[partner],i]
            d[n] = i

        
        
       

                
                
        

        