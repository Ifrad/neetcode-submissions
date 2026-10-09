class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j= len(heights)-1
        best = 0
        while i<j:
            area = (j-i) * min(heights[i],heights[j])
            if heights[i]>heights[j]:
                j-=1
            elif heights[i]<heights[j]:
                i+=1
            else:
                i+=1
            best = max(best,area)

            

        return best
            



        