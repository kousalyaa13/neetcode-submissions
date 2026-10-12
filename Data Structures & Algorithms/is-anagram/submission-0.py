class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # first check: if the lengths are different, return False
        if len(s) != len(t):
            return False

        counts_s = defaultdict(int)
        counts_t = defaultdict(int)

        for char_s in s:
            counts_s[char_s] += 1
        for char_t in t:
            counts_t[char_t] += 1
        
        if counts_s != counts_t:
            return False
        return True

        

        
        