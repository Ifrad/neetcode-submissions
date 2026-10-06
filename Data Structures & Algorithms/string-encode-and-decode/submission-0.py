class Solution:

    def encode(self, strs: List[str]) -> str:
        array = []
        for word in strs:
            length = len(word)
            pref = f"{length}"
            res = pref + "#" + word
            array.append(res)
        
        return "".join(array)


    def decode(self, s: str) -> List[str]:
        array = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            n = int(s[i:j])
            array.append(s[j+1:j+1+n])
            i = j + 1 + n
        return array
            


