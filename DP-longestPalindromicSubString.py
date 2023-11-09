""" 5. Longest Palindromic Substring
Solved
Medium
Topics
Companies
Hint
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters. """
def longestPalindr(myStr):

    longSt = ''
    for i in range(len(myStr)):
        left = i
        right =i
        while left >= 0 and right <len(myStr) and myStr[left] == myStr[right]:
            if right -left > len(longSt):
                longSt = myStr[left:right+1]
            left = left - 1
            right = right + 1
    
    for i in range(len(myStr)):
        left = i
        right = i +1
        while left >= 0 and right <len(myStr) and myStr[left] == myStr[right]:
            if right -left > len(longSt):
                longSt = myStr[left:right+1]
            left = left - 1
            right = right + 1
    
    return longSt

#print(longestPalindr("abbacd"))
#print(longestPalindr("abbbacd"))
#print(longestPalindr("aabbaacddc"))
print("================================DUGGU's Question ===========================")
print("============================"+ longestPalindr("agggagggacdc")+"=========================")
