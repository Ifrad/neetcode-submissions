class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arranged = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in arranged:
                arranged[key].append(word)
            else:
                arranged[key] = [word]
            
        return list(arranged.values())

        
        
        
  
        
        

        
        
        