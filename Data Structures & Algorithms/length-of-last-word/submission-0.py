class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        length = 0

        # while letter is a whitespace, move point -1 to find a letter
        while s[i] == " ":
            i -= 1
        
        # while it is a letter
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1 # keep decrementing
        
        return length

        