""" Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]] """
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        myHash = {}

        for word in strs:
            sorted_wrd = ''.join(sorted(word))
            if sorted_wrd in myHash:
                myHash[sorted_wrd].append(word)
            else:
                myHash[sorted_wrd] = [word]
            
        return myHash.values()