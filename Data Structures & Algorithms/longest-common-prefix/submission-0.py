class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        # start with first word
        for word in range(len(strs[0])):
            for letter in strs:
                if word == len(letter) or letter[word] != strs[0][word]:
                    return ans
            ans += strs[0][word]
        return ans



        