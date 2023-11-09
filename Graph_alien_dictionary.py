""" 269. Alien Dictionary
Attempted
Hard
Topics
Companies
There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary. Now it is claimed that the strings in words are 
sorted lexicographically
 by the rules of this new language.

If this claim is incorrect, and the given arrangement of string in words cannot correspond to any order of letters, return "".

Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.

 

Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Example 2:

Input: words = ["z","x"]
Output: "zx"
Example 3:

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "". """
 

class Solution:
    def alienOrder(self, words: list[str]) -> str:
        adj = {c:[] for word in words for c in word}
        
        for i in range(len(words)-1):
            word1,word2 = words[i],words[i+1]
            length = min(len(word1),len(word2))
            if len(word1) > len(word2) and word1[:length] == word2[:length]:
                return ""
            for j in range(length):
                if word1[j] != word2[j]:
                    adj[word1[j]].append(word2[j])
                    break
        
        print(adj)
        result = []
        visited = {}
        def dfs(node):
            visited[node] = 1
            neighbors = adj[node]
            
            for neigh in neighbors:
                if neigh not in visited:
                    if not dfs(neigh):
                        return False
                else:
                    if visited[neigh] == 1:
                        return False
            visited[node] = 2
            result.append(node)

            return True
        
        for x in adj.keys():
            if x not in visited:
                if not dfs(x):
                    return ""
        
        word = ''.join(result[::-1])

        return word
    
sol = Solution()
print(sol.alienOrder(["wrt","wrf","er","ett","rftt"]))
print(sol.alienOrder(["z","x"]))
print(sol.alienOrder(["z","x","z"]))