"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

def group_anagrams(str_list):

    anagrams = {}

    for word in str_list:
        key = str(sorted(word))
        anagrams[key] = anagrams.get(key,[]) + [word]
    
    return list(anagrams.values())