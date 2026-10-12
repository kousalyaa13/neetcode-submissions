class Solution:
    def firstUniqChar(self, s: str) -> int:
        # character -> count
        count = defaultdict(int) 

        # for each character, add it as the key to the dict, then the value is 1 or +1 depending on if it already exists
        for char in s:
            count[char] += 1
        
        # trace two variables, index and character
        # if the value for the key is only 1, return the index of the key
        for index, char in enumerate(s):
            if count[char] == 1:
                return index
        return -1

        