class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)
        l = 1
        best = 0
        for n in seq:
            curr = n
            l=1
            if curr-1 in seq:
                continue
            while curr +1 in seq:
                l+=1
                curr = curr+1
            best = max(best,l)
        return best

               
            
            
        



        