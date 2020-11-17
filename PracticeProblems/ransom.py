from collections import defaultdict
class Solution():
    def RansomNote(self,magazine,word):
        letters = defaultdict(int)
        for characters in magazine:
            letters[characters] += 1
        for character in word:
            if letters[character] > 0 :
                letters[character] -= 1
            else:
                return False
        return True
print(Solution().RansomNote(["a","b","c"],"ctab"))




